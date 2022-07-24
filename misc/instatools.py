import cgi
import datetime
import json
import os
import time

root = 'C:/inetpub/wwwroot/misc/'
got = {'data': '', 'time': ''}
try:
    for g in cgi.FieldStorage().list: got[g.name] = g.value
except:
    pass
print("Content-Type: text/plain\n")

if got['time'] == '':
    with open(root + '/instatools/errors.txt', 'a', encoding="utf-8") as f:
        writable = str(datetime.datetime.fromtimestamp(time.time())) + " (IP: " + os.environ["REMOTE_ADDR"] + ")" + '\n'
        if got['data'] != '':
            writable += got['data'] + '\n\n'
        f.write(writable)
    quit()

that_time = datetime.datetime.fromtimestamp(float(got['time'][:-3]))
with open(root + '/instatools/' + that_time.strftime("%Y%m%d_%H%M%S") +
          '_' + got['time'][-3:] + '.txt', 'w', encoding="utf-8") as f:
    f.write(got['data'])
