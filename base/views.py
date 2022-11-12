from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from .models import Videos,VideoSegment
from .serializers import VideoSegmentSerializer
from .video_slicer import split_video

# Create your views here.


class VideoAPIView(APIView):
    def get(self,request):
        
        id = request.data['video']
        try:

            video_seqments = VideoSegment.objects.filter(video__id=id).order_by('segment_name')
            serializer = VideoSegmentSerializer(video_seqments,many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        media = request.FILES['media']
        fs = FileSystemStorage()
        
        try:
            if media.name.endswith('.mp4'):
                video_instance=Videos.objects.create(
                    media_name = media.name,
                    video = media
                )
        except:

            message = {"detail":"something went wrong !"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            res = split_video(video_instance,media)

            if res :
                message = {"message": "SUCCESS"}
                return Response(message)
            else:    
                message = {"video": video_instance.id +  "file is too large"}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
           
        except:

            message = {"detail":"upload mb4 file !"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        