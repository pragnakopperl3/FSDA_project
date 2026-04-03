import urllib.request
import re
import json
import time

url = "https://html.duckduckgo.com/html/?q=site:unsplash.com/photos/+luxury+hotel"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
try:
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    matches = re.findall(r'unsplash\.com/photos/.*?([a-zA-Z0-9]{11,12}|[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+)', html)
    valid = list(set([m for m in matches if '-' in m or len(m) >= 11]))
    print(json.dumps(valid))
except Exception as e:
    print("Error:", e)
