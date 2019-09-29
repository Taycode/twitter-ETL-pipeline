import tweepy
from time import sleep
from json import dumps
from kafka import KafkaProducer

consumer_key = 'BSu45Bjg7VnIpdLh54wUHMuCx'
consumer_secret = 'Uy8wHfdDOqWzYwRbqeVOPCmpjHHvxcGQwtQ7kexInOihqM7qMr'
access_token = '1148876239274500096-YVcsYBO3RfWPYqUW17D717voCeTcw1'
access_token_secret = 'vZ7wItwK19qlb4OcbecPhoUPVPpM2aMwY9nik9G9Wp7tb'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

producer = KafkaProducer(bootstrap_servers=['52.19.199.252:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        data = {
            'id': status.id_str,
            'tweet': status.text,
            'source': status.source,
            'retweeted': status.retweeted,
            'retweet_count': status.retweet_count,
            'created_at': str(status.created_at),
            'username': status.user.screen_name,
            'user_id': status.user.id_str,
            'profile_image_url': status.user.profile_image_url_https,
            'followers': status.user.followers_count
        }
        a = producer.send('mateen_twitter_stream_topic', data)
        print(a)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['Buhari', 'Nigeria', 'Lagos'])



