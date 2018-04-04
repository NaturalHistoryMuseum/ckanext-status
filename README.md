# ckanext-status

[![Travis branch](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-status/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-status) [![Coveralls github branch](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-status/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-status)

A CKAN plugin to display a simple bar with a status message at the head of a page.

# Setup
1. Clone the repository into the virtual env's `src` folder:
```bash
cd /usr/lib/ckan/default/src/
git clone https://github.com/NaturalHistoryMuseum/ckanext-status.git
```

2. Activate the virtual env:
```bash
. /usr/lib/ckan/default/bin/activate
```

3. Run setup.py:
```bash
cd /usr/lib/ckan/default/src/ckanext-status
python setup.py develop
```

4. Add 'status' to the list of plugins in your config file:
```
ckan.plugins = ... status
```

# Configuration
To turn it on, set a message in the config file:
```
ckanext.status.message = Everything is working perfectly
```

To turn it off, simply remove the config option (or comment it out).

# Testing
```bash
nosetests --ckan --with-pylons=/path/to/your/dev/config ckanext/status/tests
```
