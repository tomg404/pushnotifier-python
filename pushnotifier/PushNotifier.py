import requests
import json
import base64
import random
import string
from pushnotifier.exceptions import *


class PushNotifier:
    def __init__(self, username, password, package_name, api_key):
        self.base_url = 'https://api.pushnotifier.de/v2'
        self.login_url = self.base_url + '/user/login'
        self.devices_url = self.base_url + '/devices'
        self.refresh_url = self.base_url + '/user/refresh'
        self.send_text_url = self.base_url + '/notifications/text'
        self.send_image_url = self.base_url + '/notifications/image'
        self.username = username
        self.package_name = package_name
        self.api_key = api_key
        self.app_token = self.__get_app_token(password)
        self.headers = {'X-AppToken': self.app_token}

    # checks if username, password, package_name and api_key are valid
    # and returns some infos
    def login(self, password):
        login_data = {
        'username': self.username,
        'password': password
        }
        r = requests.post(self.login_url, json=login_data, auth=(self.package_name, self.api_key), headers=self.headers)
        return r.json()

    def __get_app_token(self, password):
        login_data = {
        'username': self.username,
        'password': password
        }
        r = requests.post(self.login_url, data=login_data, auth=(self.package_name, self.api_key))

        if r.status_code == 401:
            raise UnauthorizedError
        elif r.status_code == 403:
            raise IncorrectCredentialsError
        elif r.status_code == 404:
            raise UserNotFoundError

        app_token = json.loads(r.text)['app_token']
        return app_token


    # calls https://api.pushnotifier.de/v2/user/refresh to refresh the app token
    def refresh_token(self):
        r = requests.get(self.refresh_url, auth=(self.package_name, self.api_key), headers=self.headers)
        new_token = r.json()['app_token']
        self.app_token = new_token
        return new_token

    # returns an array of the 'id's of every device
    def get_all_devices(self):
        r = requests.get(self.devices_url, auth=(self.package_name, self.api_key), headers=self.headers)
        devices = r.json()
        devices_array = []
        for index, _ in enumerate(devices):
            devices_array.append(devices[index]['id'])
        return devices_array

    # sends text to all devices specified.
    # if no device is specified it sends the message to every device.
    # returns the response code of the api.
    def send_text(self, text, devices=None, silent=False):
        if devices == None:
            body = {
            "devices": self.get_all_devices(),
            "content": text,
            "silent": silent
            }
        else:
            body = {
            "devices": devices,
            "content": text,
            "silent": silent
            }

        r = requests.put(self.send_text_url, json=body, auth=(self.package_name, self.api_key), headers=self.headers)
        if r.status_code == 200:
            return 200
        elif r.status_code == 400:
            raise MalformedRequestError
            return 400
        elif r.status_code == 404:
            raise DeviceNotFoundError
            return 404

    # basically same functionality as send_text
    def send_url(self, url, devices=None, silent=False):
        if devices == None:
            body = {
            "devices": self.get_all_devices(),
            "content": url,
            "silent": silent
            }
        else:
            body = {
            "devices": devices,
            "content": url,
            "silent": silent
            }

        r = requests.put(self.send_text_url, json=body, auth=(self.package_name, self.api_key), headers=self.headers)

        if r.status_code == 200:
            return 200
        elif r.status_code == 400:
            raise MalformedRequestError
            return 400
        elif r.status_code == 404:
            raise DeviceNotFoundError
            return 404

    # basically same functionality as send_text
    def send_notification(self, text, url, devices=None, silent=False):
        if devices == None:
            body = {
            "devices": self.get_all_devices(),
            "content": text,
            "url": url,
            "silent": silent
            }
        else:
            body = {
            "devices": devices,
            "content": text,
            "url": url,
            "silent": silent
            }

        r = requests.put(self.send_text_url, json=body, auth=(self.package_name, self.api_key), headers=self.headers)

        if r.status_code == 200:
            return 200
        elif r.status_code == 400:
            raise MalformedRequestError
            return 400
        elif r.status_code == 404:
            raise DeviceNotFoundError
            return 404

    # basically same functionality as send_text but you are passing an image to the function
    def send_image(self, image_path, devices=None, silent=False):
        with open(image_path, "rb") as image_file:
            encoded_bytes = base64.b64encode(image_file.read())

        # encoded_image are base64 encoded bytes of the image_file bytes
        # since json can't handle raw bytes we need to decode them into a base64 string
        encoded_image = encoded_bytes.decode('utf-8')
        file_name = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(10))
        if devices == None:
            body = {
            "devices": self.get_all_devices(),
            "content": encoded_image,
            "filename": file_name,
            "silent": silent
            }
        else:
            body = {
            "devices": devices,
            "content": encoded_image,
            "filename": file_name,
            "silent": silent
            }

        r = requests.put(self.send_image_url, json=body, auth=(self.package_name, self.api_key), headers=self.headers)

        if r.status_code == 200:
            return 200
        elif r.status_code == 400:
            raise MalformedRequestError
            return 400
        elif r.status_code == 404:
            raise DeviceNotFoundError
            return 404
