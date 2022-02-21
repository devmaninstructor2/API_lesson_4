import os
from os import listdir
import random
from time import sleep

import telegram
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_last_launch_images
from fetch_nasa import fetch_nasa_apod
from fetch_nasa import fetch_nasa_epic

def send_random_pic_from_dirs(tg_token, chat_id, dirs):
    bot = telegram.Bot(token=tg_token)
    with open(get_random_pic_from_dirs(dirs), 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)

def get_random_pic_from_dirs(dirs):
    random_dir = random.choice(dirs)
    random_picture = random.choice(listdir(random_dir))
    picture_path = f'{random_dir}/{random_picture}'
    return picture_path

if __name__ == '__main__':
    load_dotenv()

    spacex_dir = '/spacex'
    apod_dir = '/nasa_apod'
    epic_dir = '/nasa_epic'

    image_dirs = [spacex_dir, apod_dir, epic_dir]

    for image_dir in image_dirs:
        os.makedirs(image_dir, exist_ok=True)

    nasa_token = os.getenv('NASA_TOKEN')
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    seconds_delay = 86400
    while True:
        fetch_spacex_last_launch_images(spacex_dir)
        fetch_nasa_epic(nasa_token, epic_dir)
        fetch_nasa_apod(nasa_token, apod_dir)
        send_random_pic_from_dirs(tg_token, tg_chat_id, image_dirs)
        sleep(seconds_delay)
