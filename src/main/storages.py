from django.core.files.storage import FileSystemStorage


class PostersStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = './media/posters/'
        kwargs['base_url'] = '/media/'
        super().__init__(*args, **kwargs)

class PDFStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('location', './media/pdf')
        kwargs.setdefault('base_url', '/media/pdf')
        super().__init__(*args, **kwargs)