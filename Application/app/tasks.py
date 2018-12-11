# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import carmewrapper

@shared_task
def new(projectid):
    carmewrapper.new(projectid)
    carmewrapper.setStatus(projectid, "State", "New")
    carmewrapper.setStatus(projectid, "IP", "NONE")

@shared_task
def configAll(projectid, config):
    carmewrapper.configAll(projectid,config)
    carmewrapper.setStatus(projectid, "State", "Configured")
    carmewrapper.setStatus(projectid, "Task", "Idle")

@shared_task
def config(projectid, config, filename):
    carmewrapper.config(projectid,config, filename)
    carmewrapper.setStatus(projectid, "State", "Configured")
    carmewrapper.setStatus(projectid, "Task", "Idle")

@shared_task
def setup(projectid):
    carmewrapper.setStatus(projectid, "Cluster", "Creating")
    result = carmewrapper.createCluster(projectid)
    carmewrapper.setStatus(projectid, "Cluster", "Created")
    carmewrapper.setStatus(projectid, "Jupyter", "Installing")
    result += carmewrapper.installJupyter(projectid)
    carmewrapper.setStatus(projectid, "Jupyter", "Installed")
    carmewrapper.setStatus(projectid, "Task", "Idle")
    carmewrapper.setStatus(projectid, "State", "Started")

@shared_task
def delete(projectid):
    carmewrapper.setStatus(projectid, "State", "Deleted")
    carmewrapper.cleanUp(projectid)