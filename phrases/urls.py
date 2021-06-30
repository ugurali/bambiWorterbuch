from rest_framework import routers
from django.conf.urls import url
from django.urls import include

from phrases.views import VerbViewSet, NounViewSet

router = routers.DefaultRouter()
router.register(r'verbs', VerbViewSet, basename="verb")
router.register(r'nouns', NounViewSet, basename="noun")

urlpatterns = [
    url('', include(router.urls)),
]