from django.contrib import admin
from .models import Event, Club, Project


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'date', 'registration', 'popular', 'social_media_link']
    list_filter = ['category', 'status', 'registration', 'popular', 'date']
    search_fields = ['title', 'title_en', 'title_ky', 'description']
    ordering = ['-date']
    list_editable = ['status', 'registration', 'popular']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'title_en', 'title_ky', 'description', 'description_en', 'description_ky', 'category', 'image', 'color', 'popular')
        }),
        ('Event Details', {
            'fields': ('date', 'location', 'location_en', 'location_ky', 'organizer', 'organizer_en', 'organizer_ky', 'participants')
        }),
        ('Contact & Links', {
            'fields': ('social_media_link',)
        }),
        ('Status', {
            'fields': ('status', 'registration')
        }),
    )


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'members', 'leader', 'popular', 'social_media_link']
    list_filter = ['category', 'status', 'popular']
    search_fields = ['title', 'title_en', 'title_ky', 'description', 'leader']
    ordering = ['title']
    list_editable = ['status', 'popular']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'title_en', 'title_ky', 'description', 'description_en', 'description_ky', 'category', 'image', 'color', 'popular')
        }),
        ('Club Details', {
            'fields': ('members', 'meetings', 'meetings_en', 'meetings_ky', 'leader', 'leader_en', 'leader_ky', 'achievements', 'achievements_en', 'achievements_ky')
        }),
        ('Contact & Links', {
            'fields': ('social_media_link',)
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'team', 'progress', 'popular', 'social_media_link']
    list_filter = ['category', 'status', 'popular']
    search_fields = ['title', 'title_en', 'title_ky', 'description']
    ordering = ['-created_at']
    list_editable = ['status', 'progress', 'popular']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'title_en', 'title_ky', 'description', 'description_en', 'description_ky', 'category', 'image', 'color', 'popular')
        }),
        ('Project Details', {
            'fields': ('team', 'progress', 'needs', 'needs_en', 'needs_ky')
        }),
        ('Contact & Links', {
            'fields': ('social_media_link',)
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )
