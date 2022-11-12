from rest_framework import serializers

from .models import Videos,VideoSegment

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('id','media_name','slug','video','created_at','updated_at')


class VideoSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSegment
        fields = ('id','segment_name','video_segment','video')
