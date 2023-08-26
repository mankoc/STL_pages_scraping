import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import json

model_name="b1-battle-droid"
URL = f"https://cults3d.com/es/modelo-3d/arte/wolverine-jonatanvogel"

OUTPUT_DIR="h:\\temp\\"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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

    with open(f"{OUTPUT_DIR}INFO.json","w") as f:
        json.dump(info,f,indent=4)

    counter =1

    title =''.join(e for e in soup.find("title").text if e.isspace() or e.isalnum())
    with open(f"{OUTPUT_DIR}{title}.url","wt") as f:
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
                        with open(f"{OUTPUT_DIR}{spl[0]}-{counter}.{spl[1]}","wb") as f:
                            f.write(imfile.content)
                            counter+=1
            except Exception:
                pass



