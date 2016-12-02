import urllib
from urllib.request import urlopen
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_303389.xml'





uh = urllib.request.urlopen(serviceurl)
data = uh.read()

tree = ET.fromstring(data)


results = tree.findall('.//count')


totalsum=0

for i in results:
    totalsum+=int(i.text)


print(totalsum)

 