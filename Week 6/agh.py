import urllib

from urllib.request import urlopen
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_303393.json'





uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode("utf-8") 


info = json.loads(data)

commentlist = info['comments']
totalsum=0

for i in commentlist:
    totalsum+=int(i["count"])


print(totalsum)

 