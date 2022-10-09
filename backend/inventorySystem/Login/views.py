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


# allow upload file
from django.core.files.storage import default_storage
# The IsAdminUser permission class will deny permission to any user,
# unless user.is_staff is True in which case permission will be allowed.
from rest_framework.permissions import IsAuthenticated

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


class UserViewSet(viewsets.ModelViewSet):
    # ModelViewSet provided support for 'get', 'put', 'post' and 'delete'
    # However User cannot be added through this way for security regulations
    # of rest_framework.
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer