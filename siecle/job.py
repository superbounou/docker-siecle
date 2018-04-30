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
        self.docker = ApiDocker()

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
                LOGGER.info('JOB | START | %s | %s', self.container, self.job)
                docker_id = self.docker.get_container_id(self.container)
                if docker_id is not None:
                    start = time.time()
                    LOGGER.info("JOB | RESULT | %s | %s", self.container, self.docker.exec_command(docker_id, self.job))
                    end = time.time()
                else:
                    LOGGER.warn('JOB | ERROR | Cannot find container "%s"', self.container)
                LOGGER.info('JOB | FINISH | %s | %s | %i sec', self.container, self.job, end - start)
            time.sleep(1)
