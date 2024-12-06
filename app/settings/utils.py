from celery import shared_task
from django.core.mail import send_mail
from .models import Form

@shared_task
def send_contact_email(name, email, message):
    Form.objects.create(name=name, email=email, message=message)