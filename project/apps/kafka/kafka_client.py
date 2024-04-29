from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, servers='kafka:9092'):
        self.producer = Producer({'bootstrap.servers': servers})

    def send(self, topic, value):
        self.producer.produce(topic, value.encode('utf-8'))
        self.producer.poll(0)

    def close(self):
        self.producer.flush()
