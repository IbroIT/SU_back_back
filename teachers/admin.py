from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Teacher, Management

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name_ru', 'position_ru')
    search_fields = ('full_name_ru', 'position_ru')

admin.site.register(Management, MPTTModelAdmin)
