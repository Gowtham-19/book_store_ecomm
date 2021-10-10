from django.contrib import admin
from .models import Books,Category,User_Details
# Register your models here.

admin.site.register(Books)
admin.site.register(User_Details)
admin.site.register(Category)