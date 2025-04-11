import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not re.fullmatch(r'\+?\d{10,15}', value):
        raise ValidationError("Invalid phone number format")