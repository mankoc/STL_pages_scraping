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
def scrape_myminifactory(URL,OUTPUT_DIR):

    code=URL.split("-")[-1]
    url=f"https://www.myminifactory.com/api/v2/objects/{code}"


    with open("myminifactory_session.txt","rt") as f:
        sess=f.read()
    cookies={"SESSID":sess}

    #TODO: check session response.
    response = requests.get(url,cookies=cookies).json()

    info = {
        "name": response["name"],
        "author": response["designer"]["username"],
        "distributor": "MyMiniFactory",
        "url": URL,
        "description": clean_tags(response["description"]),
        "tags": response["tags"]
    }

    main_dir = sanitize_filepath(os.path.join(OUTPUT_DIR, clean_path(f'{info["name"]} - {info["author"]}')))
    files_dir = os.path.join(main_dir, "Files")
    images_dir = os.path.join(main_dir, "Images")
    create_dir(main_dir)
    create_dir(files_dir)
    create_dir(images_dir)

    with open(os.path.join(main_dir, f"INFO.json"), "w") as f:
        json.dump(info, f, indent=4)

    write_url(main_dir,info)

    for img in response["images"]:
        image_link=img["large"]["url"]
        imfile=requests.get(image_link,cookies=cookies)
        if imfile.ok:
            filename = image_link.split("?")[0].split("/")[-1]
            spl = filename.split(".")
            print(filename)
            with open(sanitize_filepath(os.path.join(images_dir, f"{spl[0]}.{spl[1]}")), "wb") as f:
                f.write(imfile.content)
    return main_dir