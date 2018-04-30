"""Class example"""
import re
import ConfigParser
from crontab import CronTab

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("siecle.cfg")

class Scheduler(object):
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.jobs = []

    def parse_crontab(self, path):
        """
        Parse crontab file and extract frequency
        """
        file = open(path, "r")
        for line in file.readlines():
            # extract frequency
            line = line.split(' ')
            frequency = line[0:5]
            frequency = " ".join(frequency)
            # avoid if it's a comment
            if re.match(r'^#.*', frequency) is None:
                entry = CronTab(frequency)
                print(int(entry.next(default_utc=False)))
