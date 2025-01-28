import urllib.request
from http.client import responses

from bs4 import BeautifulSoup

url = 'http://vlada.cz'

response = urllib.request.urlopen(url)
html_content = response.read()
soup = BeautifulSoup(html_content, 'html.parser')

title = soup.title.string
print("Titulek stranky:", title)

print("\nNadpisy H1:")
for h1 in soup.find_all('h1'):
    print(h1.get_text())

print("\nNadpisy H2:")
for h2 in soup.find_all('h2'):
    print(h2.get_text())

print("\nURL adresy odkazů:")
for link in soup.find_all('a', href=True):
    print(link['href'])