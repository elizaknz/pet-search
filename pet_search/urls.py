from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from pet_search import views

router = routers.DefaultRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'cats', views.CatViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('frontend.urls')),
]