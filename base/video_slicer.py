from moviepy.editor import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import datetime
from .models import VideoSegment



def split_video(obj,media):
    print(obj)
    print('video splited')
    video = VideoFileClip(obj.video.path,obj.media_name)
    
    video_duration = datetime.timedelta(seconds=video.duration)
    video_size = video.size
    time_slice = datetime.timedelta(seconds=30)
    fa = FileSystemStorage()
    print(video_duration,"duration")
    print(time_slice,"time_slice")
    print(video_size)
    if video_duration < datetime.timedelta(seconds=3*60) and video_size[0] < 51200:
        if video_duration<=time_slice:
            try:
                video_segment = VideoSegment.objects.create(
                    video = obj,
                    segment_name = 'clip_1',
                    video_segment = media
                )
            except:
                print('somthing went wrong')
                pass

        elif video_duration >= time_slice:
            
            count = 1
            rem = int(video.duration)%30
            root = os.path.join(settings.MEDIA_ROOT)+"media/segment/"
            
            for i in range(0,int(video.duration)//30):
                start = i*30
                end = (i+1)*30
                print(start,"  ",end)
                clips = video.subclip(start, end).write_videofile(root+"clip_%d.mp4" % count)
                
                video_segment = VideoSegment.objects.create(
                    video = obj,
                    segment_name = 'clip_%d'% count,
                )
                video_segment.video_segment=os.path.join('media/segment/', "clip_%d.mp4" % count)
                video_segment.save()
                count += 1
            
            if rem > 0:
                clips = video.subclip(end, end+rem).write_videofile(root+"clip_%d.mp4" % count)
                video_segment = VideoSegment.objects.create(
                    video = obj,
                    segment_name = 'clip_%d'% count,
                )
                video_segment.video_segment=os.path.join('media/segment/', "clip_%d.mp4" % count)
                video_segment.save()
            print(count)
        
        return True

    
    return False