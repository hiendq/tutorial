from rest_framework import serializers
from snippets.models import Snippet
from .models import User

class SnippetSerializer(serializers.ModelSerializer):
    # owner = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    owner = serializers.StringRelatedField(many=False)
    class Meta:
        model = Snippet
        fields = ['id','title', 'owner', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.ModelSerializer):

    snippets =SnippetSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'full_name', 'snippets']
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],)
        user.set_password(validated_data['password'])
        user.save()

        return user


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password','full_name']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)
        
    


