from rest_framework import serializers
from .models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'name',
            'basic',
            'episode',
            'appeal',
            'email',
        )
        model = About
