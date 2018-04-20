"""This class manage the CLI interaction"""
import json
import logging
import sys
import ConfigParser
from .api import ApiDocker

LOGGER = logging.getLogger(__name__)
CONFIG = ConfigParser.ConfigParser()

#pylint: disable=invalid-name
class SiecleStage(object): # pylint: disable=too-few-public-methods
    """This class manage CLI interactions"""
    @staticmethod
    def api(): # pylint: disable=invalid-name
        """FOO"""
        api = ApiDocker()
        api.start_crond()


class Cli(object):# pylint: disable=too-few-public-methods
    """CLI class"""
    def __init__(self):
        """CLI constructor"""
        self.docker = SiecleStage()
