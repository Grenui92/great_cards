from django.shortcuts import render
from django.views import View


from tools.mixins import MessageMixin
from tools.decorators import class_login_required
from tube.models import Videos
from tube.tasks import download_and_create_video


class VideoCollectionsListView(View):
    """A class-based view for handling the video collections.

    The class has the following att ributes:
    
    - template_name (str): The name of the template to be rendered.
    """

    template_name = 'tube/video_list.html'

    @class_login_required
    def get(self, request):
        """Return the video collections page. Get all videos from the database
        and render the video collections page with the videos.

        :param request: request object
        :return: render
        """
        collections = Videos.objects.filter(owner=request.user.id)
        return render(request,
                      self.template_name,
                      context={'collections': collections})


class UploadVideoView(View, MessageMixin):
    """A class-based view for handling the uploading of videos.

    The class has the following attributes:
    
    - ABSOLUTE_UPLOAD_URL (str): The absolute path to the upload directory.
    - OUTPUT_FILENAME (str): The name of the output file.
    - template_name (str): The name of the template to be
    """

    ABSOLUTE_UPLOAD_URL = 'media/videos/'
    OUTPUT_FILENAME = "%(title)s.%(ext)s"
    template_name = 'tube/upload_video.html'

    @class_login_required
    def get(self, request):
        """Return the upload video page.

        :param request: request object
        :return: render
        """
        return render(request, self.template_name)

    @class_login_required
    def post(self, request):
        """Download the video from the given URL and create a new video in the
        database.

        :param request: request object
        :return: render
        """
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
    """A class-based view for handling the watching of videos.

    The class has the following attributes:
    
    - template_name (str): The name of the template to be rendered.
    """

    template_name = 'tube/watch.html'

    @class_login_required
    def get(self, request, video_id):
        """Return the watch video page.

        :param request: request object
        :param video_id: Video id
        :return: render
        """
        video = Videos.objects.get(id=video_id)
        video_subs = video.video_subs
        yt_id = video.yt_id
        return render(request,
                      self.template_name,
                      context={'video_subs': video_subs,
                               'yt_id': yt_id})
