# Django Task Manager (Todo App)

A web application built with Django for managing personal tasks, todos, and task status tracking.

## Key Features

* Task Management: Create, read, update, and delete (CRUD) tasks
* Project Organization: Modular Django apps (`todos` and project config)
* Database Integration: SQLite for local storage of tasks and states

## Tech Stack

* Python 3
* Django
* HTML/CSS
* SQLite3

## Getting Started

1. Clone the repository:
   ```bash
   git clone [https://github.com/divarusa/django-todo-app.git](https://github.com/divarusa/django-todo-app.git)
   cd django-todo-app
   Python -m venv venv
   source venv/bin/activate
   pip install django
   python manage.py migrate
   python manage.py runserver
