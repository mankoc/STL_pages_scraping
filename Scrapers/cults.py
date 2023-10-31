import requests
from bs4 import BeautifulSoup
from utils import create_dir,clean_path
import json
import os
from os import path as op

# Press the green button in the gutter to run the script.
def scrape_cults(URL,OUTPUT_DIR):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #images=soup.find_all("div", class_="thumb-list-wrapper js-list-wrapper")
    images=soup.find("div",{"data-controller":"picker slides"}).find_all("button")

    info={
            "name": soup.find("h1",{"class":"t0"}).text.strip(),
            "author": soup.find("h3",{"class":"card__title--secondary"}).find("a").text,
            "distributor": "cults3d",
            "url": URL,
            "description": soup.find("div",{"class":"rich"}).find("p").text,
            "tags": [a.text for a in soup.find_all("a",{"rel":"tag"})]
    }

    main_dir=clean_path(os.path.join(OUTPUT_DIR,info["name"]+" - "+info["author"]))
    files_dir=os.path.join(main_dir,"Files")
    images_dir = os.path.join(main_dir, "Images")
    create_dir(main_dir)
    create_dir(files_dir)
    create_dir(images_dir)

    with open(op.join(main_dir, "INFO.json"), "w") as f:
        json.dump(info,f,indent=4)

    counter =1

    title =''.join(e for e in soup.find("title").text if e.isspace() or e.isalnum())

    with open(op.join(main_dir,f"cults - {title}.url"),"wt") as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={URL}")

    for block in images:
            image=block.find("source")
            try:
                if "srcset" in image.attrs:
                    image_link = image['srcset']
                else:
                    image_link=image['data-srcset']
                if True:
                    imfile = requests.get(image_link)
                    if imfile.ok:
                        filename = image_link.split("/")[-1]
                        spl = filename.split(".")
                        print(filename)
                        with open(op.join(images_dir,f"{spl[0]}-{counter}.{spl[1]}"),"wb") as f:
                            f.write(imfile.content)
                            counter+=1
            except Exception:
                pass
    return main_dir


