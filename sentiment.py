from peewee import *
from tweetfeels import TweetFeels
from threading import Thread
import time

mysql_db = MySQLDatabase('sql9224506', user='sql9224506', password='NqDZ2Yd2yg',
                         host='sql9.freemysqlhosting.net', port=3306)




class BaseModel(Model):

    class Meta:
        database = mysql_db

class twitterkey(BaseModel):
    id=IntegerField(primary_key=True)
    CONSUMERKEY = CharField(max_length=150)
    CONSUMERSECRET = CharField(max_length=150)
    ACCESSTOKEN = CharField(max_length=150)
    ACCESSTOKENSECRET=CharField(max_length=150)

consumer_key=twitterkey.get(twitterkey.id==1234).CONSUMERKEY
consumer_secret=twitterkey.get(twitterkey.id==1234).CONSUMERSECRET
access_token=twitterkey.get(twitterkey.id==1234).ACCESSTOKEN
access_token_secret=twitterkey.get(twitterkey.id==1234).ACCESSTOKENSECRET


login = [consumer_key, consumer_secret, access_token, access_token_secret]



def print_feels(seconds=10,feels):
    while go_on:
        time.sleep(seconds)
        print(f'[{time.ctime()}] Sentiment Score: {trump_feels.sentiment.value}')

go_on = True
t = Thread(target=print_feels)
trump_feels = TweetFeels(login, tracking=['trump'])
trump_feels.start()
t.start()
print(trump_feels.sentiment.value)
#trump_feels.sentiment.value