from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import fields
from rest_framework import serializers

class userSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['url','username','email','group']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']