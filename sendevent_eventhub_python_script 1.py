import time
import os
import uuid
import datetime
import random
import json

import azure.eventhub
from azure.eventhub import EventHubProducerClient, EventData

# This script simulates the production of events for 10 devices.
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

# Create a producer client to produce and publish events to the event hub.
producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://vamsi-event.servicebus.windows.net/;SharedAccessKeyName=python;SharedAccessKey=9qUnX990zzSxUqYfFggAOjoe8WZmxrmWE+AEhAtNGvQ=;EntityPath=majji", eventhub_name="majji")

for y in range(0,2000):    # For each device, produce 20 events. 
    event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later. 
    for dev in devices:
        # Create a dummy reading.
        reading = {'id': random.randint(1, 10), 'timestamp': str(datetime.datetime.utcnow()), 'temperature': random.randint(70, 100), 'humidity': random.randint(70, 100)}
        s = json.dumps(reading) # Convert the reading into a JSON string.
        event_data_batch.add(EventData(s)) # Add event data to the batch.
        print("events proccessing", s)
    producer.send_batch(event_data_batch) # Send the batch of events to the event hub.

# Close the producer.    
producer.close()