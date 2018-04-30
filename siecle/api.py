import docker
import ConfigParser
from crontab import CronTab

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("siecle.cfg")

class ApiDocker(object):

    def __init__(self, _socket = ''):
        if _socket == '':
            self.socket = CONFIG.get('docker','socket')
        else:
            self.socket = _socket
        self.client = docker.APIClient(self.socket)

    def list_containers(self):
        """
        List container like docker ps command
        """
        print "CONTAINER ID\t\tIMAGE\t\t\tCOMMAND"
        for container in self.client.containers():
            print container['Id'][:12] + "\t\t" + container['Image'] + "\t\t" + container['Command']

    def get_container_id(self, name):
        for container in self.client.containers():
            if container['Names'][0][1:] == name:
                return container['Id']
        return None

    def exec_command(self, container_id, command):
        ex = self.client.exec_create(container_id, command)
        return self.client.exec_start(ex.get("Id"))
