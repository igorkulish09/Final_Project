from celery import shared_task

@shared_task
def sync_books():
    return "Синхронізація книг завершена."