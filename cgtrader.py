import requests
from bs4 import BeautifulSoup
from utils import create_dir
from io import BytesIO
import json
import os


# Press the green button in the gutter to run the script.
def scrape_cgtrader(URL,OUTPUT_DIR):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #images=soup.find_all("div", class_="thumb-list-wrapper js-list-wrapper")
    images=soup.find("div", class_="product-carousel__thumbs").find_all("img")

    counter =1

    info={
            "name": soup.find("h1",{"class":"product-header__title", "itemprop":"name"}).text.strip(),
            "author": soup.find("div",{"class":"username"}).text,
            "distributor": "cgtrader",
            "url": URL,
            "description": soup.find("div",{"class":"product-description"}).find("p").text,
            "tags": [a.text for a in soup.find_all("li",{"class":"label"})]
    }

    main_dir=os.path.join(OUTPUT_DIR,info["name"]+" - "+info["author"])
    files_dir=os.path.join(main_dir,"Files")
    images_dir = os.path.join(main_dir, "Images")
    create_dir(main_dir)
    create_dir(files_dir)
    create_dir(images_dir)

    title =''.join(e for e in soup.find("title").text if e.isspace() or e.isalnum())
    with open(os.path.join(main_dir,f"{title}.url"),"wt") as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={URL}")
    with open(os.path.join(main_dir,f"INFO.json"),"w") as f:
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



