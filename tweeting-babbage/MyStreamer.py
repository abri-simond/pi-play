### CAMERA MODULE ###
from picamera import PiCamera
from time import sleep
from twython import Twython, TwythonStreamer
import datetime


camera = PiCamera()

def take_and_post_picture_to_twitter():
    today = datetime.datetime.now()
    filename = 'pictures/' + today.strftime("bilde_%Y-%m-%d %H:%M:%S.jpg")
    camera.capture(filename)
    message = today.strftime("Bilde tatt med Bringebaret %d %b %Y %H:%M:%S")
    with open(filename, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)
    print("Picture taken and uploaded to twitter")

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if "text" in data:
            take_and_post_picture_to_twitter()


from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )



stream.statuses.filter(track="#raspberrycam")
