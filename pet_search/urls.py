from django.conf.urls import url, include
from rest_framework import routers
from pet_search import views

router = routers.DefaultRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'cats', views.CatViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]