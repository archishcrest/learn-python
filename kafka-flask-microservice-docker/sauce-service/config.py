kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'acks': 'all'
}

consumer_config = {
    'auto.offset.reset': 'earliest',
    'group.id': 'sauces',
}