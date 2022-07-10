from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

def validate_stroke(stroke):
    valid_stroke = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in valid_stroke:
        raise ValidationError(f"{stroke} is not a valid stroke")

def min_distance(distance):
    if distance < 50:
        raise ValidationError("Ensure this value is greater than or equal to 50.")

def validate_date(record_date):
    if record_date > timezone.now():
        raise ValidationError("Can't set record in the future.")

def validate_record_date(record_broken_date):
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")