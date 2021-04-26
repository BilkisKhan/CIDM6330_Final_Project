# Test Driven Development for Python architecture
This repository contains test-Driven Development approach for  Python architecture.  

This project is about online Learning Management System, where User can register themselves as member and can take Courses and record their Progress after taking assessments at the end of the Course. 

Project contains following Python architecture pattern:

1. Repository pattern
2. Domain Model 
3. Unit of Work Pattern 
4. Event and Message Bus


Repository created based on TTD approach utilizing Python Archrtrcture :
Add User
Edit User profile
Delete User profile


##  Requirements

This tutorial utilizes the following requirements:

1. Python v3.9.0
2. Flask v1.1.2
3. tenacity v7.0.0
4. SQLAlchemy v1.4.1
5. pytest v6.2.2




### Project Setup

# Download Python
Before beginning make sure you have the latest version of Python 3.9 installed, which you can download from http://www.python.org/download/.


# Create a new directory for new project:

mkdir Final_Project
cd Final_Project

# Create an environment(optional)
python3.9 -m venv .venv
source .venv/bin/activate

# Install Flask with pip:
pip install Flask

# Install pytest
pip install pytest 

# Install sqlalchemy
pip install sqlalchemy


### Run tests
pytest tests/unit
pytest tests/integration
