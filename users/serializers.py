from django.contrib.auth import get_user_model
from rest_framework import serializers
import django.contrib.auth.password_validation as validations
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from phrases.serializers.common import * 

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match."})
        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data
    
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)
        return User.objects.create(**validated_data) 
# the ** unpacks the validated_data dictionary into keyword arguments

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'target_language', 'character')

class PopulatedUserSerializer(PublicUserSerializer):
    locations = PopulatedUserLocationSerializer(source='userlocation_set', many=True)

    class Meta(PublicUserSerializer.Meta):
        fields = PublicUserSerializer.Meta.fields + ('locations',)
