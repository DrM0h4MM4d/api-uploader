from django.core.exceptions import ValidationError
from os.path import splitext

def upload_file_validator(value):
    valid_extensions = ['.png', '.jpg', '.mp4', '.mpv',
                            '.mvw', '.ico', '.pdf', '.mp3', '.ogg',
                            '.wav', '.avi', '.zip', '.mkv', '.rar',
                            '.mov', 
                        ]
    file_format = splitext(value.name)[1]
    if file_format not in valid_extensions:
        return ValidationError('Sorry dear, This file format is not supported right now!')


def upload_file_path(instance, filename):
    return f"files/{instance.sender.username}/%Y/%m/%d"