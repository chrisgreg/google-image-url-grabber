#Google Image URL Retriever
#Author: Chris Gregori
#Date: 22/08/13

import os
import sys
import time
from urllib import FancyURLopener
from random import randint
import urllib2
import json

searchTerm = ''
searchTerm = searchTerm.replace(' ','%20')
imageList = []

def main(searchTerm = '', endRange = 5):
	count = 0

	for i in range(0,endRange):
		try:
		    # Changes for each iteration in order to request a new set of images for each loop
		    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+ searchTerm +'&start='+str(i*randint(1,50))+'&userip=MyIP')
		    request = urllib2.Request(url, None, {'Referer': 'testing'})
		    response = urllib2.urlopen(request)
	    	
		    # Get results using JSON
		    results = json.load(response)
		    data = results['responseData']
		    dataInfo = data['results']

		    # Iterate for each result and get unescaped url
		    for myUrl in dataInfo:
		        count = count + 1
		        imageUrl = myUrl['unescapedUrl']
		        print myUrl['unescapedUrl']
		        imageList.append(imageUrl)

		    # Sleep for one second to prevent IP blocking from Google
		    time.sleep(1)

		except:
			continue

if __name__=="__main__":
	main()