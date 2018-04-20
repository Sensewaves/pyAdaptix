
class StreamEntity:

    def __init__(self, description=None, name=None, device_id=None, anomaly_monitoring=None, data_rate=None, stream_id=None):
        self.name = name
        self.description = description
        self.device_id = device_id
        self.anomaly_monitoring = anomaly_monitoring
        self.data_rate = data_rate
        self.patterns = []
        self.points = []
        self.tags = []
        self.store_points = False
        self.id = stream_id

    def add_points(self, point):
        if not self.points:
            self.store_points = True
        self.points.append(point)
    
    def add_tag(self, tag):
        self.tags.append(tag)


class PatternEntity:

    def __init__(self, name, description, stream_id, _from, to):
        self.stream_id = stream_id
        self.description = description
        self.name = name
        self._from = _from
        self.to = to






