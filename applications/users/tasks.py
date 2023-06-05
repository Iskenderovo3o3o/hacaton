from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def send_activation_code(user_id):
    user = User.objects.get(id=user_id)

    message = f"""
    Спасибо за регистрацию! Ваш код активации {user.activation_code}
    """
    send_mail(
        subject='Активация ',
        message=message, 
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )

