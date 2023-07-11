from django.urls import path

from files_storage.views import FilesListView, UploadFileView
app_name = 'files_storage'

urlpatterns = [
    path('files_list/', FilesListView.as_view(), name='files_list'),
    path('upload_file/', UploadFileView.as_view(), name='upload_file')
]