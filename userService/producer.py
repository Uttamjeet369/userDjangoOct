import json

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})


def send_email_event(event_data):
    try:
        message_json = json.dumps(event_data)
        p.produce('sending_email', message_json)

        p.flush()

        print("Message sent")
    except Exception as e:
        print(e)
