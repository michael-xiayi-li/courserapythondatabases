
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")


intlist=[]
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   intlist.append(int(tag.contents[0]))
    

sum=0


for num in intlist:
	sum+=num


print(sum)