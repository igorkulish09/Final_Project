from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')

app = Celery('api_project')

# Завантаження конфігурації з налаштувань Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматичне визначення завдань із файлів tasks.py всіх зареєстрованих додатків Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
