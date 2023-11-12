import requests
from bs4 import BeautifulSoup
from utils import create_dir,clean_tags,clean_useless_names,clean_path
from io import BytesIO
import json
import os
from pathlib import Path

# Press the green button in the gutter to run the script.
def scrape_cgtrader(URL,OUTPUT_DIR):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #images=soup.find_all("div", class_="thumb-list-wrapper js-list-wrapper")
    images=soup.find("div", class_="product-carousel__thumbs").find_all("img")

    counter =1
    model_name= clean_useless_names(soup.find("h1",{"class":"product-header__title", "itemprop":"name"}).text.strip())
    info={
            "name": model_name,
            "author": soup.find("div",{"class":"username"}).text,
            "distributor": "cgtrader",
            "url": URL,
            "description": clean_tags(soup.find("div",{"class":"product-description"}).text),
            "tags": [a.text for a in soup.find_all("li",{"class":"label"})]
    }
    main_dir=Path(OUTPUT_DIR) / (info["name"]+" - "+info["author"])
    #main_dir=clean_path(os.path.join(OUTPUT_DIR,info["name"]+" - "+info["author"]))
    files_dir=os.path.join(main_dir,"Files")
    images_dir = os.path.join(main_dir, "Images")
    create_dir(main_dir)
    create_dir(files_dir)
    create_dir(images_dir)

    title =''.join(e for e in soup.find("title").text if e.isspace() or e.isalnum())

    with open(os.path.join(main_dir,f"{title}.url"),"wt") as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={URL}")

    with open(os.path.join(main_dir, f"INFO.json"), "w") as f:
        json.dump(info,f,indent=4)

    for image in images:
            try:
                image_link= image['data-src']
                image_link=image_link.replace("_xs","")
                if True:
                    if True:
                        imfile = requests.get(image_link)
                        if imfile.ok:
                            filename = image_link.split("/")[-1]
                            spl = filename.split(".")
                            print(filename)
                            with open(os.path.join(images_dir,f"{spl[0]}-{counter}.{spl[1]}"),"wb") as f:
                                f.write(imfile.content)
                                counter+=1
            except Exception:
                pass
    return OUTPUT_DIR



