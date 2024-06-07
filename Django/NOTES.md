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

# Django Creating Models

In order to setup the database, we first need to create classes in the `models.py` file. Each class will represent a single table.

Once we have created the classes, all we have to do is run the following commands:

1. Migrate the database

```bash
python manage.py migrate
```

2. Register the changes to the application

Note: The `<application-name>` should be replaced to the name of the application.

```bash
python manage.py makemigrations <application-name>
```

3. Migrate the database once again

```bash
python manage.py migrate
```

# Testing Models

Once the commands above were successfully completed, we can then test to see if the migration was successful by using some dummy data.

1. Open the Django interactive shell

```bash
python manage.py shell
```

2. In the shell, import the class to test

```python
from <app_name>.models import <class_name>
```

3. Print all objects that are referencing the class that was imported

Note: An object should be returned, but it should be empty.

```python
print(<class_name>.objects.all())
```

4. Create a new object with the class

Note: If you set attributes within the class, it must be provided as arguments

```python
x = <class_name>(<any_required_arguments>)
```

5. Save the new object

Note: This `save()` method is inherited from the `Models` class.

```python
x.save()
```

6. Print all objects that have references the class to make sure the new instance of the class is saved

```python
print(<class_name>.objects.all())
```

7. View the data from the admin page

Note: We first need to setup the admin account. Follow the section `Inital Admin Setup` section before proceeding.

# Initial Admin Setup

This section will cover the steps to setup the first admin account for the application.

1. Register the models to the `admin.py` file

- Import all classes that was created in the `models.py` file
- Register each model by using the following Python code:

```python
admin.site.register(<class_name>)
```

2. Create a super user

Using the following command in the terminal, create a new super user.

Note: You will be asked to create a Username and Password. Also provide an email address.

```bash
python manage.py createsuperuser
```

3. Run the server

```bash
python manage.py runserver
```

4. Navigate to the `/admin` webpage

Enter the username and password you created in step 2.

5. Navigate through the options

Django has automatically created an admin dashboard for you and there are many things you can do within the web interface.

Some of the things you are able to do include:
- Manage admin users
- Manage tables/data
- etc.


