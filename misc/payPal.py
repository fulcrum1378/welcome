# -*- coding: utf-8 -*-
import urllib3

print("Content-Type: text/plain\n")
urllib3.util.make_headers(disable_cache=True)
raw = str(urllib3.PoolManager().request('GET', 'https://www.paymentstate.com/charge-account-paypal/')
          .data.decode('utf-8'))
area = raw[raw.index("id=\"vl\""):]
area = area[(area.find('\">') + 3):]
area = area[:area.find('</select>')]

eve = {"دلار": "USD", "یورو": "EUR", "پوند": "GBP"}
cur = area.split('<option')[1:]
for x in range(len(cur)):
    cur[x] = cur[x][:cur[x].find("</option>")]
    this = None
    for z in eve.keys():
        if z in cur[x]:
            this = eve[z]
    price = cur[x][(cur[x].find('value=\"') + 7):]
    price = price[:price.find('\"')]
    print(this, "=>", price)
