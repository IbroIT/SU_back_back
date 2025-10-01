from rest_framework import serializers
from .models import Event, Club, Project


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 'title', 'title_en', 'title_ky', 
            'description', 'description_en', 'description_ky',
            'date', 'location', 'location_en', 'location_ky',
            'organizer', 'organizer_en', 'organizer_ky',
            'participants', 'category', 'status', 'registration',
            'image', 'color', 'popular', 'social_media_link',
            'created_at', 'updated_at'
        ]


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = [
            'id', 'title', 'title_en', 'title_ky',
            'description', 'description_en', 'description_ky',
            'members', 'meetings', 'meetings_en', 'meetings_ky',
            'leader', 'leader_en', 'leader_ky',
            'achievements', 'achievements_en', 'achievements_ky',
            'category', 'status', 'image', 'color', 'popular',
            'social_media_link', 'created_at', 'updated_at'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'title_en', 'title_ky',
            'description', 'description_en', 'description_ky',
            'team', 'progress', 'needs', 'needs_en', 'needs_ky',
            'category', 'status', 'image', 'color', 'popular',
            'social_media_link', 'created_at', 'updated_at'
        ]