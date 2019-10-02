# twitter-ETL-pipeline
an ETL pipeline that gets data from twitter, queues on Kafka and sends to amazon S3

Data is gotten from twitter using Twitter Streaming API. send_data_to_kafka.py is used to get the data from twitter and send to kafka.

the data is in json form and has the following data

* Tweet ID
* Tweet text
* source of tweet e.g Twitter for iPhone
* Retweeted. this field is boolean
* Retweet_count. this field contains the amount of retweets a post have
* created_at. This field contains the time a tweet was created
* username. This contains the username of the tweet sender at the time of the tweet being sent
* user_id. This is the unique ID for a twitter user.
* profile_image_url. Url to the profile image of the user at the time of the tweet being sent
* followers. This is the amount of the followers the sender of tweet had at the time of the tweet being sent


A cronjob is made to run kafka_get.py to get data from kafka and write to json file which is saved in the same directory.

cronjob.py is what initiates the cronjob which uses cronTab python library inorder to trigger the computer or server to run the python script after some minutes (in this case, 1minute)

this can only work on linux computers or servers.


