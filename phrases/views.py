from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import * 
from .serializers.common import * 

# ! LOCATIONS
# GET ALL LOCATIONS/ CREATE LOCATION
class LocationList(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# GET LOCATION BY ID
class LocationById(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# UPDATE OR DELETE LOCATION
class LocationUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# ! PHRASES
class PhraseList(ListCreateAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

class PhraseById(RetrieveAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

class PhraseUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

class getPhraseByLocation(ListCreateAPIView):
    serializer_class = PhraseSerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Phrase.objects.filter(location_id=location_id) 
