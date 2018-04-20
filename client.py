
from restWrappers import Stream
from restWrappers import Pattern


class Client:

    def __init__(self, base_url=None, api_key=None, debug_mode=False):
        self.conf = {'base_url': base_url, 'api_key': api_key, 'debug_mode': debug_mode}
        self.Stream = None
        self.Pattern = None

    @property
    def streams(self):
        self.Stream = Stream(connection=self.conf)
        return self.Stream

    @property
    def patterns(self):
        self.Pattern = Pattern(connection=self.conf)
        return self.Pattern
