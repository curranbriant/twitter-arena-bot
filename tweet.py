import os
import datetime
from time import sleep
import requests
from twython import Twython
from io import BytesIO
from arena import Arena
from credentials import ARENA_ACCESS_KEY, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
arena = Arena(ARENA_ACCESS_KEY)

chan = arena.channels.channel('Your-channel-url')

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
twitter.verify_credentials()
items, page = chan.contents()
for x in items:
    try:
        image = x.image['original']
        url = image['url']
        response = requests.get(url)
        photo = BytesIO(response.content)
        response = twitter.upload_media(media=photo)
        twitter.update_status(media_ids=[response['media_id']])
        print("tweeted!")
        chan.remove_block(x.id)
        sleep(600)

    except Exception as e:
        print("encountered error! error deets: %s"%str(e))
        sleep(10)

