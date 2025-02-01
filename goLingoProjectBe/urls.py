"""
URL configuration for goLingoProjectBe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phrases.views import *
from users.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', LocationList.as_view()),
    path('location/<int:pk>/', LocationById.as_view()),
    path('locations/<int:pk>/', LocationUpdateDestroy.as_view()),
    path('phrases/', PhraseList.as_view()),
    path('phrase/<int:pk>/', PhraseById.as_view()),
    path('phrases/<int:pk>/', PhraseUpdateDestroy.as_view()),
    path('user-location/', UserLocationList.as_view()),
    path('location-phrases/<str:location_name>/', getPhraseByLocation.as_view()),
    path('get_locations_by_coordinates/', get_locations_by_coordinates),
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/', CredentialsView.as_view())
]
