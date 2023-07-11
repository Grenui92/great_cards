from django.shortcuts import render
from django.views.generic import View, ListView

from files_storage.models import File
from files_storage.services import DropboxServices


class FilesListView(ListView):
    template_name = 'files_storage/files_list.html'
    context_object_name = 'files'

    def get_queryset(self):
        files = File.objects.filter(owner=self.request.user.id)
        print(files)
        return files

class UploadFileView(View):
    template_name = 'files_storage/upload_file.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        file = request.FILES.get('file')
        new_name = DropboxServices.upload_file(file=file)
        print(new_name)