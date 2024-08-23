from django.urls import path

from tube.views import VideoCollectionsListView, UploadVideoView, WatchVideoView

app_name = 'tube'

urlpatterns = [
    path('video_list/',
         VideoCollectionsListView.as_view(),
         name='video_list'),
    path('upload_video/',
         UploadVideoView.as_view(),
         name='upload_video'),
    path('watch_video/<int:video_id>/',
         WatchVideoView.as_view(),
         name='watch_video')
]
