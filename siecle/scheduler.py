"""Class example"""
import re
import time
import ConfigParser
from crontab import CronTab
from .job import Job

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("siecle.cfg")

class Scheduler(object):
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.jobs = []

    def start(self):
        """
        Run the scheduler
        """
        self.set_crontab('crontab')
        while True:
            for job in self.jobs:
                job.run()
            time.sleep(1)

    def set_crontab(self, path):
        """
        Parse crontab file and extract job
        """
        file = open(path, "r")
        for line in file.readlines():
            # extract frequency
            line = re.split(r' +', line)
            frequency = line[0:5]
            frequency = " ".join(frequency)
            # avoid if it's a comment
            if re.match(r'^#.*', frequency) is None and len(line) > 7:
                self.jobs.append(Job(" ".join(line[6:]), frequency, line[5]))
