from celery import shared_task


@shared_task
def process_order(order_id):
    return f"Замовлення {order_id} опрацьовано."
