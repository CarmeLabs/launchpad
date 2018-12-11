"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

import carmewrapper
import uuid

import app.tasks


def dashboard(request):
    """Renders the dashboard page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dashboard.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def chatbot(request):
    """Renders the Carme chat bot page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/chatbot.html',
        {
            'title':'New Chatbot',
            'year':datetime.now().year,
        }
    )

def form(request):
    """Renders the Carme form setup page."""
    assert isinstance(request, HttpRequest)
    
    """If it was a post then set the make the project and go to the page"""
    if request.method == "POST":
        projectid = str(uuid.uuid4())
        app.tasks.new(projectid)
        carmewrapper.setStatus(projectid, "Task", "Config")
        app.tasks.configAll(projectid, request.POST)
        return redirect("project", projectid)
    else:
        return render(
            request,
            'app/form.html',
            {
                'title':'New Form',
                'year':datetime.now().year,
            }
        )

def project(request, projectid):
    """Renders the Carme form setup page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/project.html',
        {
            'title':'Project ' + projectid,
            'year':datetime.now().year,
            'project' : carmewrapper.getProjectDetails(projectid)
        }
    )

def setup(request, projectid):
    """Renders the Carme form setup page."""
    assert isinstance(request, HttpRequest)
    app.tasks.setup.delay(projectid)
    return redirect("project", projectid)

def delete(request, projectid):
    """Renders the Carme form setup page."""
    assert isinstance(request, HttpRequest)
    app.tasks.delete.delay(projectid)
    return redirect("project", projectid)
