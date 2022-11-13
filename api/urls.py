from django.urls import path
from base.views import VideoAPIView,VideoSegmentAPIView
urlpatterns = [
   path('upload-video/',VideoAPIView.as_view(),name='upload-video-view'),
   path('video/',VideoSegmentAPIView.as_view(),name='video-view'),
]