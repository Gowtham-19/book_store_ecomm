from rest_framework import serializers

class Books(serializers.Serializer):
    book_title = serializers.CharField()
    book_author = serializers.CharField()
    book_category = serializers.CharField()

    description = serializers.CharField()

    book_cost = serializers.FloatField()

    book_quantity = serializers.IntegerField()

    class Meta:
        table_name="Books"
        pk="book_title"
        sk=None
        lsi=[]
        gsi=[]