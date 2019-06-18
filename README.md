# PushNotifier (V2) for Python
[![PyPI version](https://badge.fury.io/py/pushnotifier.svg)](https://badge.fury.io/py/pushnotifier)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pushnotifier.svg)
![GitHub contributors](https://img.shields.io/github/contributors/tomg404/pushnotifier-python.svg)
![Codacy grade](https://img.shields.io/codacy/grade/c7eb50b6f38b48aca431fc576ff7eb29.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/tomg404/pushnotifier-python.svg)
![GitHub](https://img.shields.io/github/license/tomg404/pushnotifier-python.svg)

A python module to easily use the service of [PushNotifier](https://pushnotifier.de) in your python projects.
Special thanks go to [@Logxn](https://github.com/Logxn).

## About
Easily send

-   messages
-   urls
-   images

via python to all your devices. For more info visit [pushnotifier.de](https://pushnotifier.de)

## Installation
**Note: you have to have `requests` installed (`pip install requests`)**
-   Install PushNotifier via pip
  ```console
  foo@bar:~$ pip install pushnotifier
  ```

-   Install PushNotifier manually
  ```console
  foo@bar:~$ git clone https://github.com/tomg404/pushnotifier-python
  foo@bar:~$ cd /path/to/repository/
  foo@bar:~$ python setup.py install
  ```

## Usage
```python
from pushnotifier import PushNotifier as pn

pn = pn.PushNotifier('username', 'password', 'package_name', 'api_key')
```

### Sending messages
```python
>>> pn.send_text('hello world', silent=False)
>>> pn.send_url('https://www.example.com', silent=True)
>>> pn.send_notification('hello world', 'https://www.example.com')	# by default silent is set to False
>>> pn.send_image('path/to/image.png')
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
