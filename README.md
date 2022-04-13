<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# ckanext-status

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-status/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-status)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-status/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-status)
[![CKAN](https://img.shields.io/badge/ckan-2.9.1-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)

_A CKAN extension that adds a 'status' bar to the top of the page._


# Overview

This extension allows maintainers to add a simple static message to the top of every page by setting
a single configuration option.
For example, it can be used to notify users of planned downtime, unexpected issues with the site, or
new features.


# Installation

Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1. Clone the repository into the `src` folder:

  ```bash
  cd $INSTALL_FOLDER/src
  git clone https://github.com/NaturalHistoryMuseum/ckanext-status.git
  ```

2. Activate the virtual env:

  ```bash
  . $INSTALL_FOLDER/bin/activate
  ```

3. Install the requirements from requirements.txt:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-status
  pip install -r requirements.txt
  ```

4. Run setup.py:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-status
  python setup.py develop
  ```

5. Add 'status' to the list of plugins in your `$CONFIG_FILE`:

  ```ini
  ckan.plugins = ... status
  ```


# Usage

To turn the status bar on, login as a sysadmin and head to the system configuration page.
There, just set the `ckanext.status.message` config option.
To deactivate it, just remove the contents of the text box.


## Templates

This extension adds content to the `{% block skip %}` section of `page.html`. To add it elsewhere:

```html+jinja
{% if h.status_get_message() %}
    {% resource 'ckanext-status/main' %}
    <p id="status-bar">{{ h.status_get_message() }}</p>
{% endif %}
```


# Testing
_Test coverage is currently extremely limited._

To run the tests in this extension, there is a Docker compose configuration available in this
repository to make it easy.

To run the tests against ckan 2.9.x on Python3:

1. Build the required images
```bash
docker-compose build
```

2. Then run the tests.
   The root of the repository is mounted into the ckan container as a volume by the Docker compose
   configuration, so you should only need to rebuild the ckan image if you change the extension's
   dependencies.
```bash
docker-compose run ckan
```

The ckan image uses the Dockerfile in the `docker/` folder which is based on `openknowledge/ckan-dev:2.9`.
