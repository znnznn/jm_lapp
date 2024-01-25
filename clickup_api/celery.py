from celery import Celery
from celery.schedules import crontab

from settings import Default_DB

celery_app = Celery("clickup_api", include=["ebms_api.tasks"])

celery_app.conf.result_backend = "db+postgresql://{}:{}@{}:5432/{}".format(
    Default_DB.DB_USER, Default_DB.DB_PASS, Default_DB.DB_HOST, Default_DB.DB_NAME
)

celery_app.conf.beat_schedule = {
    "Execute-getting-tasks-every-5-minutes": {
        "task": "ebms_api.tasks.get_tasks",
        "schedule": crontab(),
    },
}