import urllib.request
import urllib.parse
import re
import json

url = "https://html.duckduckgo.com/html/?q=site:images.unsplash.com/photo+-premium+luxury+hotel"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    # DuckDuckGo links are like: /l/?uddg=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1542314831-c6a4d14d8376
    decoded = urllib.parse.unquote(html)
    matches = re.findall(r'images\.unsplash\.com/photo-([0-9]{10,13}-[0-9a-f]{12}|[A-Za-z0-9_-]{11})\b', decoded)
    valid = list(set([m for m in matches if '-' in m]))
    print("Found IDs:")
    print(json.dumps(valid[:60]))
except Exception as e:
    print(e)
