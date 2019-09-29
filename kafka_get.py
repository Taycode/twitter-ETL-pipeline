from kafka import KafkaConsumer
from kafka import TopicPartition

print('Making connection.')
consumer = KafkaConsumer('mateen_twitter_stream_topic',
                         bootstrap_servers=['52.19.199.252:9092'], auto_offset_reset='earliest',
                         enable_auto_commit=False)
print('connection made')
print('Getting message.')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%d : value=%s" % (message.offset, message.value))
