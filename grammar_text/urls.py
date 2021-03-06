# coding: utf-8
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'phrases', views.PhraseViewset, base_name='phrases')
urlpatterns = router.urls
