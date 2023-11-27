from rest_framework import routers
from .api import PostulanteViewSet

router = routers.DefaultRouter()

router.register('api/postulante',PostulanteViewSet, 'postulante')

urlpatterns = router.urls
