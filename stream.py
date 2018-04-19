from http import HttpWrapper as http
from entities import StreamEntity


class Stream:

    def __init__(self, configuration, description, name, device_id=None, anomaly_monitoring=None, data_rate=None):
        self.store_points = False
        self.http = http
        self.uri = "streams"
        self.http = http(url=configuration["base_url"], api_key=configuration["api_key"])
        self.configuration = configuration
        self.stream = StreamEntity(description=description, name=name,
                                   device_id=device_id, anomaly_monitoring=anomaly_monitoring, data_rate=data_rate)

    def create(self):
        self.http.post(uri=self.uri, payload=self.stream)

    def fetch(self):
        self.http.get(uri=self.uri)

