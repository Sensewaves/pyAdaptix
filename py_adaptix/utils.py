
import json


class JsonSerializer:

    def __init__(self, instance):
        self.json = json.dumps(instance.__dict__)

    def dump(self):
        return self.json.replace("_from","from")