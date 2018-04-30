"""Class example"""
import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("siecle.cfg")

class Job(object):
    """CLI class"""
    def __init__(self, _job, _delay = 0, _container = ""):
        self.delay = 0
        self.container = ""
        self.job = ""

    def run(self):
        print "run"
