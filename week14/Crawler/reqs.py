import requests
import json
from bs4 import BeautifulSoup


resp = requests.get('http://register.start.bg')
encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '')\
        .lower() else None
soup = BeautifulSoup(resp.content, from_encoding=encoding)


links = []
servers = {}
for link in soup.find_all('a', href=True):
    if link['href'].startswith("link."):
        string = "http://register.start.bg/"
        link['href'] = string + link['href']
    if link['href'].startswith("http://register.start.bg/link."):
        try:
            print(link['href'])
            server = requests.get(link['href']).headers['Server']
            if server not in servers.keys():
                servers[server] = 1
            else:
                servers[server] += 1
        except:
            print("Can't open!")

with open('stat.json', 'w') as f:
    f.write(json.dumps(servers))
