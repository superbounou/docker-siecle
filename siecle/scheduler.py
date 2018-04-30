"""Class example"""
import re
import time
import logging
import ConfigParser
from crontab import CronTab
from .job import Job

LOGGER = logging.getLogger(__name__)
CONFIG = ConfigParser.ConfigParser()
CONFIG.read("siecle.cfg")

class Scheduler(object):
    """CLI class"""
    def __init__(self, _crontab = None):
        """CLI constructor"""
        self.jobs = []
        if _crontab is not None:
            self.set_crontab(_crontab)
        else:
            self.set_crontab(CONFIG.get('cron','crontab'))

    def start(self):
        """
        Run the scheduler
        """
        while True:
            for job in self.jobs:
                job.run()
            time.sleep(1)

    def set_crontab(self, path):
        """
        Parse crontab file and extract job
        """
        lines = [line.rstrip('\n') for line in open(path)]
        for line in lines:
            # extract frequency
            items = re.split(r' +|\t*', line)
            frequency = items[0:5]
            frequency = " ".join(frequency)
            # avoid if it's a comment$
            if re.match(r'^#.*', frequency) is None and len(items) > 1:
                command, container = " ".join(items[6:]), items[5]
                LOGGER.info('JOB | CREATE | %s | %s | %s', frequency, command, container)
                self.jobs.append(Job(command, frequency, container))
