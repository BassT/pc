5##follow the chain
##chain: an url ...?nothing=SomeNumber contains one line 'and the next nothing is NextNumber'
##Hint: DON'T TRY ALL NOTHINGS, since it will never 
##end. 400 times is more than enough. 
##
##Request urls one after the other, if there's something else written than the phrase --> halt, output

import urllib.request
import re

response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")

for i in range(400):
	body = response.read().decode()
	print(body)
	number = re.findall("and the next nothing is ([0-9]{1,5})", body)
	print(number)
	if number != None:
		print("calling: " + "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number[0])
		response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number[0])
