from django.db import models
from rest_framework import serializers
# from django.contrib.postgres.fields.jsonb import JSONField

# Create your models here.
class Books(models.Model):
    
    # book_id = models.AutoField(primary_key=True)
    book_title = serializers.CharField(max_length=150)
    book_author = serializers.CharField(max_length=50)

    book_category = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)

    book_quantity = serializers.IntegerField()

    book_cost = serializers.FloatField()

    def __str__(self):
        return self.book_title


class User_Details(models.Model):
    # user_id = models.AutoField(primary_key=True)
    user_name = serializers.CharField(max_length=100) 
    password = serializers.CharField(max_length=200)

    user_favourite_categorys = serializers.JSONField()

    def __str__(self):
        return self.user_name


class Category(models.Model):
    # category_id = models.AutoField(primary_key=True)
    category_name = serializers.CharField(max_length=150)


    def __str__(self):
        return self.category_name
