# This job would read from twitter and write into a kafka topic in real-time
#pip3 install tweepy
# sh kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic tweets --from-beginning
# to run: python3 51-twitter-kafka.py /home/user/workarea/projects/learn-pyspark/config/twitter.conf dev

from tweepy import OAuthHandler,Stream,StreamListener
import tweepy

# define variables to store user credentials to access twitter API, read the credentials from config file

import configparser as cp
import time
import sys

from kafka import KafkaProducer, KafkaConsumer, TopicPartition
#from kafka.producer import SimpleProducer
#from kafka.client import SimpleClient
from time import sleep
from json import dumps


conf = cp.ConfigParser()
conf.read(sys.argv[1])
env = sys.argv[2]

consumer_key=conf.get(env,'consumer_key')
consumer_secret=conf.get(env,'consumer_secret')
access_token=conf.get(env,'access_token')
access_token_secret=conf.get(env,'access_token_secret')

producer=KafkaProducer(bootstrap_servers='localhost:9092')
topic_name='tweets'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

def get_twitter_data():
    res = api.search("kafka or spark")
    for i in res:
        record=''
        record+=str(i.user.id_str)
        record+=';'
    producer.send(topic_name,str.encode(record))

def periodic_work(interval):
    while True:
        get_twitter_data()
        sleep(interval)

periodic_work(5)

