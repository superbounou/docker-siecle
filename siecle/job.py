from crontab import CronTab

class Job(object):
    """Job class"""
    def __init__(self, _job, _cron, _container = None):
        self.cron = CronTab(_cron)
        self.container = _container
        self.job = _job

    def run(self):
        next_exec_delay = int(self.cron.next(default_utc=True))
        if next_exec_delay == 0:
            self.exec_job()

    def exec_job(self):
        print self.job
