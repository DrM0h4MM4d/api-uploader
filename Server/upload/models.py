from django.db import models
from django.conf import settings
from .validators import upload_file_path, upload_file_validator

User = settings.AUTH_USER_MODEL

# Create your models here.
class Uploader(models.Model):
    title = models.CharField(max_length=500)
    file_code = models.CharField(max_length=11000)
    file_upload = models.FileField(upload_to=upload_file_path, validators=[upload_file_validator])
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploads')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return self.file_code

    def get_sender_username(self) -> str:
        return self.sender

    def get_file_upload_code(self) -> str:
        return self.file_code
