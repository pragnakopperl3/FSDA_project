import urllib.request
import re
import json

url = "https://unsplash.com/s/photos/luxury-hotel"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')

# Find patterns like photo-1512345678901-abcdef123456
# Unsplash IDs are typically 11 to 24 chars, e.g., 1582719478250-c89cae4dc85b
matches = re.findall(r'photo-([0-9]{10,13}-[a-f0-9]{12})', html)
# unique and valid
valid = list(set(matches))
print(json.dumps(valid[:20]))
