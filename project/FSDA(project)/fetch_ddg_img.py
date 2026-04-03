import urllib.request
import re
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

query = "luxury+resort+hotel+interior"
req1 = urllib.request.Request(f'https://duckduckgo.com/?q={query}&t=h_&iar=images&iax=images&ia=images', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req1, context=ctx).read().decode('utf-8')
vqd_match = re.search(r'vqd=([\d-]+)', html)
vqd = vqd_match.group(1) if vqd_match else ""

if vqd:
    req2 = urllib.request.Request(f'https://duckduckgo.com/i.js?l=us-en&o=json&q={query}&vqd={vqd}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    data = json.loads(urllib.request.urlopen(req2, context=ctx).read().decode('utf-8'))
    images = [i['image'] for i in data['results']][:40] # Need 40
    print(json.dumps(images))
else:
    print("[]")
