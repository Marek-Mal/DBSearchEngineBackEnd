from django.contrib import admin
from .models import spare_parts, wartsila_engine
# Register your models here.

@admin.register(wartsila_engine)
class wartsila_engine(admin.ModelAdmin):
    list_display = [
        "id",
        "component_name",
        "pdf_page",
        "engine",
        "image"
    ]
    list_filter = ('id', 'component_name')
    search_fields = ('id', 'component_name', 'pdf_page')

admin.site.register(spare_parts)


