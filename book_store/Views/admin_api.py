# from django.shortcuts import render
from book_store.models import Category,User_Details,Books
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#api for book category creation
@csrf_exempt
def create_Category(request):
    try:
        body = loads(request.body)

        category_data = body["category_data"]
        insert_data=[]

        print("data of category",category_data)
        for i in category_data:
            insert_data.append(Category(category_name=i["category_name"]))

        Category.objects.bulk_create(insert_data)

        return JsonResponse({"data":"categorys created"})

    except Exception as err:#pragma: no cover
        return JsonResponse({"error":err})


#api for fetching book categorys 
@csrf_exempt
def get_Categorys(request):

    try:
       res = list(Category.objects.all().values())

       return JsonResponse({"data":res})

    except Exception as err:#pragma: no cover
        return JsonResponse({"error":err})
