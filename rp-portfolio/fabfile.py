from fabric.api import *

def deploy():
    # local('sudo docker image build .')
    # local('sudo docker-compose up --build')
    local('ansible-playbook -i hosts.yml playbook.yml')
    local('ansible-playbook -i hosts.yml letsencrypt_playbook.yml')
