# from django.shortcuts import render
# from book_store.models import User_Details
# from json import loads
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from book_store.Encryption_Service import encrypt_string
# # Create your views here.

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
