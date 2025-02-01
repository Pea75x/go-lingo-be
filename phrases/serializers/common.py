from rest_framework import serializers
from ..models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("__all__")

class MiniLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("name",)

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ("__all__")

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = "__all__"

class PopulatedUserLocationSerializer(UserLocationSerializer):
    location = MiniLocationSerializer()

    class Meta:
        model = UserLocation
        fields = ('id', 'location', 'visited_at')

