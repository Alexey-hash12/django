from main.celery import app
from .service import send


@app.task
def spam_message(user_email):
    send(user_email)
