from django.core.exceptions import ValidationError

def validate_title(value):
    if "bangladesh" not in value.lower():
        raise ValidationError(
            "Title must contain the word 'Bangladesh'."
        )
    return value