import json
import requests
from utils import JsonSerializer


class HttpWrapper:

    def __init__(self, url, api_key):
        self.base_url = url
        self.api_key = api_key
        self.request_header = {'Content-Type': 'application/json',
                               'X-API-Key': self.api_key}
        self.timeout = 1000
        self.res = None

    def post(self, uri, payload):
        json_resource = JsonSerializer(payload).dump()
        self.res = requests.post(self.base_url+uri, data=json_resource, headers=self.request_header, timeout=self.timeout)
        return self.res

    def get(self, resource):
        self.res = requests.get(resource.url, headers=self.request_header, timeout=self.timeout)
        return self.res

    def is_ok(self):
        if self.res.status_code == 200 and self.r.status_code == 201:
            return False
        else:
            return True
