# Django & FastAPI

- Pipenv Doc — https://pipenv-fork.readthedocs.io/
- Django 2.x Books — https://books.agiliq.com/en/latest/README.html

## Common used Django apps

- [model_bakery](https://github.com/model-bakers/model_bakery)
- [factory-boy](https://github.com/FactoryBoy/factory_boy) `fetching fake data`
- [django-braces](https://github.com/brack3t/django-braces) `classed based view`
- [djang-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) `awesome`
- [django-guardian](https://github.com/django-guardian/django-guardian)
- [django-jimmypage](https://github.com/yourcelf/django-jimmypage) `caching`
- [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)
- [pytest](https://github.com/pytest-dev/pytest)
- [coveragepy](https://github.com/nedbat/coveragepy)

## Django Installation via Virtualenv

- Go to the directory and type `pip install pipenv`
- After it has been installed successfully type `pipenv install`
- It will create new virtualenv and activate venv type `pipenv shell`
- Install django type `pipenv install django` | `pip install django==x.x.x`
- type `pipenv --venv` to check is there any venv for this current project & if satisfied it will show location else return no venv has been created
- Exit virtual env type `exit` or `CTRL + d` & back to normal prompt
- Create Django project `django-admin startproject "NameOfProject" .`
- Create django app `python manage.py startapp "NameofApp"`
- Migration command `python manage.py makemigrations` then `python manage.py migrate`
- Remove venv `pipenv --rm`.. It will be deleted virtualenv for this current project
- Create requirements.txt file --> `pip freeze > requirements.txt`
- Install all dependencis after clone -> `pip install` -> `pipenv install -r requirements.txt`
- Check Django version `python -m django --version`

## Django Track

- [wsvincent/awesome-django](https://github.com/wsvincent/awesome-django)
- [Full Stack Web Development with Python & Django 1.x by Durga `mesutramsey`](https://www.youtube.com/playlist?list=PL1pDVBmUq2HS_Uri7Begq3aOBLlFQ52pp) `v1`
- [The Ultimate Django Series](https://codewithmosh.com/p/the-ultimate-django-series) — Mosh Hamedani `v2`
- [Speed Up Your Django Tests](https://adamchainz.gumroad.com/l/suydt) — Adam Johnson `v3`
- [Two Scoops of Django 3.x](https://www.feldroy.com/books/two-scoops-of-django-3-x) — Audrey Roy Greenfeld and Daniel Roy Greenfeld `v3`
- [Full Stack Python Security](https://www.manning.com/books/full-stack-python-security) — Dennis Byrne `v3`
- Django Conf
    - DjangoCon Europe 2021
        - [Videos](https://www.youtube.com/playlist?list=PLY_che_OEsX0C5IkZcqPlrbKvce178kFD)
        - [WorkShop](https://www.youtube.com/playlist?list=PLY_che_OEsX2KIIqShIrNgoxvBgNJP_ye)
    - [Django & FastAPI Conf Playlist](https://www.youtube.com/playlist?list=PLshEJn4_ZJAawWMcHoHM_zTKCzjkgSnFY)
- [Python & Django Projects](https://www.youtube.com/playlist?list=PLshEJn4_ZJAYffGl55VlOWJYoKIK7bzjv) `v2`
- [Advanced Django Training](https://django-advanced-training.readthedocs.io/en/latest/)
- [Advanced Django: Mastering Django and Django Rest Framework Specialization](https://www.coursera.org/specializations/codio-advanced-django-and-django-rest-framework)
