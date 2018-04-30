import logging
import time
from threading import Thread
from crontab import CronTab
from .api import ApiDocker

LOGGER = logging.getLogger(__name__)

class Job(Thread):
    """Job class"""
    def __init__(self, _job, _cron, _container = None):
        Thread.__init__(self)
        self.cron = CronTab(_cron)
        self.container = _container
        self.job = _job
        self.daemon = True

    def can_start(self):
        next_exec_delay = int(self.cron.next(default_utc=True))
        LOGGER.debug('Delay %s sec on %s before exec "%s"', next_exec_delay,
                     self.container, self.job)
        if next_exec_delay == 0:
            return True
        return False

    def run(self):
        while True:
            if self.can_start():
                LOGGER.debug('Start job %s', self.job)
                docker = ApiDocker()
                docker_id = docker.get_container_id(self.container)
                if docker_id is not None:
                    LOGGER.info("JOB | RESULT | %s", docker.exec_command(docker_id, self.job))
                else:
                    LOGGER.warn('Cannot find container named "%s"', self.container)
                LOGGER.info('JOB | FINISH | %s | %s', self.container, self.job)
            time.sleep(1)
