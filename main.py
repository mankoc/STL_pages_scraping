import cgtrader
from cults import scrape_cults

URL = f"https://cults3d.com/en/3d-model/game/panam-palmer-cyberpunk-2077"

OUTPUT_DIR="h:\\temp\\"

if "cgtrader.com" in URL:
    cgtrader.scrape_cgtrader(URL,OUTPUT_DIR)
if "cults3d" in URL:
    URL=URL.replace("https://cults3d.com/es/modelo-3d/arte/","https://cults3d.com/en/3d-model/art/")
    scrape_cults(URL,OUTPUT_DIR)