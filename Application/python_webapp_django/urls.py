"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
import app.api.projects

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.dashboard, name='dashboard'),
    url(r'^api/projects$', app.api.projects.projects, name='apiProjectsProject'), #adds url for new command 
    url(r'^api/projects/(?P<projectid>[0-9a-f-]+)$', app.api.projects.project, name='apiProjectsProjects'), #adds url for new command 
    url(r'^api/projects/(?P<projectid>[0-9a-f-]+)/setup$', app.api.projects.setup, name='apiProjectsProjectsSetup'), #adds url for install command 
    url(r'^projects/(?P<projectid>[0-9a-f-]+)$', app.views.project, name='project'), #adds url for new command 
    url(r'^projects/(?P<projectid>[0-9a-f-]+)/setup$', app.views.setup, name='projectSetup'), #adds url for install command 
    url(r'^projects/(?P<projectid>[0-9a-f-]+)/delete$', app.views.delete, name='projectDelete'), #adds url for delete command 
    url(r'^chatbot', app.views.chatbot, name='chatbot'),
    url(r'^form', app.views.form, name='form'),
    url(r'^login/$',
        django.contrib.auth.views.LoginView,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.LogoutView,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
