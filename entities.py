class Stream:

    def __init__(self,stream_type,description,name,device_id,anomaly_monitoring,data_rate):
        self.type = stream_type
        self.name = name
        self.description = description
        self.device_id = device_id
        self.anomaly_monitoring = anomaly_monitoring
        self.data_rate = data_rate
        self.patterns =[]
        self.points = []
        self.tags = []
        self.store_points = False

    def add_points(self, point):
        if not self.points:
            self.store_points = True
        self.points.append(point)
    
    def add_tag(self, tag):
        self.tags.append(tag)


