from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Login.models import User
from Login.serializers import UserSerializer
# Create your views here.

# allow upload file
from django.core.files.storage import default_storage
 

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
            return JsonResponse("Add Successfully", safe = False)
        return JsonResponse("Failed to add", safe = False)

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
