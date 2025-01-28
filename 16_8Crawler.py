import urllib.request
from bs4 import BeautifulSoup
import requests

def analyze(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Chyba při stahování stránky: {url}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title is not None else "Bez titulku"

    links = [a['href'] for a in soup.find_all('a', href=True)]

    print(f"Titulek stránky: {title}")
    print(f"Počet odkazů na stránce: {len(links)}")
    return links

def main():
    main_url = 'http://vlada.cz'
    print(f"Navštěvuji hlavní stránku: {main_url}")
    links_1 = analyze(main_url)

    if links_1:
        print("\nNavštěvuji odkazy z hlavní stránky:")
        for link in links_1:
            if not link.startswith('http'):
                link = main_url + link
            print(f"\nNavštěvuji stránku: {link}")
            analyze(link)

if __name__ == '__main__':
    main()


