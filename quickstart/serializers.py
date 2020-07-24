from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerialier(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ['url', 'username','email', 'groups']
    
class GroupSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
