from rest_framework import serializers
from .models import Teacher, Management

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ManagementSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Management
        fields = ('id', 'full_name_ru', 'full_name_kg', 'full_name_en', 
                  'position_ru', 'position_kg', 'position_en', 
                  'bio_ru', 'bio_kg', 'bio_en', 'photo', 'parent', 'children')

    def get_children(self, obj):
        children = obj.get_children()
        return ManagementSerializer(children, many=True, context=self.context).data
