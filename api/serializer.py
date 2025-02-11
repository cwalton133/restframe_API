from rest_framework import serializers
from . models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name,', 'email',
               'phone_number', 'mobile_number', 'photo']
        read_only_fields = ['id', 'created_at']
