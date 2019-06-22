# PushNotifier (V2) for Python

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pushnotifier.svg)
[![PyPI version](https://badge.fury.io/py/pushnotifier.svg)](https://badge.fury.io/py/pushnotifier)
[![Documentation Status](https://readthedocs.org/projects/pushnotifier-python/badge/?version=latest)](https://pushnotifier-python.readthedocs.io/en/latest/?badge=latest)
![GitHub](https://img.shields.io/github/license/tomg404/pushnotifier-python.svg)

[![Gitter](https://badges.gitter.im/pushnotifier/community.svg)](https://gitter.im/pushnotifier/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
![Codacy grade](https://img.shields.io/codacy/grade/c7eb50b6f38b48aca431fc576ff7eb29.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/tomg404/pushnotifier-python.svg)

A python module to easily use the service of [PushNotifier](https://pushnotifier.de) in your python projects.

You can find the documentation [here](https://pushnotifier-python.readthedocs.io/en/latest/).

Special thanks go to [@Logxn](https://github.com/Logxn).

## About
Easily send

-   messages ✉️
-   urls 🌎
-   images 🖼️

via python to all your devices. For more info visit [pushnotifier.de](https://pushnotifier.de)

## Installation
**Note: you have to have `requests` installed (`pip install requests`)**
-   Install PushNotifier via pip
    ```console
    $ pip install pushnotifier
    ```

-   Install PushNotifier manually
    ```console
    $ git clone https://github.com/tomg404/pushnotifier-python
    $ cd /path/to/repository/
    $ python setup.py install
    ```

## Usage
```python
from pushnotifier import PushNotifier as pn

pn = pn.PushNotifier('username', 'password', 'package_name', 'api_key')
```

### Sending messages
```python
>>> pn.send_text('hello world', silent=False, devices=['abcd', 'efgh'])
>>> pn.send_url('https://www.example.com', silent=False, devices=['abcd', 'efgh'])
>>> pn.send_notification('hello world', 'https://www.example.com', silent=False, devices=['abcd', 'efgh'])

>>> # Note on send_image: currently you can't send images to android/ios devices
>>> pn.send_image('path/to/image.png', silent=False, devices=['abcd', 'efgh'])
```

### Get Basic information
```python
>>> password = 'XXXXX'
>>> pn.login(password)
{'username': 'username', 'avatar': 'https://gravatar.com/avatar/XXXXX', 'app_token': 'XXXXX', 'expires_at': XXXXX}

>>> pn.get_all_devices()
['abcd', 'efgh', 'ijkl']
```
### Refresh app token
```python
>>> pn.refresh_token()
'new_token'
```

### More detailed help
See the [documentation](https://pushnotifier-python.readthedocs.io/en/latest/) or
```python
>>> help(pn.some_method_you_need_help_on)
```
