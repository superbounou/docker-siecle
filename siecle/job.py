import logging
from crontab import CronTab
from .api import ApiDocker

LOGGER = logging.getLogger(__name__)

class Job(object):
    """Job class"""
    def __init__(self, _job, _cron, _container = None):
        self.cron = CronTab(_cron)
        self.container = _container
        self.job = _job

    def run(self):
        next_exec_delay = int(self.cron.next(default_utc=True))
        LOGGER.debug('Delay %s sec on %s before exec "%s"', next_exec_delay,
                     self.container, self.job)
        if next_exec_delay == 0:
            self.exec_job()

    def exec_job(self):
        docker = ApiDocker()
        docker_id = docker.get_container_id(self.container)
        if docker_id is not None:
            LOGGER.info(docker.exec_command(docker_id, self.job))
        else:
            LOGGER.warn('Cannot find container named "%s"', self.container)
