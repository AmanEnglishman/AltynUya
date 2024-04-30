from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage 
from django.conf import settings


def send_mail(instance):
    to_email = 'altynuya.shk21@gmail.com'
    subject = instance.email
    message = f"{instance.full_name}\n{instance.phone}\n{instance.message}"

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to=[to_email])
    email.send()