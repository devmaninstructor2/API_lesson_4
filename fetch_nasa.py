import requests

from fetch_image import fetch_image

def fetch_nasa_epic(token, images_dir):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': token}

    response = requests.get(epic_url, params=payload)
    response.raise_for_status()
    epici_images = response.json()

    for image_num, image in enumerate(epici_images[:10]):
        image_name = image['image']
        image_date = image['date'][:10].replace('-', '/')
        image_url = 'https://api.nasa.gov/EPIC/'\
                    f'archive/natural/{image_date}/'\
                    f'png/{image_name}.png'
        fetch_image(image_url, images_dir, f'nasa_epic_{image_num}', payload)


def fetch_nasa_apod(token, images_dir):
    apod_url = f'https://api.nasa.gov/planetary/apod'
    payload = {'count': 30, 'api_key': token}

    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    apod_images = response.json()

    for image_num, image in enumerate(apod_images):
        fetch_image(image['url'], images_dir, f'nasa_apod_{image_num}', payload)

