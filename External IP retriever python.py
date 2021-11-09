import urllib.request
import re

url = "http://checkip.dyndns.org"
print (url,"Has been accessed to retrieve your IP address: ")


request = urllib.request.urlopen(url).read()
## print ("\nRaw request with external IP: \n", request) ##

IPadd = str(request)
IPadd = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", IPadd) ## searches for 4 sets of digits (\d) that is in a form of between 1-3 digits in one line (\b) ##
print ("\nExternal IP Address: ", IPadd)