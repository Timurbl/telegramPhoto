# Сделано с помощью https://habr.com/ru/post/457078/

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon import TelegramClient, sync
from config import *
from utils import *
from datetime import datetime
import time


client = TelegramClient('session', api_id, api_hash)
client.start()

prev_update_time = ""

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = time_image_name(datetime.now())
        print(prev_update_time)
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time_images/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file))
        time.sleep(30)

if __name__ == '__main__':
    pass
