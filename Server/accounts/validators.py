from django.core.exceptions import ValidationError
import re

def validate_password(value):
    if not re.match(r'', value):
        raise ValidationError("Password must be ...")