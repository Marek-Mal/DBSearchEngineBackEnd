from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import wartsila_engine, spare_parts
from .serializers import engine_serializer, parts_serializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
import base64

# Create your views here.


class GET_wartsila_engine(generics.ListAPIView):
    queryset = wartsila_engine.objects.all()
    serializer_class = engine_serializer
    permission_classes = []
    http_method_names = ["get"]
    

class GET_spare_parts(generics.ListAPIView):
    queryset = spare_parts.objects.all()
    serializer_class = parts_serializer
    permission_classes = []
    http_method_names = ["get"]

class GET_spare_parts_filter(generics.ListAPIView):
    queryset = spare_parts.objects.all()
    serializer_class = parts_serializer
    permission_classes = []
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        if kwargs.get('id').startswith('D '):
            part_id = kwargs.get('id')
            if part_id:
                queryset = spare_parts.objects.filter(part_id=part_id)
                json = parts_serializer(queryset, many=True).data
                return Response(json)
            return Response({"error": "ID parameter is missing"}, status=400)
        else:
            part_name = kwargs.get('id')
            if part_name:
                queryset = spare_parts.objects.filter(part_name=part_name)
                json = parts_serializer(queryset, many=True).data
                return Response(json)
            return Response({"error": "ID parameter is missing"}, status=400)

class GET_spare_parts_filter_by_engineID(generics.ListAPIView):
    queryset = spare_parts.objects.all()
    serializer_class = parts_serializer
    permission_classes = []
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        # print('*'*30)
        # print(kwargs)
        coded_id = kwargs.get('component_id')
        engine_id = base64.urlsafe_b64decode(coded_id.encode()).decode()
        if engine_id[0].isdigit():
            if engine_id:
                queryset = spare_parts.objects.filter(component_id=engine_id)
                # queryset2 = wartsila_engine.objects.filter(id=engine_id)
                json = parts_serializer(queryset, many=True).data
                return Response(json)
            return Response({"error": "ID parameter is missing"}, status=400)
        else:
            component_name = engine_id
            if component_name:
                queryset = wartsila_engine.objects.filter(component_name=component_name)
                json = engine_serializer(queryset, many=True).data
                return Response(json)
            return Response({"error": "ID parameter is missing"}, status=400)

class GET_wartsila_engine_filter(generics.ListAPIView):
    queryset = wartsila_engine.objects.all()
    serializer_class = engine_serializer
    permission_classes = []
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        coded_id = kwargs.get('encoded_id')
        new_id = base64.urlsafe_b64decode(coded_id.encode()).decode().replace('-', '–')
        if new_id[0].isdigit():
            component_id = new_id
            if component_id:
                queryset = wartsila_engine.objects.filter(id=component_id)
                json = engine_serializer(queryset, many=True).data
                return Response(json)
            return Response({"error": "ID parameter is missing"}, status=400)
        else:
            component_name = kwargs.get('id')
            if component_name:
                queryset = wartsila_engine.objects.filter(component_name=component_name)
                json = engine_serializer(queryset, many=True).data
                return Response(json)
            return Response({"error": "ID parameter is missing"}, status=400)