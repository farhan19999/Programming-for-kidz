from django.contrib import admin
from .models import ReadingMaterial


# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ("contentId", "sectionId", "contentTopic",)


admin.site.register(ReadingMaterial, MaterialAdmin)
