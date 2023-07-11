from storages.backends.dropbox import DropBoxStorage

class DropboxServices:
    storage = DropBoxStorage()

    @classmethod
    def upload_file(cls, file):
        file = cls.storage.save(file.name, file)
        return file