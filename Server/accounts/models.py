from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

JOBS = (
    ('System Administrator', 1),
    ('Gamer', 2),
    ('Developer', 3),
    ('Graphist', 4),
    ('Other', 5),
)

REGIONS = (
    ('MiddleEast', 1),
    ('Europe', 2),
    ('North America', 3),
    ('South America', 4),
    ('Canada', 5),
    ('India', 6),
    ('Chineese', 7),
    ('Japaneese', 8),
    ('Russia', 9),

)

# Create your models here.
class Users(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/profiles/', null=True, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    why_using = models.CharField(max_length=500, null=True, blank=True)
    job = models.CharField(choices=JOBS, max_length=50)
    region = models.CharField(choices=REGIONS, max_length=50)

    def get_total_files_uploaded(self):
        return self.uploads.count()

    def get_file_uploaded(self, code: int) -> Model:
        if code:
            for file in self.uploads.all():
                if code == file.code:
                    return file

    def get_all_files_uploaded(self) -> list:
        return [file for file in self.uploads.all()]
