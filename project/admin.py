from django.contrib import admin
from .models import ReadingMaterial, Course, Mcq


# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ("contentId", "sectionId", "contentTopic",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_level", "short_description")

class McqAdmin(admin.ModelAdmin):
    list_display = ("course", "question", "right_option", "wrong_option1", "wrong_option2", "wrong_option3")

admin.site.register(ReadingMaterial, MaterialAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Mcq, McqAdmin)
