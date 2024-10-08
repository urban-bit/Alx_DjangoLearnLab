from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'bio', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Create a new user instance
        user = User(
            username=validated_data['username'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', '')
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the user instance
        
        # Create a token for the user
        Token.objects.create(user=user)  
        
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
