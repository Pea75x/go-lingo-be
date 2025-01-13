from django.db import models
from django.core.exceptions import ValidationError
import json

with open("phrases/data.json") as f:
    CATEGORY_CHOICES = json.load(f)

def validate_categories(value):
	if not all(item in CATEGORY_CHOICES for item in value):
		raise ValidationError("Invalid category in array.")

class Location(models.Model):
	name = models.CharField(max_length=100)
	categories = models.JSONField(default=list, validators=[validate_categories])

	def __str__(self):
		return self.name

class Phrase(models.Model):
	english_phrase = models.CharField(max_length=200)
	spanish_phrase = models.CharField(max_length=200)
	location = models.ForeignKey(Location, related_name='phrases', on_delete=models.CASCADE)

	def __str__(self):
		return self.english_phrase

