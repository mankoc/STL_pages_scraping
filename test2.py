from requests import get as GET
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15'
}
with GET('https://www.artstation.com/projects/39L94v.json', headers=HEADERS) as response:
    response.raise_for_status()