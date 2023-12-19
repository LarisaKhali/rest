from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from .views import BookView, AuthorView

router = DefaultRouter()
router.register(r'books', BookView)
router.register(r'authors', AuthorView)

urlpatterns = [
   path('', include(router.urls)),
   path('test/', include('rest_framework.urls', namespace='auth'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)