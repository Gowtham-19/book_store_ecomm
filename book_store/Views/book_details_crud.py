from django.shortcuts import render
# from book_store.models import Books
from json import load, loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book_store.serializer_Models import Books
from book_store.Dynamodb.dynamodb_services import dynamodbPutItem,dynamodbGetItem, dynamodbScan,dynamodbUpdateItem
# Create your views here.

# api for book details creation
@csrf_exempt
def add_BookDetails(request):

    try:
        body = loads(request.body)
        
        book_details = body["book_details"]
        # book_insert_data=[]
        
        for i in book_details:
            Item = {
                "book_title":i["book_title"],
                "book_author":i["book_author"],
                "book_category":i["book_category"],
                "desciption":i["description"],
                "book_quantity":i["book_quantity"],
                "book_cost":i["book_cost"]
            }
            res = dynamodbPutItem(body["client"],'Books',Item)

        print("value of res",res)
        return JsonResponse({"data":"Book Details Created"},status=200)
    except Exception as err:#pragma: no cover
        
        return JsonResponse({"error":err},status=500)


#api for getting book details
@csrf_exempt
def get_BookDetails(request):
    try:
        body=loads(request.body)

        res = dynamodbGetItem(body["client"],"Books",body["key"])
        return JsonResponse({"data":res},status=200)
    except Exception as err:#pragma: no cover
        return JsonResponse({"error":err},status=500)


#api for getting all book details
def get_allBookDetails(request):
    try:
        body=loads(request.body)
    
        res = dynamodbScan(body["client"],Books,True)
        return JsonResponse({"data":res},status=200)

    except Exception as err:
        return JsonResponse({"error":err},status=500)
#api for updating book details
@csrf_exempt
def update_BookDetails(request):
    try:
        body=loads(request.body)

        dynamodbUpdateItem(body["client"],"Books",body["key"],body["updated_values"])

        return JsonResponse({"data":"data updated"},status=200)
    except Exception as err:
        return JsonResponse({"data":err},status=500)