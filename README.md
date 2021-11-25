# Django Installation via Virtualenv [pipenv]

Pipenv Doc — https://pipenv-fork.readthedocs.io/

- Go to the directory and type `pip install pipenv`
- After it has been installed successfully type `pipenv install`
- It will create new virtualenv and activate venv type `pipenv shell`
- Install django type `pipenv install django`
- type `pipenv --venv` to check is there any venv for this current project & if satisfied it will show location else return no venv has been created
- Exit virtual env type `exit` or `CTRL + d` & back to normal prompt
- Create Django project `django-admin startproject "NameOfProject" .`
- Remove venv `pipenv --rm`.. It will be deleted virtualenv for this current project
- Create requirements.txt file --> `pip freeze > requirements.txt`
- Install all dependencis after clone -> `pip install` -> `pipenv install -r requirements.txt`
