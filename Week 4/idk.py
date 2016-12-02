
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen









def trawl(url, count,position):



	html = urllib.request.urlopen(url).read()

	soup = BeautifulSoup(html,"html.parser")


#tag.get('href',none)


	# Retrieve all of the anchor tags
	tags = soup('a')
	newurl =tags[position-1].get('href',None)
	print(newurl)

	if(count ==2):
   		return newurl

	else:
   		trawl(newurl,count-1,position)



    









url = input('Enter URL ')
count = int(input('Enter count '))
position = int(input('Enter position '))




print(trawl(url,count,position))