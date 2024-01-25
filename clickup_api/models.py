from datetime import datetime

from sqlalchemy import String, TIMESTAMP, Integer
from sqlalchemy.orm import Mapped, mapped_column

from common.models import DefaultBase


class Task(DefaultBase):
    task_autoid: Mapped[int] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    clickup_id: Mapped[int] = mapped_column(Integer, default=0)
