from django.core.mail import send_mail

def send(user_email):
    send_mail(
        f"Some Spam from DjSports",
        f"this is spam",
        'ryzhakovalexeynicol@gmail.com',
        [user_email],
        fail_silently=False
    )
