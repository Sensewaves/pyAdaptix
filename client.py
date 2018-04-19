import json
import logging
import requests
from utils import JsonSerializer


class HttpClient:

    def __init__(self, url, api_key):
        self.base_url = url
        self.api_key=api_key
        self.streams_url = self.base_url + "/streams"
        self.devices_url = self.base_url + "/devices"
        self.configurations_url = self.base_url + "/configurations"
        self.request_header = {'Content-Type': 'application/json', 'Accept': 'application/json',
                               'X-API-Key': self.api_key}
        self.timeout = 1000

    def create_stream(self, stream):
        json_stream = JsonSerializer(stream).dump()
        print(json_stream)
        logging.debug("Stream to send stream" + json_stream)
        r = requests.post(self.streams_url, data=json_stream, headers=self.request_header, timeout=self.timeout)
        if r.status_code != 200 and r.status_code != 201:
            logging.error("[Adaptix] POST failed with ERROR " + str(r.status_code) + " " + str(r.text))
            return None
        else:
            return json.loads(r.content)