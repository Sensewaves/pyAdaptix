
from stream import Stream


class Client:

    def __init__(self, base_url=None, api_key=None):
        self.conf = {'base_url': base_url, 'api_key': api_key}
        self.Stream = None

    def stream(self, description, name, device_id=None, anomaly_monitoring=None, data_rate=None):
        self.Stream = Stream(configuration=self.conf, description=description, name=name, device_id=device_id,
                             anomaly_monitoring=anomaly_monitoring, data_rate=data_rate)
        return self.Stream
