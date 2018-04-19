from http import HttpWrapper as http
from entities import StreamEntity
import json
import logging


class CannotCreateStreamError(LookupError):
    """Raise when when response is different from 20X"""


class Stream:

    def __init__(self, connection):
            self.http = http
            self.uri = "streams"
            self.http = http(url=connection["base_url"], api_key=connection["api_key"])
            self.stream = None

    def with_tag(self, tag):
        self.stream.add_tag(tag)

    def with_point(self, point):
        self.stream.add_points(point)

    def create(self, name, description, device_id=None, anomaly_monitoring=None, data_rate=None):
        stream = StreamEntity(name=name, description=description,
                              device_id=device_id, anomaly_monitoring=anomaly_monitoring, data_rate=data_rate)
        res = self.http.post(uri=self.uri, payload=stream)
        if res.status_code != 200 and res.status_code != 201:
            logging.error("[Adaptix] POST failed with ERROR " + str(res.status_code) + " " + str(res.text))
        else:
            json_res = json.loads(res.text)
            return json_res

    def fetch(self,id=None):
        if id is None:
            json_res = json.loads(self.http.get(uri=self.uri).text)
        else:
            json_res = json.loads(self.http.get(uri=self.uri+"/"+id).text)
        return json_res

