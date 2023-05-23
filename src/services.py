import json

import allure
import requests

import config
from src.response import AssertableResponse


class ApiClient:
    def __init__(self):
        self._base = ApiServiceBase()
        self._token = self._base.token
        self.user = UserApiService(token=self._token)


class ApiServiceBase:

    def __init__(self, token=None):
        self.base_url = config.BASE_URL
        self._headers = {'Content-type': 'Application/json'}
        self.token = self.login().field('access') if token is None else token
        self._auth_headers = {**self._headers, 'Authorization': f'JWT {self.token}'}

    def _get(self, url, headers=None):
        headers = headers if headers else self._headers
        return requests.get(f'{self.base_url}{url}', headers=headers)

    def _post(self, url, body, headers=None):
        headers = headers if headers else self._headers
        return requests.post(f'{self.base_url}{url}', data=json.dumps(body), headers=headers)

    def login(self):
        data = {"email": config.USER_EMAIL, "password": config.USER_PASSWORD}
        return AssertableResponse(self._post('/accounts/login/', data, headers=self._headers))


class UserApiService(ApiServiceBase):

    @allure.step("Request to /accounts/me/ endpoint")
    def get_me(self):
        return AssertableResponse(self._get('/accounts/me/', headers=self._auth_headers))
