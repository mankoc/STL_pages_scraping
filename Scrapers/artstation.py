import requests
from bs4 import BeautifulSoup
from utils import create_dir
import json
import os
from os import path as op
import urllib
from utils import clean_tags,write_url,clean_path
from pathvalidate import sanitize_filepath


# Press the green button in the gutter to run the script.
def scrape_artstation(URL,OUTPUT_DIR):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}  # This is chrome, you can set whatever browser you like

    ID=URL.split("/")[-1]


    url=f"https://www.artstation.com/projects/{ID}.json"
    response = requests.get(url,headers=headers).json()

    info = {
        "name": response["title"],
        "author": response["user"]["full_name"],
        "distributor": "Artstation",
        "url": URL,
        "description": clean_tags(response["description"]),
        "tags": response["tags"]
    }

    main_dir = clean_path(os.path.join(OUTPUT_DIR, f'{info["name"]} - {info["author"]}'))
    files_dir = os.path.join(main_dir, "Files")
    images_dir = os.path.join(main_dir, "Images")
    create_dir(main_dir)
    create_dir(files_dir)
    create_dir(images_dir)

    with open(os.path.join(main_dir, f"INFO.json"), "w") as f:
        json.dump(info, f, indent=4)

    write_url(main_dir,info)

    for img in response["assets"]:
        image_link=img["image_url"]
        imfile=requests.get(image_link,headers=headers)
        if imfile.ok:
            filename = image_link.split("?")[0].split("/")[-1]
            spl = filename.split(".")
            print(filename)
            with open(sanitize_filepath(os.path.join(images_dir, f"{spl[0]}.{spl[1]}")), "wb") as f:
                f.write(imfile.content)
    return main_dir