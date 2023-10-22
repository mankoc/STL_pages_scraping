from Scrapers import cgtrader
from Scrapers.cults import scrape_cults
from Scrapers.artstation import scrape_artstation

URL = f"https://cults3d.com/es/modelo-3d/variado/psylocke-janter"


OUTPUT_DIR="h:\\temp\\"

#with open("h:\\temp\\urls.txt", "r") as f:
#    urls=f.readlines()
urls=["https://www.cgtrader.com/3d-print-models/miniatures/figurines/andrea-pirate-girls-vol-1"]

for URL in urls:
    URL=URL.replace("\n","")

    if "cgtrader.com" in URL:
        cgtrader.scrape_cgtrader(URL, OUTPUT_DIR)
    if "cults3d" in URL:
        URL=URL.replace("https://cults3d.com/es/modelo-3d/arte/","https://cults3d.com/en/3d-model/art/")
        scrape_cults(URL,OUTPUT_DIR)
    if "artstation" in URL:
        scrape_artstation(URL, OUTPUT_DIR)
#    if "myminifactory" in URL:
#        output = scrape_myminifactory(URL, OUTPUT_DIR)



