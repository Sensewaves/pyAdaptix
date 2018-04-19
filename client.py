
from stream import Stream


class Client:

    def __init__(self, base_url=None, api_key=None):
        self.conf = {'base_url': base_url, 'api_key': api_key}
        self.Stream = None

    @property
    def streams(self):
        self.Stream = Stream(connection=self.conf)
        return self.Stream
