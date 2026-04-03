import urllib.request
import re
import json

req = urllib.request.Request("https://picsum.photos/v2/list?page=2&limit=50", headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))

unsplash_urls = [item['url'] for item in data]
ids = []
for u in unsplash_urls:
    # URL is like https://unsplash.com/photos/G-XXzX-_0Q0
    # Wait, Picsum has older unsplash photos! Let's check format.
    # Actually, we can get download_url: https://picsum.photos/id/1020/4288/2848
    # That doesn't give us the Unsplash ID directly. 
    pass

# Alternative: duckduckgo html search with python regex
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://html.duckduckgo.com/html/?q=site:unsplash.com+/photo-+luxury", headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req, context=ctx)
html = res.read().decode('utf-8')
matches = re.findall(r'photo-([0-9]{13}-[0-9a-f]{12}|[0-9]{10}-[0-9a-f]{12})', html)
print(json.dumps(list(set(matches))))

