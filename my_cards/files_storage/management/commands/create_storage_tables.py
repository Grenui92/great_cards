"""
This module contains command for create files types and files extensions in FileExtension and FileTypes tables from storageapp
"""
from django.core.management.base import BaseCommand


"""
This module is used to create tables in the database.
"""
from files_storage.models import FileExtension, FileType


def create_tables():
    """
    The create_tables function creates the tables in the database.
    It is called by manage.py when you run python manage.py create_storageapp_tables

    :return: Nothing
    """
    file_types = {'other': 'icons/other.jpeg', 'images': 'icons/image.png', 'videos': 'icons/video.png',
                  'archives': 'icons/archive.png', 'docs': 'icons/docs.png', 'sound': 'icons/audio.png',
                  'applications': 'icons/applications.jpg', 'message': 'icons/message.png'}
    applications = ['.js', '.mjs', '.json', '.webmanifest', '.dot', '.wiz', '.bin', '.a', '.o',
                    '.obj', '.so', '.oda', '.p7c', '.ps', '.ai', '.eps', '.m3u', '.m3u8', '.xlb', '.pot', '.ppa',
                    '.pps',
                    '.pwz', '.wasm', '.bcpio', '.cpio', '.csh', '.dvi', '.gtar',
                    '.hdf', '.h5', '.latex', '.mif', '.cdf', '.nc', '.p12', '.pfx', '.ram', '.pyc', '.pyo', '.sh',
                    '.shar', '.swf', '.sv4cpio', '.sv4crc', '.tcl', '.tex', '.texi', '.texinfo', '.roff', '.t',
                    '.tr', '.man', '.me', '.ms', '.ustar', '.src', '.xsl', '.rdf', '.wsdl', '.xpdl', '.exe',
                    '.msi', '.dll']
    sound = ['.3gp', '.3gpp', '.3g2', '.3gpp2', '.aac', '.adts', '.loas', '.ass', '.au', '.snd', '.mp3', '.mp2',
             '.opus', '.aif', '.aifc', '.aiff', '.ra', ".ogg", ".amr"]
    images = ['.bmp', '.gif', '.ief', '.jpg', '.jpe', '.jpeg', '.heic', '.heif', '.png', '.svg', '.tiff', '.tif',
              '.ico', '.ras', '.pnm', '.pbm', '.pgm', '.ppm', '.rgb', '.xbm', '.xpm', '.xwd']
    message = ['.eml', '.mht', '.mhtml', '.nws']
    docs = ['.css', '.csv', '.html', '.htm', '.txt', '.bat', '.c', '.h', '.ksh', '.pl', '.rtx', '.tsv', '.py', '.etx',
            '.sgm', '.sgml', '.vcf', ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".rtf", ".xml",
            ".ini"]
    videos = ['.mp4', '.mpeg', '.m1v', '.mpa', '.mpe', '.mpg', '.mov', '.qt', '.webm', '.avi', '.movie', '.wav', ".mkv"]
    archives = [".zip", ".tar", ".tgz", ".gz", ".7zip", ".7z", ".iso", ".rar"]
    other = ['unknown']


    for type_name, img in file_types.items():
        inst = FileType.objects.create(name=type_name, img=img)
        if type_name == 'images':
            for ext in images:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'videos':
            for ext in videos:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'archives':
            for ext in archives:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'message':
            for ext in message:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'docs':
            for ext in docs:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'sound':
            for ext in sound:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'applications':
            for ext in applications:
                FileExtension.objects.create(name=ext, type=inst)
        elif type_name == 'other':
            for ext in other:
                FileExtension.objects.create(name=ext, type=inst)

class Command(BaseCommand):
    """
    This class contains command for create files types and files extensions in FileExtension and FileTypes tables from storageapp
    """
    help = 'Command create files types and files extensions in FileExtension and FileTypes tables from storageapp'

    def handle(self, *args, **options):
        """
        The handle function is the entry point for a Django management command.
        It's called by the manage.py script when you run python manage.py &lt;command&gt;
        from your project directory.

        :param self: Represent the instance of the class
        :param args: Pass a variable number of arguments to a function
        :param options: Pass in the options that are passed to the command
        :return: A string that is printed in the console
        """
        create_tables()
