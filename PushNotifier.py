import requests
import json

class PushNotifier:
    def __init__(self, username, password, package_name, api_key):
        self.base_url = 'https://api.pushnotifier.de/v2'
        self.login_url = self.base_url + '/user/login'
        self.devices_url = self.base_url + '/devices'
        self.refresh_url = self.base_url + '/user/refresh'
        self.send_text_url = self.base_url + '/notifications/text'
        self.username = username
        self.password = password
        self.login_data = {
        'username': self.username,
        'password': self.password
        }
        self.package_name = package_name
        self.api_key = api_key
        self.app_token = self.__get_app_token()
        self.headers = {'X-AppToken': self.app_token}

    def __get_app_token(self):
        r = requests.post(self.login_url, data=self.login_data, auth=(self.package_name, self.api_key))
        app_token = json.loads(r.text)['app_token']
        return app_token

    def refresh_token(self):
        r = requests.get(self.refresh_url, auth=(self.package_name, self.api_key), headers=self.headers)
        new_token = r.json()
        return new_token

    def get_devices(self):
        r = requests.get(self.devices_url, auth=(self.package_name, self.api_key), headers=self.headers)
        devices = r.json()
        return devices

    def send_text(self, text, devices):
        body = {
        'devices': devices,
        'content': text
        }
        r = requests.put(self.send_text_url, data=body, auth=(self.package_name, self.api_key), headers=self.headers)
        
