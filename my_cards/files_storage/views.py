from django.shortcuts import render
from django.views.generic import View, ListView

from files_storage.models import File
from files_storage.services import DropboxServices
from tools.mixins import MessageMixin


class FilesListView(ListView):
    template_name = 'files_storage/files_list.html'
    context_object_name = 'files'

    def get_queryset(self):
        files = File.objects.filter(owner=self.request.user.id)
        return files

class UploadFileView(View, MessageMixin):
    template_name = 'files_storage/upload_file.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        file = request.FILES.get('file')

        old_name, new_name = DropboxServices.upload_file(request=request, file=file)


        return render(request, self.message_template, context={'message': f'File "{old_name}" saved to the dropbox as "{new_name}"'})