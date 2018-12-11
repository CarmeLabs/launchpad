# ITWS MITR Team 6

## Description

A Django website for setting up data science environments using Carme.

## Features

* Carme Python wrapper
* Editing configuration files
* Background task processing with Celery and Redis
* Hosting on Azure

## Contributors

This project was built by Team 6 in the Fall 2018 MITR class at RPI.

## Setup

1. Install Python 3.7.X and PIP
2. run `pip install -r requirements-carme.txt`
  * This installs the requirements for the Carme project
3. run `pip install -r requirements.txt`
  * This will install Carme and requirements for this project
4. Open the Application folder in Visual Studio Code or another IDE

## Running

* To run the website: `python manage.py runserver`
* To run the background worker: `celery worker -A python_webapp_django --pool=solo`

## Hosting

* Any code that is checked in to the Git repository is automatically built and deployed to the ITWS_Capstone resource group on Azure. 
  * carmeonline - The main Linux web site host
  * carmebot - The chatbot implementation and IDE
  * VstsResourceGroup-carme - Resource group for continuous integration and delivery, Git