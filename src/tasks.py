import time
from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def send_email(user_email: str):
    print(f"[Worker] Start sending mail to {user_email}")
    time.sleep(5)
    print(f"[Worker] End sending mail to {user_email}")
    return f"Sent to {user_email}"