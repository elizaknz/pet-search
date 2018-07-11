from django.db import models
from enum import Enum


class Breed(Enum):
    RETRIEVER = 'RETRIEVER'
    SHEPHERD = 'SHEPHERD'
    DACHSHUND = 'DACHSHUND'
    CHIHUAHUA = 'CHIHUAHUA'
    BULLDOG = 'BULLDOG'
    MONGREL = 'MONGREL'


class Color(Enum):
    WHITE = 'WHITE'
    BLACK = 'BLACK'
    MULTICOLOR = 'MULTICOLOR'


class Dog(models.Model):

    name = models.CharField(max_length=70)
    breed = models.CharField(max_length=70, choices=[(tag.value, tag.value) for tag in Breed])
    collar = models.BooleanField()

    def __str__(self):
        return self.name


class Cat(models.Model):

    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70, choices=[(tag.value, tag.value) for tag in Color])

    def __str__(self):
        return self.name
