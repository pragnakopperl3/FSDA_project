import urllib.request
import re
import json

url = "https://unsplash.com/s/photos/resort"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
})
try:
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    matches = re.findall(r'photo-([0-9]{10,13}-[0-9a-f]{12}|[a-zA-Z0-9]{11})', html)
    valid = list(set([m for m in matches if '-' in m]))
    print(json.dumps(valid[:25]))
except BaseException as e:
    print(e)
