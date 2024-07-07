import requests
from bs4 import BeautifulSoup
from utils import create_dir
import json
import os
from os import path as op
import urllib
from utils import clean_tags,write_url,clean_path
from pathvalidate import sanitize_filepath
from pathlib import Path

# Press the green button in the gutter to run the script.
def scrape_artstation(URL,OUTPUT_DIR):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
        "__cf_bm": "hGaKfxtgYfhsmUrFKcvsE8W6CStKQSBwY1pj4VGcqok - 1716544879 - 1.0.1.1 - NpjfsI_hdapyeaC7i79wvtvQHAOx3ZjqeKrohJQe57HhREwt_KzIEHYnyDGYSWfCIJ3gY_TzCrkk5BqaO7V9yz_FcyO_.seSnCx4chsQOvY"
    }
    cookies=__cf_bm={"__cf_bm":"hGaKfxtgYfhsmUrFKcvsE8W6CStKQSBwY1pj4VGcqok-1716544879-1.0.1.1-NpjfsI_hdapyeaC7i79wvtvQHAOx3ZjqeKrohJQe57HhREwt_KzIEHYnyDGYSWfCIJ3gY_TzCrkk5BqaO7V9yz_FcyO_.seSnCx4chsQOvY; Path=/; Domain=artstation.com; Secure; HttpOnly; Expires=Fri, 24 May 2024 10:31:19 GMT;"}
    ID=URL.split("/")[-1]


    url=f"http://www.artstation.com/projects/{ID}.json"
    return url
    # payload = {}
    # headers = {
    #     'Cookie': '__cf_bm=hGaKfxtgYfhsmUrFKcvsE8W6CStKQSBwY1pj4VGcqok-1716544879-1.0.1.1-NpjfsI_hdapyeaC7i79wvtvQHAOx3ZjqeKrohJQe57HhREwt_KzIEHYnyDGYSWfCIJ3gY_TzCrkk5BqaO7V9yz_FcyO_.seSnCx4chsQOvY'
    # }
    #
    # resp = requests.request("GET", url, headers=headers, data=payload)
    #
    #
    # response=resp.json()
    #
    # info = {
    #     "name": response["title"],
    #     "author": response["user"]["full_name"],
    #     "distributor": "Artstation",
    #     "url": response["permalink"],
    #     "description": clean_tags(response["description"]),
    #     "tags": response["tags"]
    # }
    #
    # main_dir=Path(OUTPUT_DIR) / (info["name"].replace("/",",")+" - "+info["author"]).replace('"','')
    # files_dir = os.path.join(main_dir, "Files")
    # images_dir = os.path.join(main_dir, "Images")
    # create_dir(main_dir)
    # create_dir(files_dir)
    # create_dir(images_dir)
    #
    # with open(os.path.join(main_dir, f"INFO.json"), "w") as f:
    #     json.dump(info, f, indent=4)
    #
    # write_url(main_dir,info)
    #
    # for img in response["assets"]:
    #     image_link=img["image_url"]
    #     imfile=requests.get(image_link,headers=headers)
    #     if imfile.ok:
    #         filename = image_link.split("?")[0].split("/")[-1]
    #         spl = filename.split(".")
    #         print(filename)
    #         with open(sanitize_filepath(os.path.join(images_dir, f"{spl[0]}.{spl[1]}")), "wb") as f:
    #             f.write(imfile.content)
    # return main_dir

def scrape_artstation_json(json_str,OUTPUT_DIR):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
        "__cf_bm": "hGaKfxtgYfhsmUrFKcvsE8W6CStKQSBwY1pj4VGcqok - 1716544879 - 1.0.1.1 - NpjfsI_hdapyeaC7i79wvtvQHAOx3ZjqeKrohJQe57HhREwt_KzIEHYnyDGYSWfCIJ3gY_TzCrkk5BqaO7V9yz_FcyO_.seSnCx4chsQOvY"
    }
    response=json.loads(json_str)
    info = {
        "name": response["title"],
        "author": response["user"]["full_name"],
        "distributor": "Artstation",
        "url": response["permalink"],
        "description": clean_tags(response["description"]),
        "tags": response["tags"]
    }

    main_dir=Path(OUTPUT_DIR) / (info["name"].replace("/",",")+" - "+info["author"]).replace('"','')
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