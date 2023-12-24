import os
from datetime import datetime

from django.shortcuts import render
from django.views import View

import subprocess
import re

from tools.mixins import MessageMixin
from tube.models import Videos
from tube.services.video_services import VideoServices

class VideoCollectionsListView(View):
    template_name = 'tube/video_list.html'
    def get(self, request):
        collections = Videos.objects.filter(owner=request.user.id)
        return render(request, self.template_name, context={'collections': collections})
    
class UploadVideoView(View, MessageMixin):
    
    ABSOLUTE_UPLOAD_URL = 'media/videos/'
    OUTPUT_FILENAME = "%(title)s.%(ext)s"
    template_name = 'tube/upload_video.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):

        url = request.POST.get('yt_url').split('&')[0]
        result = VideoServices.download_and_create_video(ABSOLUTE_UPLOAD_URL=self.ABSOLUTE_UPLOAD_URL,
                                                        OUTPUT_FILENAME=self.OUTPUT_FILENAME,
                                                        url=url,
                                                        user=request.user)
        

        return render(request, self.message_template, context={'message': result})

class WatchVideoView(View):
    template_name = 'tube/watch.html'
    def get(self, request, video_id):
        video = Videos.objects.get(id=video_id)
        video_path = video.video_path
        video_subs = video.video_subs

        return render(request, self.template_name, context={'video_path': video_path,
                                                            'video_subs': video_subs})