import shutil
import time

import tqdm
import requests as requests
import json

all_cards = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
response = requests.get(all_cards)
content = json.loads(response.text).get("raw_data")



def scrap_cards():
    i = 0
    for card in tqdm.tqdm(content):
        id = card.get("id")
        image_url = f"https://images.ygoprodeck.com/images/cards/{id}.jpg"
        image = requests.get(image_url, stream=True)
        with open(f"raw_data/{id}.png", "wb") as f:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, f)
        if i % 15 == 0:
            time.sleep(1)
        i += 1
