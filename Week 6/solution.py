import urllib
import urllib.request
import urllib.parse
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
 
    uh = urllib.request.urlopen(url)
    data = uh.read().decode('utf-8')
 

   



    try: js = json.loads(data)
    except: js = None
 


    placeid = js["results"][0]["place_id"]
    print(placeid)

