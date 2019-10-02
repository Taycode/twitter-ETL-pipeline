from kafka import KafkaConsumer
import time
import json
import redis


redis_instance = redis.Redis()

print('Making connection.')
consumer = KafkaConsumer('mateen_twitter_stream_topic',
                         bootstrap_servers=['52.19.199.252:9092'], auto_offset_reset='earliest',
                         enable_auto_commit=False)
print('connection made')
print('Getting message.')
timeout = 5
timeout_start = time.time()
data = []
myFile = open('/home/taycode/Desktop/myetl/mateen_{}.json'.format(str(timeout_start)), 'a')
last_offset = redis_instance.get('offset')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    if message.offset <= last_offset:
        continue
    else:
        if time.time() < timeout_start + timeout:
            data.append(message.value.decode('utf-8'))
            last_offset = message.offset
            print('appended one data')
        else:
            json.dump(data, myFile)
            redis_instance.mset({'offset': last_offset})
            print('done writing')
            break
