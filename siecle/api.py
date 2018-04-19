"""Class example"""
import docker
import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("project.cfg")

class ApiDocker(object):
    def list_containers(self):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        for container in client.containers():
            ex = client.exec_create(container['Id'], "ls")
            print(client.exec_start(ex.get("Id")))
