from pet_search.models import Dog, Cat
from rest_framework import serializers


class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'breed', 'collar')


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('name', 'color')