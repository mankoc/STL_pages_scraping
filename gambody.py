import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
from PIL import Image
from io import BytesIO
import json
OUTPUT_DIR="h:\\temp\\GB Imgs"
import re

def get_images(soup, out_dir,model_id):
    output_path = out_dir / "Images"
    output_path.mkdir(parents=True, exist_ok=True)
    #images=soup.find_all("div")#, class_= "slick-slide slick-current slick-active")
    imgprv=soup.find_all("div", {'data-image-url': True} )

    for image in imgprv:
        kkk=0
        try:
            image_link= image['data-image-url'].replace("_xs","")
            filename=image_link.split("/")[-1]
            spl=filename.split(".")
            # if spl[1]=='png' and "x" in spl[0]:
            if True:
                imfile=requests.get(image_link)
                if imfile.ok:
                    with open(output_path/f"{model_id} - {spl[0]}.{spl[1]}","wb") as f:
                        f.write(imfile.content)
        except Exception:
            pass

def write_url(out_dir,title,URL):
    with open(out_dir/f"{title}.url","wt") as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={URL}")

def write_info(out_dir, soup,row):
    info_file=out_dir / "INFO.txt"
    info_json=out_dir / "INFO.json"
    with open(info_file,"wt",encoding="utf-8") as f:

        author=soup.find_all("div", class_="dnamePrt")
        author2=author[0].find('a').get_text()
        f.write(f"Author: \n{author2.strip()}\n\n")
        f.write(f"Url: \n{row.link}\n\n")

        description = soup.find("div", {"id": "description-block"}).get_text()
        f.write("Description:")
        f.write(description)
        f.write("\nTags:\n")
        tags=soup.find("p",class_="cloudTags").get_text().split(',')
        for tag in tags:
            f.write(tag.strip()+"\n")
        f.write("\n")
    output_json={
        "name": re.sub('[^\w\-_\. ]', '_', row.title.split(" 3D")[0]),
        "author": author2,
        "distributor": "Gambody",
        "url": row.link,
        "description": description.strip(),
        "tags": [x.strip() for x in tags]
    }
    with open(info_json,"wt", encoding='utf-8') as f:
        json.dump(output_json, f, indent=4,ensure_ascii=False)


def process_row():
    model_id = f"{row.id:04d}"
    model_name = re.sub('[^\w\-_\. ]', '_', row.title.split(" 3D")[0])
    out_dir = path / f"{model_id} - {model_name.strip()}"
    infoname = out_dir / "INFO.txt"
    if infoname.is_file():
        print(f"{out_dir} existe")
    else:
        model_url = row.link

        page = requests.get(model_url)
        soup = BeautifulSoup(page.content, "html.parser")

        print(f"Processing {out_dir}")
        get_images(soup, out_dir, model_id)
        write_url(out_dir, model_name, model_url)
        write_info(out_dir, soup, row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = Path(OUTPUT_DIR)
    list_file=pd.read_csv("f:\\STL\\08 - Gambody\\products.txt",sep='\t')

    for i,row in list_file.iterrows():
        process_row()
        kk=0



