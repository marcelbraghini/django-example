# Example django + pybuilder

[python 3.7](https://www.python.org/downloads/release/python-370/)<br>
[pipEnv](https://github.com/pypa/pipenv)<br>
[pyBuilder](https://pybuilder.github.io/)<br>
[django](https://www.djangoproject.com/start/)<br>

* how to install
```python
# to create virtualenv using specific python version 
pipenv --python 3.7

# activate virtualenv
pipenv shell

# install django
pipenv install django=='2.2.3'

# install pybuilder
pipenv install --pre pybuilder
```
* run server

```python
python manage.py runserver
```

* new project

```python
# add project
django-admin startproject example

# add sub project
./manage.py startapp subProject

# aplicando migrações
./manage.py makemigrations
./manage.py migrate --run-syncdb
```

[Django Configurações de Produção](https://www.ibm.com/developerworks/br/library/os-django/index.html)<br>
[Docs Django](https://docs.djangoproject.com/pt-br/2.2/)<br>
[Gunicorn - Webservice](https://gunicorn.org/#quickstart)<br>
[Python + django web](https://pythonacademy.com.br/blog/desenvolvimento-web-com-python-e-django-template)<br>
[Tutotial django](https://giovannireisnunes.wordpress.com/2018/04/06/exemplo-em-django-parte-1/)<br>
[Pybuilder](https://pybuilder.github.io/documentation/tutorial.html)<br>

[Celery](https://pybuilder.github.io/documentation/tutorial.html)<br>
[Celery](https://medium.com/@kevin.michael.horan/scheduling-tasks-in-django-with-the-advanced-python-scheduler-663f17e868e6)<br>
[Celery](https://code.tutsplus.com/tutorials/using-celery-with-django-for-background-task-processing--cms-28732)<br>