import urllib

url = 'http://vlada.cz'

response = urllib.request.urlopen(url)

html_content = response.read().decode('utf-8')
print(html_content)