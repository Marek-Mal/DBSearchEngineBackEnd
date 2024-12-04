from rest_framework import serializers
from .models import wartsila_engine, spare_parts

class engine_serializer(serializers.ModelSerializer):
    class Meta:
        model = wartsila_engine
        fields = (
            "id",
            "component_name",
            "pdf_page",
            "engine",
            "image"
        )

class parts_serializer(serializers.ModelSerializer):
    class Meta:
        model = spare_parts
        fields = (
            "id",
            "part_id",
            "part_name",
            "pdf_page",
            "price",
            "extras",
            "component_id",
            "isAvalable"
        )
