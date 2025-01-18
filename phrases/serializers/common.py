from rest_framework import serializers
from ..models import *

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ("__all__")

class PhraseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Phrase
    fields = ("__all__")
