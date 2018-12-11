from django.http import HttpRequest
from django.template import RequestContext
from django.http import JsonResponse

import carmewrapper
import uuid

import app.tasks

def projects(request):
  """Makes a new Carme project."""
  assert isinstance(request, HttpRequest)

  """If it was a post then set the configuration"""
  if request.method == "POST":
    projectid = str(uuid.uuid4())
    app.tasks.new(projectid)
    carmewrapper.setStatus(projectid, "Task", "Config")
    app.tasks.configAll(projectid, request.POST)
    return JsonResponse({'projectid':projectid})
  else:
    return JsonResponse({})

def project(request, projectid):
  """Get or updates a new Carme project."""
  assert isinstance(request, HttpRequest)

  """If it was a post then set the configuration"""
  if request.method == "POST":
    carmewrapper.setStatus(projectid, "Task", "Config")
    app.tasks.configAll(projectid, request.POST)

  return JsonResponse(carmewrapper.getProjectDetails(projectid))

def setup(request, projectid):
  carmewrapper.setStatus(projectid, "Task", "Setup")
  app.tasks.setup.delay(projectid)
  return JsonResponse(carmewrapper.getProjectDetails(projectid))