import requests
from utils import JsonSerializer
import logging


class HttpWrapper:

    def __init__(self, url, api_key, debug_mode):
        self.base_url = url
        self.api_key = api_key
        self.request_header = {'Content-Type': 'application/json',
                               'X-API-Key': self.api_key}
        self.timeout = 1000
        self.res = None
        if debug_mode:
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

    def post(self, uri, payload):
        json_resource = JsonSerializer(payload).dump()
        print(json_resource)
        self.res = requests.post(self.base_url+uri, data=json_resource, headers=self.request_header, timeout=self.timeout)
        return self.res

    def get(self, uri):
        self.res = requests.get(self.base_url+uri, headers=self.request_header, timeout=self.timeout)
        return self.res
