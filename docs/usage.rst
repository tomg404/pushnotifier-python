=====
Usage
=====

Initialization
--------------


  The PushNotifier object takes four parameters.

  1. ``username:`` your username from https://pushnotifier.de

  2. ``password:`` your password from https://pushnotifier.de

  3. ``package_name:`` the package you want to send your messages to

  4. ``api_key:`` your api key from https://pushnotifier.de/account/api

  ::

      >>> from pushnotifier import PushNotifier as pn
      >>> pn = pn.PushNotifier('username', 'password', 'package_name', 'api_key')


login
-----

  The ``login`` method returns a dictionary with some basic information
  about your account if the login data is valid::

      >>> pn.login(password)
      {'username': 'username', 'avatar': 'https://gravatar.com/avatar/XXXXX', 'app_token': 'XXXXX', 'expires_at': XXXXX}


send_text
---------

  The ``send_text`` method takes three parameters of which only ``text`` is required.

  ::

      >>> pn.send_text(text, devices, silent)
      200

  By default the message gets sent to all ``devices`` linked to your
  `PushNotifier <https://pushnotifier.de>`_ account.
  The ``silent`` parameter, which by default is set to ``False`` specifies if the
  message triggers a sound on the device(s) it gets sent to. ``send_text`` returns
  ``200`` if nothing went wrong.


  **Example:** Send the message to specific devices only and don't trigger a sound
  on the receiving devices.

  ::

    >>> pn.send_text(text, devices=['ID1', 'ID2'], silent=True)
    200

  **Errors:**

  +-------------------------------------+
  | MalformedRequestError               |
  +-------------------------------------+
  | DeviceNotFoundError                 |
  +-------------------------------------+


send_url
--------

  The ``send_url`` method has the same parameters as the ``send_text`` method
  except that it takes an ``url`` instead of text.
  ::

      >>> pn.send_url(url, devices, silent)
      200

  **Example:**

  ::

      >>> pn.send_url('https://www.example.com')
      200

  **Errors and returns:**

  ``send_url`` raises the **same errors** and has the **same returns** as ``send_text``.


send_notification
-----------------

  To send a notification you have to pass 2 parameters to the method. ``text``
  and ``url``. Apart from that the method again is basically the same as
  ``send_text`` and ``send_url``.
  ::

      >>> pn.send_notification(text, url, devices, silent)
      200

  **Example:**

  ::

      >>> pn.send_url('hello world', 'https://www.example.com')
      200

  **Errors and returns:**

  ``send_notification`` raises the **same errors** and has the **same returns** as
  ``send_text`` and ``send_url``.


send_image
----------

  To send an image you only have to pass the ``path`` of your image to the method.
  The method returns ``200`` if eveverything went OK.

  ::

      >>> pn.send_image(image_path, devices, silent)
      200

  .. IMPORTANT::
    If you leave the ``devices`` parameter untouched and you have a
    mobile phone in your devices list the method will raise a ``UnsupportedMediaTypeError``
    because the `PushNotifier API <https://pushnotifier.de>`_ currently doesn't
    support sending images to mobile phones.

  **Example:**

  ::

      >>> pn.send_image('path/to/image.png', devices=['ID1', 'ID2', 'ID3'])


  **Errors:**

  +-------------------------------------+
  | MalformedRequestError               |
  +-------------------------------------+
  | DeviceNotFoundError                 |
  +-------------------------------------+
  | PayloadTooLargeError                |
  +-------------------------------------+
  | UnsupportedMediaTypeError           |
  +-------------------------------------+
