from rest_framework import serializers
import requests
from rest_framework.exceptions import ValidationError

from cats.models import Cat


class BreedValidationService:
    @staticmethod
    def validate_breed(breed):
        response = requests.get(
            "https://api.thecatapi.com/v1/breeds/search", params={"q": breed}
        )
        if response.status_code != 200:
            raise ValidationError("This breed is not maintains")

        return breed


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]


    @staticmethod
    def validate_breed(self, value):
        if not BreedValidationService.validate_breed(value):
            raise serializers.ValidationError("Invalid cat breed")
        return value