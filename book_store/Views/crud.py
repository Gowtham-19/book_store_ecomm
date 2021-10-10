import collections
from django.shortcuts import render
from book_store.models import Category
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#api for book category creation

cluster="mongodb+srv://Gowtham:gowtham2012@cluster0.wztfa.mongodb.net/test"
from pymongo import MongoClient
  
try:
    conn = MongoClient(cluster)
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

@csrf_exempt
def create_Category(request):
    try:
        body = loads(request.body)
        data_base= conn["Ecomm"]

        # print("value of data_base",data_base.list_collection_names())

        collection = data_base["book_store_category"]

        category_data = body["category_data"]
        insert_data=[]

        # print("data of category",category_data)
        rec_id1 = collection.insert_many(body["category_data"])

       
        print("value of:",rec_id1)
        
        return JsonResponse({"data":"categorys created"})

    except Exception as err:#pragma: no cover
        print("value of err",err)
        return JsonResponse({"error":err})


#api for fetching book categorys 
@csrf_exempt
def get_Categorys(request):

    try:
       res = list(Category.objects.all().values())

       return JsonResponse({"data":res})

    except Exception as err:#pragma: no cover
        return JsonResponse({"error":err})
