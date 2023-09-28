import schedule
import time


class Scheduler:
    def __init__(self) -> None:
        pass

    def add_daily_job(self, func_name) -> None:
        schedule.every(1).days.do(func_name)

    def add_hour_job(self, func_name) -> None:
        schedule.every(1).hour.do(func_name)

    def add_minute_job(self, func_name) -> None:
        schedule.every(1).minute.do(func_name)

    def add_daily_job_at_time_EDT(self, func_name, time_HM: str = "12:00") -> None:
        schedule.every().day.at(time_HM, "America/New_York").do(func_name)

    def get_all_jobs(self):
        return schedule.jobs

    def run():
        """runs the scheduler for ever"""
        while True:
            schedule.run_pending()
            time.sleep(1)
