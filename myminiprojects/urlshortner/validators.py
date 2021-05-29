from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False
    try:
        url_validator(value)
    except:
        value_1_invalid = True
    value_2_url = "http://" + value
    try:
        url_validator(value_2_url)
    except:
        value_1_invalid = True

    if value_1_invalid ==False or value_2_invalid == False:
        raise ValidationError("Invalid Url Entered..please cheack it once more")
    return value