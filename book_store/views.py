# from django.shortcuts import render
# from .models import Category,Books,User_Details
# from json import loads
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .Encryption_Service import encrypt_string
# # Create your views here.

# #api for book category creation
# @csrf_exempt
# def create_Category(request):
#     try:
#         body = loads(request.body)

#         category_data = body["category_data"]
#         insert_data=[]

#         print("data of category",category_data)
#         for i in category_data:
#             insert_data.append(Category(category_name=i["category_name"]))

#         Category.objects.bulk_create(insert_data)

#         return JsonResponse({"data":"categorys created"})

#     except Exception as err:#pragma: no cover
#         return JsonResponse({"error":err})


# #api for fetching book categorys 
# @csrf_exempt
# def get_Categorys(request):

#     try:
#        res = list(Category.objects.all().values())

#        return JsonResponse({"data":res})

#     except Exception as err:#pragma: no cover
#         return JsonResponse({"error":err})


# #api for book details creation
# @csrf_exempt
# def add_BookDetails(request):

#     try:
#         body = loads(request.body)
        
#         book_details = body["book_details"]
#         book_insert_data=[]
#         for i in book_details:
#             book_insert_data.append(
#                 Books(
#                     book_title=i["book_title"],
#                     book_author=i["book_author"],
#                     book_category=i["book_category"],
#                     description=i["description"],
#                     book_quantity=i["book_quantity"],
#                     book_cost=i["book_cost"]
#                 ))

#         Books.objects.bulk_create(book_insert_data)

#         return JsonResponse({"data":"Book Details Created"})
#     except Exception as err:#pragma: no cover
        
#         return JsonResponse({"error":err})


# #api for getting book details
# @csrf_exempt
# def get_BookDetails(request):
#     try:
#         res = list(Books.objects.all().values())

#         return JsonResponse({"data":res})
#     except Exception as err:#pragma: no cover
#         return JsonResponse({"error":err})

# #api for inserting User
# @csrf_exempt
# def add_User(request):
#     try:
#         body=loads(request.body)

#         user_name = body["user_name"]
#         password = encrypt_string(body["password"])

#         User_Details.objects.create(
#                            user_name=user_name,
#                            password=password,
#                            user_favourite_categorys=body["user_choices"])
      
#         return JsonResponse({"data":"User Created"})
#     except Exception as err:
#         print("value of err",err)
#         return JsonResponse({"data":"User Creation Failed"})

# #api for validating User
# @csrf_exempt
# def validate_User(request):
#     try:
#         body=loads(request.body)

#         user_name = body["user_name"]
#         password = encrypt_string(body["password"])

#         result = User_Details.objects.get(user_name=user_name)

#         if result.password == password:
#             return JsonResponse({"data":"Login Succes"})
#         else:
#             return JsonResponse({"data":"Login Failed"})
        
#     except Exception as err:
#         print("login exception",err)
#         return JsonResponse({"data":"User Authentication Failed"})
