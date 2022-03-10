from datetime import datetime
from app.models import Session


def verify_tatoo_schedule(mark_tatoo_schedule: Session, list_tatoo_schedule: list[Session]) -> bool:
    for tatoo_schedule in list_tatoo_schedule:
        start_db = tatoo_schedule.start
        end_db = tatoo_schedule.end

        pattern = "%d/%m/%Y %H:%M:%S"
        start = datetime.strptime(mark_tatoo_schedule.start, pattern)
        end = datetime.strptime(mark_tatoo_schedule.end, pattern)

        if not(start > start_db and start > end_db or end < start_db and start < end_db):
            return False
    return True
