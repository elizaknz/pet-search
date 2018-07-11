from rest_framework import viewsets
from pet_search.models import Dog, Cat
from pet_search.serializers import DogSerializer, CatSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
