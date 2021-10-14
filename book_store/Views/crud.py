import collections
from django.shortcuts import render
from book_store.models import Category
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book_store.Dynamodb.dynamodb_services import dynamodbPutItem,dynamodbGetItem, dynamodbScan,dynamodbUpdateItem

# Create your views here.

#api for book category creation

# cluster="mongodb+srv://Gowtham:gowtham2012@cluster0.wztfa.mongodb.net/test"
# from pymongo import MongoClient
  
# try:
#     conn = MongoClient(cluster)
#     print("Connected successfully!!!")
# except:  
#     print("Could not connect to MongoDB")

@csrf_exempt
def create_Category(request):
    try:
        body = loads(request.body)
    
        category_data = body["category_data"]

        for i in category_data:
            Item = {
                "category_name":i["category_name"],
                "is_active":1,
            }
            dynamodbPutItem(body["client"],'Category',Item)
    
        
        return JsonResponse({"data":"categorys created"},status=200)

    except Exception as err:
        
        return JsonResponse({"error":err},status=500)


#api for fetching book categorys 
@csrf_exempt
def get_Categorys(request):
    try:
       
        body=loads(request.body)
        res = dynamodbScan(body["client"],"Category",True)
        return JsonResponse({"data":res},status=200)

    except Exception as err:
        return JsonResponse({"error":err},status=500)

