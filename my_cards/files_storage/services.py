import re

from storages.backends.dropbox import DropBoxStorage
from django.contrib.auth.models import User

from files_storage.models import File, FileExtension
class DropboxServices:
    reg_ex_extension = r'\.[^./\\]+$'
    storage = DropBoxStorage()

    @classmethod
    def upload_file(cls, request, file):
        old_name = file.name
        new_name = cls.storage.save(old_name, file)

        cls.save_fileinfo_db(request, file, old_name, new_name)

        return old_name, new_name

    @classmethod
    def get_file_info(cls, file):
        pass

    @classmethod
    def save_fileinfo_db(cls, request, file, old_name, new_name):
        owner: User = User.objects.get(id=request.user.id)

        try:
            extension = re.findall(cls.reg_ex_extension, file.name)[0]
            extension_inst: FileExtension = FileExtension.objects.get(name=extension)
        except FileExtension.DoesNotExist:
            extension_inst: FileExtension = FileExtension.objects.get(id=1)

        type_inst = extension_inst.type

        File.objects.create(
            owner=owner,
            file_type=type_inst,
            file_extension=extension_inst,
            file_name=old_name,
            dropbox_file_name=new_name
        )
