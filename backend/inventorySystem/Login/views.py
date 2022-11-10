from sqlite3 import DatabaseError
from uuid import UUID
from django.shortcuts import render
from Login.models import User
from Login.serializers import UserSerializer
# csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# viewsets
from rest_framework import viewsets, status
from rest_framework.response import Response

# hashing raw user instance password
from django.contrib.auth.hashers import make_password

# allow upload file
from django.core.files.storage import default_storage
# The IsAdminUser permission class will deny permission to any user,
# unless user.is_staff is True in which case permission will be allowed.
from rest_framework.permissions import IsAuthenticated
# for sending email
from Login.email import sendAuthEmail

from django.db.models import Q

import sys
sys.path.append("..")
from inventorySystem import settings


@csrf_exempt
def userApi(request, id=0):
    # get all the user
    if request.method=='GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data,safe=False)
    
    # add user
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        print(user_serializer.errors)
        return JsonResponse("Failed to add", safe = False)

    # edit user's data
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserId = user_data['UserId'])
        user_serializer = UserSerializer(user, data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to update", safe = False)

    # delete user through UserId, not the objectId
    elif request.method=='DELETE':
        user = User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Delete Successfully", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def userSearch(request, username):
    if request.method=='GET':
        user = User.objects.filter(Q(username__contains=username) | Q(username__icontains=username))
        user_serializer = UserSerializer(user, many=True)
    return JsonResponse(user_serializer.data,safe=False) 


class UserViewSet(viewsets.ModelViewSet):
    # ModelViewSet provided support for 'get', 'put', 'post' and 'delete'
    # However User cannot be added through this way for security regulations
    # of rest_framework.
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        name = self.request.query_params.get('name', None)
        print(name)
        if name is not None:
            #queryset = queryset.filter(Q(username__contains=name) | Q(username__icontains=name))
            queryset = queryset.filter(username__exact = name)
        return queryset

    # for cases an user to create another user
    def create(self, request, *args, **kwargs):
        username = request.data['username']
        pwd_raw = request.data['password']
        email = request.data['email']
        role = request.data['role']

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response("A user with that username already exists.", \
                status=status.HTTP_406_NOT_ACCEPTABLE)


        # create user_info as a User typed instence of serializer
        user_info = User(serializer)
        user_info.username = username
        user_info.set_password(pwd_raw)
        user_info.is_active = "True"
        user_info.email = email
        user_info.role = role
        # Uncomment the below if wanna login with this instance in Django Admin
        #user_info.is_superuser = "True" 
        user_info.is_staff = "True"

        self.perform_create(user_info)
        user_info.save()
        
        uuid = user_info.UUID
        url = request.build_absolute_uri(uuid)
        
        sendAuthEmail(url,user_info,settings)


        headers = self.get_success_headers(user_info)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        username = request.data['username']
        pwd_raw = request.data['password']
        pwd_hashed = make_password(pwd_raw)
        request.data['password'] = pwd_hashed

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
