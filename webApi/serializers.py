from rest_framework import serializers
from.models import *
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['lname', 'address']


class FamilyMemberSer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = FamilyMember
        exclude= ['id', 'created_at', 'updated_at', 'user']
    
    