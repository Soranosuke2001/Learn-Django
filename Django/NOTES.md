# Django Project File Tree Explanation

This section explains what each file does once the Django project is created by using the following command:

Note: Create a Virtual Env and install Django before running the following command.

```bash
django-admin startproject first_project
```

## `__init__.py` File

This is a blank Python file. This file is required in order to let Python know that this directory can be treated as a package.

## `settings.py` File

This file will contain all the necessary settings for the project.

## `urls.py` File

This file will contain all the necessary URL patterns for the project. Basically the different pages that the application will have.

## `wsgi.py` File

This is a Python script that will act as our Web Server Gateway Interface. This will be required later on when we want to deploy the application to production.

## `manage.py` File

We will be touching this file a lot since it will be associated with many commands as we build our web app.

# Running Django

In order to run the Django application, use the following command:

```bash
python manage.py runserver
```

Using the above command will run the Django application on port 8000.

# Creating the First Django Application

A Django **application** is different from a Django **project**.

In order to create a simple application, use the following command:

Note: The `<application-name>` as it suggests will be the name of the application you are going to create.

```bash
python manage.py startapp <application-name>
```

## Django Project

A Django project will have a collection of Django applications and configurations. Once these are combined together, it makes up the entire web application.

## Django Application

A Django application is just a component of the Django project. It will perform a certain functionality for the entire web application.

Note: These Django applications can be incorporated into other Django projects.

### Example

1. Registration App
2. Polling App
3. Comments App
4. etc.

# Django Application File Tree Explanation

This section explains what each file does once a Django application is created using the following command:

```bash
python manage.py startapp <application-name>
```

## `__init__.py` File

This file acts exactly the same as the `__init__.py` file in the Django project directory. Its a special name to let Python know that this directory can be treated as a package.

## `admin.py` File

This file will allow you to register models. Once registered, Django will then use them with Django's admin interface.

## `apps.py` File

This file will store configurations that is specific to the application only.

## `models.py` File

This file will store the application's data models. In other words, specifying the entities and relationships between the data.

## `tests.py` File

This file is used to create test cases (functions) to test the code for the application.

## `views.py` File

This file will contain functions that will handle requests and return responses.
