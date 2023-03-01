from django.core.mail import send_mail
import random
from django.conf import settings
def send_otp(email):
    subject=f"your account verification email is"
    otp=random.randint(1000,9999)
    message='your otp is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])