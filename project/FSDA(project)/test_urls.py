import urllib.request
import json

base_url = "https://images.unsplash.com/photo-{id}?w=600&auto=format&fit=crop"

candidate_ids = [
    "1582719478250-c89cae4dc85b", "1542314831-c6a4d14d8376", "1564013799919-ab600027ffc6",
    "1566665797739-1674de7a421a", "1611892440504-42a792e24d32", "1522708323590-d24dbb6b0267",
    "1590490360182-c33d57733427", "1631049307264-da0ec9d70304", "1505691938895-1758d7feb511",
    "1598928506311-c55dd58c2460", "1584622650111-993a426fbf0a", "1592229505726-ca121723b8ef",
    "1596436889106-be35e843f974", "1519999482648-25049ddd37b1", "1598928636135-d146006ff4be",
    "1560662105-57f8ad6fa545", "1574643030364-e29f37c3dafa", "1616486022830-df4f0612c98d",
    "1549488344-9f44ce2fde06", "1600109040974-9b2f6fbf0387", "1578683010236-d716f9a3f461",
    "1568941159152-ed3744a9542a", "1615460541571-7243b940a92e", "1445013115162-4c27a3ef22bd",
    "1596394511913-c7a42b9d2a0e", "1594560913095-8cf34bab82db", "1561501900-3701fa6a0864"
]

valid = []
for cid in candidate_ids:
    url = base_url.replace("{id}", cid)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req)
        if res.status == 200:
            valid.append(cid)
            if len(valid) == 20: break
    except Exception as e:
        pass

print(json.dumps(valid))
