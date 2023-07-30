from requests_html import HTMLSession
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
URL = "https://www.cgtrader.com/3d-models/character/fantasy-character/blasphemous-statue-for-3d-printing"



OUTPUT_DIR="e:\\temp\\"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    session = HTMLSession()
    r = session.get(URL)
    r.html.render()

    page = r.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #images=soup.find_all("div", class_="thumb-list-wrapper js-list-wrapper")
    images=soup.find_all("img")
    counter =1

    for image in images:
            try:
                image_link= image['data-src']
                filename=image_link.split("/")[-1]
                spl=filename.split(".")
                imfile=requests.get(image_link)
                if imfile.ok:
                    with open(f"{OUTPUT_DIR}{spl[0]}-{counter}.{spl[1]}","wb") as f:
                        f.write(imfile.content)
                    counter+=1

                kkk=0
            except Exception:
                pass



