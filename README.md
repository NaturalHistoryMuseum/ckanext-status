<!--header-start-->
<img src="https://data.nhm.ac.uk/images/nhm_logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# ckanext-status

[![Tests](https://img.shields.io/github/actions/workflow/status/NaturalHistoryMuseum/ckanext-status/main.yml?style=flat-square)](https://github.com/NaturalHistoryMuseum/ckanext-status/actions/workflows/main.yml)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-status/main?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-status)
[![CKAN](https://img.shields.io/badge/ckan-2.9.7-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)
[![Docs](https://img.shields.io/readthedocs/ckanext-status?style=flat-square)](https://ckanext-status.readthedocs.io)

_A CKAN extension that adds a 'status' bar and an extensible system status page._

<!--header-end-->

# Overview

<!--overview-start-->
This extension allows maintainers to add a simple static message to the top of every page by setting a single configuration option.
For example, it can be used to notify users of planned downtime, unexpected issues with the site, or new features.

It also adds a status page giving an overview of the health of various systems. By default this has very few items, but it is easily extensible by other CKAN extensions.

<!--overview-end-->

# Installation

<!--installation-start-->
Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

## Installing from PyPI

```shell
pip install ckanext-status
```

## Installing from source

1. Clone the repository into the `src` folder:
   ```shell
   cd $INSTALL_FOLDER/src
   git clone https://github.com/NaturalHistoryMuseum/ckanext-status.git
   ```

2. Activate the virtual env:
   ```shell
   . $INSTALL_FOLDER/bin/activate
   ```

3. Install via pip:
   ```shell
   pip install $INSTALL_FOLDER/src/ckanext-status
   ```

### Installing in editable mode

Installing from a `pyproject.toml` in editable mode (i.e. `pip install -e`) requires `setuptools>=64`; however, CKAN 2.9 requires `setuptools==44.1.0`. See [our CKAN fork](https://github.com/NaturalHistoryMuseum/ckan) for a version of v2.9 that uses an updated setuptools if this functionality is something you need.

## Post-install setup

1. Add 'status' to the list of plugins in your `$CONFIG_FILE`:
   ```ini
   ckan.plugins = ... status
   ```

2. Install `lessc` globally:
   ```shell
   npm install -g "less@~4.1"
   ```

<!--installation-end-->

# Configuration

<!--configuration-start-->


<!--configuration-end-->

# Usage

<!--usage-start-->

## Status bar

To turn the status bar on, login as a sysadmin and head to the system configuration page.
There, just set the `ckanext.status.message` config option.
To deactivate it, just remove the contents of the text box.

This extension adds content to the `{% block skip %}` section of `page.html`. To add it elsewhere:

```html+jinja
{% if h.status_get_message() %}
    {% resource 'ckanext-status/main' %}
    <p id="status-bar">{{ h.status_get_message() }}</p>
{% endif %}
```

## Status page

The status page can be found at `/status`, or the JSON response can be accessed from the API at `/api/3/action/status_list`. By default it only contains one status report: the number of queues with pending items. Additional status report items come from other CKAN extensions implementing the `IStatus` interface.

To add status report items in another extension, add the `modify_status_reports` method of the `IStatus` interface in `plugin.py`:
```python
from ckan.plugins import SingletonPlugin, implements
from ckanext.status.interfaces import IStatus

class ExamplePlugin(SingletonPlugin):
    implements(IStatus)

    def modify_status_reports(self, status_reports):
        status_reports.append({
            'label': 'Example status',
            'value': 'connected',
            'group': 'Examples',  # can be omitted
            'help': 'A description of what this means',
            'state': 'good'  # valid values: good, ok, bad, neutral
        })

        return status_reports
```

<!--usage-end-->

# Testing

<!--testing-start-->
There is a Docker compose configuration available in this repository to make it easier to run tests. The ckan image uses the Dockerfile in the `docker/` folder.

To run the tests against ckan 2.9.x on Python3:

1. Build the required images:
   ```shell
   docker-compose build
   ```

2. Then run the tests.
   The root of the repository is mounted into the ckan container as a volume by the Docker compose
   configuration, so you should only need to rebuild the ckan image if you change the extension's
   dependencies.
   ```shell
   docker-compose run ckan
   ```

<!--testing-end-->
