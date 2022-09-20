from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from inventory.models import Item
from inventory.serializers import itemSerializer

# allow upload file
from django.core.files.storage import default_storage

# Create your views here.
def index(request):
    return render(request, "t_inventory/index.html")

@csrf_exempt
def itemApi(request, id=0):

    # get all the Item
    if request.method=='GET':
        item = Item.objects.all()
        item_serializer = itemSerializer(item, many=True)
        return JsonResponse(item_serializer.data,safe=False)
    
    # add Item
    elif request.method=='POST':
        item_data = JSONParser().parse(request)
        item_serializer = itemSerializer(data = item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        print(item_serializer.errors)
        return JsonResponse("Failed to add", safe = False)

    # edit Item's data
    elif request.method=='PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(idItem = item_data['idItem'])
        item_serializer = itemSerializer(item, data = item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        print(item_serializer.errors)
        return JsonResponse("Failed to update", safe = False)

    # delete user through UserId, not the objectId
    elif request.method=='DELETE':
        item = item.objects.get(idItem=id)
        item.delete()
        return JsonResponse("Delete Successfully", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)