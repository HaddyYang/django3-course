import os
from django.http import HttpResponse
from django.conf import settings


def home(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)
    