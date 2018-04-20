# pyAdaptix
An python interface to the Adaptix platform API  https://www.sensewaves.io

# usage : 


```ruby
client = Client(base_url="PROVIDED_API_URL",
                api_key="YOUR_API_KEY",
                debug_mode=True)
                
resp = client.streams.create(
        name="Stream X", 
        description="description of stream X",
        anomaly_monitoring=False,
        data_rate="1d")

stream = client.streams.fetch()
## or with a specific id 
stream = client.streams.fetch(stream_id="XXXXX")

```