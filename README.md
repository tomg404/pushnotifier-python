# PushNotifier (V2) for Python
A python module to easily use the service of [PushNotifier](https://pushnotifier.de) in your python projects.
Special thanks going to [@Logxn](https://github.com/Logxn).

## Installation
- Install all dependencies
  ```
  pip install -r requirements.txt
  ```

- Install PushNotifier
  ```
  pip install pushnotifier
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
```
### Get Basic information
```python
>>> pn.login()
{'username': 'username', 'avatar': 'https://gravatar.com/avatar/XXXXX', 'app_token': 'XXXXX', 'expires_at': XXXXX}

>>> pn.get_all_devices()
['abcd', 'efgh', 'ijkl']
```
### Refresh app token
```python
>>> pn.refresh_token()
'new_token'
```
