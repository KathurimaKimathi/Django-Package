from fabric.api import *

# def runserver():
#    local('python3 manage.py runserver')


def run_fab():
    local('sudo docker image build .')
    local('sudo docker-compose up --build')
    local('ansible-playbook -i hosts.yml playbook.yml')
