

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import DetectionResultViewSet

from django.conf import settings
from django.conf.urls.static import static



router = DefaultRouter()

urlpatterns = [
    path('predict-maladie/', views.PredictMaladie.as_view(), name='predict_maladie'),
    path('detection-results/', DetectionResultViewSet.as_view({'get': 'list', 'post': 'create'}), name='detection-results'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




