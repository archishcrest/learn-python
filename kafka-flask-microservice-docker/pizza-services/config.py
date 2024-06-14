kafka_config = {
    # User-specific properties that you must set
    'bootstrap.servers': 'localhost:9092',

    # Fixed properties
    'acks': 'all'
}

consumer_config = {
    'auto.offset.reset': 'earliest',
    'group.id': 'pizza_shop',
    'enable.auto.commit': 'true',
    'max.poll.interval.ms': '3000000'
}

# 
# sr_config = {
#     'url': 'http://localhost:8081'
# }