from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import * 
from .serializers.common import * 
import requests
from django.http import JsonResponse
from dotenv import load_dotenv
import os

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
        location_name = self.kwargs['location_name']
        return Phrase.objects.filter(location__name=location_name) 

def get_locations_by_coordinates(request):
    load_dotenv()

    latitude = request.GET.get('lat')
    longitude = request.GET.get('long')

    if not latitude or not longitude:
        return JsonResponse({'error': 'Latitude and longitude are required.'}, status=400)
    
    foursquare_url = f"{os.getenv('FOUR_SQUARE_ENDPOINT')}?ll={latitude},{longitude}&radius=100"
    headers = {
        'Accept': 'application/json',
        'authorization': os.getenv('FOUR_SQUARE_API_KEY')
    }
    response = requests.get(foursquare_url, headers=headers)

    if response.status_code != 200:
        return JsonResponse({'error': 'Error fetching data from FourSquare API'}, status=500)
    
    foursquare_data = response.json()
    locations = Location.objects.all()

    matching_locations = []
    for item in foursquare_data['results']:
        for category in item.get('categories', []):
            for location in locations:
                if category['name'] in location.categories:
                    matching_locations.append(location.name)

    matching_locations = list(set(matching_locations))

    return JsonResponse({'locations': matching_locations}, status=200)


