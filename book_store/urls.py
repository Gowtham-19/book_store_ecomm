from django.contrib import admin
from django.urls import path
from book_store import views
from .Views import  book_details_crud
from .Views import user_crud
from .Views import crud

app_name = "book_store"
urlpatterns = [

    #Category Views
    path('createCategory',crud.create_Category,name="create_Category"),
    path("getCategorys",crud.get_Categorys,name="get_Categorys"),
    
    #Book detail Views
    path("add_BookDetails",book_details_crud.add_BookDetails,name="add_BookDetails"),
    path("get_BookDetails",book_details_crud.get_BookDetails,name="get_BookDetails"),
    path("update_BookDetails",book_details_crud.update_BookDetails,name="update_BookDetails"),
    
    #User detail Views
    
    path('add_User',user_crud.add_User,name="add_User"),
    path('get_User',user_crud.validate_User,name="get_User")
]
