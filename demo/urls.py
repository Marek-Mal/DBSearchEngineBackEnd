from django.urls import path, include, register_converter
from rest_framework import routers
from .views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

class PartIDConverter:
    regex = '[^/]+'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
    
register_converter(PartIDConverter, 'identify')

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # ============ GET METHOD URLS ============

    path('WartsilaEngine/', GET_wartsila_engine.as_view()), 

    path('WartsilaEngineFilter/<identify:encoded_id>', GET_wartsila_engine_filter.as_view()),

    path('SpareParts/', GET_spare_parts.as_view()), 

    path('SparePartsFilter/<str:id>', GET_spare_parts_filter.as_view()), 

    path('SparePartsFilterByEngineID/<str:component_id>', GET_spare_parts_filter_by_engineID.as_view()), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)