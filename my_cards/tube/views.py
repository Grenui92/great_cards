from django.shortcuts import render
from django.views import View


from tools.mixins import MessageMixin
from tools.decorators import class_login_required
from tube.models import Videos
from tube.tasks import download_and_create_video


class VideoCollectionsListView(View):
    template_name = 'tube/video_list.html'

    @class_login_required
    def get(self, request):
        collections = Videos.objects.filter(owner=request.user.id)
        return render(request,
                      self.template_name,
                      context={'collections': collections})


class UploadVideoView(View, MessageMixin):

    ABSOLUTE_UPLOAD_URL = 'media/videos/'
    OUTPUT_FILENAME = "%(title)s.%(ext)s"
    template_name = 'tube/upload_video.html'

    @class_login_required
    def get(self, request):
        return render(request, self.template_name)

    @class_login_required
    def post(self, request):

        url = request.POST.get('yt_url').split('&')[0]
        download_and_create_video.delay(ABSOLUTE_UPLOAD_URL=self.ABSOLUTE_UPLOAD_URL,
                                        OUTPUT_FILENAME=self.OUTPUT_FILENAME,
                                        url=url,
                                        user_id=request.user.id)

        message = 'Загрузка видео может занять какое-то время,\
            вы можете пользоваться другими функциями сайта,\
            а видео автоматически появится на странице Tube'
        return render(request,
                      self.message_template,
                      context={'message': message})


class WatchVideoView(View):
    template_name = 'tube/watch.html'

    @class_login_required
    def get(self, request, video_id):
        video = Videos.objects.get(id=video_id)
        video_subs = video.video_subs
        yt_id = video.yt_id
        return render(request,
                      self.template_name,
                      context={'video_subs': video_subs,
                               'yt_id': yt_id})
