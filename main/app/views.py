from django.shortcuts import render
from .tasks import spam_message


def index(request):
    # spam_message('alexryzhak238@gmail.com')
    return render(request, 'main/index.html')
