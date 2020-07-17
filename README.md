# Django survey

This is django survey app without tex, pdf report.

A django survey app, based on and compatible with "django-survey".
You will be able to migrate your data from an ancient version of
django-survey, but it has been ported to python 3 and you can export results as
CSV using your native language.

If you want the latest version still compatible with python 2.7 you need a
version < 1.3.0.

[![Build Status](https://travis-ci.org/Pierre-Sassoulas/django-survey.svg?branch=master)](https://travis-ci.org/Pierre-Sassoulas/django-survey)
[![Coverage Status](https://coveralls.io/repos/github/Pierre-Sassoulas/django-survey/badge.svg?branch=master)](https://coveralls.io/github/Pierre-Sassoulas/django-survey?branch=master)
[![PyPI version](https://badge.fury.io/py/django-survey-and-report.svg)](https://badge.fury.io/py/django-survey-and-report)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Table of contents

* [Language available](#language-available)
* [Getting started](#getting-started)
* [Making a survey](#making-a-survey)
* [Contributing as a developer](#contributing-as-a-developer)
  * [Development environment](#development-environment)
  * [Committing code](#committing-code)
    * [Launching tests](#launching-tests)
    * [Adding test data](#adding-test-data)
    * [Launching coverage](#launching-coverage)
    * [Applying Lint](#applying-lint)
* [Translating the project](#translating-the-project)
  * [As a developer](#as-a-developer)
  * [As a translator](#as-a-translator)
* [Credit](#credits)

## Language available

The software is developed in english. Other available languages are :

* [x] Chinese thanks to [朱聖黎 (Zhu Sheng Li)](https://github.com/digglife/), [John Lyu](https://github.com/PaleNeutron) and [Anton Melser](https://github.com/AntonOfTheWoods/) \(with help from 宋璐\)
* [x] French thanks to [Pierre Sassoulas](https://github.com/Pierre-Sassoulas/) and [Anton Melser](https://github.com/AntonOfTheWoods/)
* [x] Japanese thanks to [Nobukuni Suzue](https://github.com/nsuzue/)
* [x] Spanish thanks to [Javier Ordóñez](https://github.com/ordonja/), [Pierre Sassoulas](https://github.com/Pierre-Sassoulas/) and [Anton Melser](https://github.com/AntonOfTheWoods/)
* [x] Russian thanks to [Vlad M.](https://github.com/manchos/) and [Anton Melser](https://github.com/AntonOfTheWoods/)
* [x] German thanks to [Georg Elsas](https://github.com/gjelsas)

## Getting started

Add `django-survey-and-report` to your requirements and get it with pip.

~~~~bash
echo 'django-survey-and-report' > requirements.txt
pip install -r requirements.txt
~~~~

Add `bootstrapform` and `survey` in the `INSTALLED_APPS` in your settings :

~~~~python
INSTALLED_APPS = [
	# Your own installed apps here
]

from pathlib import Path

CSV_DIRECTORY = Path("csv") # Define the directory where csv are exported

INSTALLED_APPS += [
	'bootstrapform',
	'survey'
]
~~~~

Add an URL entry to your project’s urls.py, for example:

~~~python
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    # Your own url pattern here
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^survey/', include('survey.urls'))
    ]
~~~~

Note: you can use whatever you wish as the URL prefix.

You can also change some options:

~~~~python
# Permit to open the csv in excel without problem with separator
# Using this trick : https://superuser.com/a/686415/567417
EXCEL_COMPATIBLE_CSV = True

# The separator for questions (Default to ",")
CHOICES_SEPARATOR = "|"

# What is shown in export when the user do not answer (Default to "Left blank")
USER_DID_NOT_ANSWER = "NAA"
~~~~

To uninstall `django-survey-and-report`, simply comment out or remove the
'survey' line in your `INSTALLED_APPS`.

## Making a survey

Using the admin interface you can create surveys, add questions, give questions
categories, and mark them as required or not. You can define choices for answers
using comma separated words.

![Creating of a question](doc/creating_questions.png "Creating of a question")

The front-end survey view then automatically populates based on the questions
that have been defined and published in the admin interface. We use bootstrap3
to render them.

![Answering a survey](doc/answering_questions.png "Answering a survey")

Submitted responses can be viewed via the admin backend, in an exported csv
or in a pdf generated with latex.

## Contributing as a developer

### Development environment

This is the typical command you should do to get started:

~~~~bash
python -m venv venv/ # Create virtualenv
source venv/bin/activate # Activate virtualenv
pip install -e ".[dev]" # Install dev requirements
pre-commit install # Install pre-commit hook framework
python manage.py migrate # Create database
python manage.py loaddata survey/tests/testdump.json # Load test data
python manage.py createsuperuser
python manage.py runserver # Launch server
~~~~

Please note that `pre-commit` will permit to fix a lot of linting error
automatically and is not required but highly recommended.

### Committing code

#### Launching tests

~~~~bash
python manage.py test survey
~~~~

#### Adding test data

If you want to dump a test database after adding data to it, this is
the command to have a minimal diff :

~~~~bash
python manage.py dumpdata --format json -e contenttypes -e admin -e auth.Permission
-e sessions.session -e sites.site --natural-foreign --indent 1
-o survey/tests/testdump.json
~~~~

#### Launching coverage

~~~~bash
coverage run --source=survey --omit=survey/migrations/* ./manage.py test
coverage html
xdg-open htmlcov/index.html
~~~~

#### Applying Lint

We're using `pre-commit`, it should take care of linting during commit.

## Translating the project

Django survey's is available in multiple language.
Your contribution would be very appreciated if you
know a language that is not yet available.

### As a developer

If your language do not exists add it in the `LANGUAGE` variable in the
settings, like [here](https://github.com/Pierre-Sassoulas/django-survey/commit/ee3bdba26c303ad12fc4584938e724b39223faa9#diff-bdf3ecebd8379ca98cc89e545fc90899).
Do not forget to credit yourself like in the header seen
[here](https://github.com/Pierre-Sassoulas/django-zxcvbn-password-validator/commit/274d7c9b27268a0455f80ea518c452532b970ea4#diff-8015f170326f20998060314fda9b92b1)

Then you can translate with :

~~~~bash
python manage.py makemessages
# python manage.py createsuperuser ? (You need to login for rosetta)
python manage.py runserver
# Access http://localhost:8000/admin to login
# Then go to http://localhost:8000/rosetta to translate
python manage.py makemessages --no-obsolete --no-wrap
git add survey/locale/
...
~~~~

If your language is not yet available in rosetta,
[this stack overflow question](https://stackoverflow.com/questions/12946830/)
should work even for language not handled by django.

### As a translator

If you're not a developer, open an issue on github and ask for a .po
file in your language. I will generate it for you, so you can edit it with an
online editor. I will then create the .po and commit them, so you can edit them
with your github account or integrate it myself if you do not have one.
You will be credited
[here](https://github.com/Pierre-Sassoulas/django-survey#language-available).

## Credits

Based on [jessykate's django-survey](https://github.com/jessykate/django-survey),
and contribution by jibaku, joshualoving, and ijasperyang in forks of jessykate's project.

We use [anazalea's pySankey](https://github.com/anazalea/pySankey) for sankey's
diagram during reporting.
