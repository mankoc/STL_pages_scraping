import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

model_name="b1-battle-droid"
URL = f"https://www.gambody.com/3d-models/{model_name}"

OUTPUT_DIR="h:\\temp\\"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #images=soup.find_all("div", class_="thumb-list-wrapper js-list-wrapper")
    images=soup.find_all("img")
    counter =1

    title =''.join(e for e in soup.find("title").text if e.isspace() or e.isalnum())
    with open(f"{OUTPUT_DIR}{title}.url","wt") as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={URL}")

    for image in images:
            try:
                image_link= image['src']
                image_link=image_link.replace("_xs","")
                if "https://www.gambody.com/storage" in image_link:
                    # if model_name in image_link:
                    if True:
                        imfile = requests.get(image_link)
                        if imfile.ok:
                            filename = image_link.split("/")[-1]
                            spl = filename.split(".")
                            print(filename)
                            with open(f"{OUTPUT_DIR}{spl[0]}.{spl[1]}","wb") as f:
                                f.write(imfile.content)
            except Exception:
                pass



