from django.urls import path
from base.views import VideoAPIView
urlpatterns = [
   path('upload-video/',VideoAPIView.as_view(),name='upload-video-view'),
]