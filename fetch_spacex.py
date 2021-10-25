import requests
from fetch_image import fetch_image


def fetch_spacex_last_launch_images(images_dir):
    api_spacex_url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(api_spacex_url)
    response.raise_for_status()
    flight_images = response.json()["links"]["flickr"]["original"]

    for image_num, image_url in enumerate(flight_images):
        fetch_image(image_url, images_dir, f"spacex_last_launch_{image_num}")

