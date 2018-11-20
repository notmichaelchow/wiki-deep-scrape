# how many nested links to traverse to get to United States wikipedia from a random wikipedia page

import random
import time
import requests
from bs4 import BeautifulSoup



set_of_links = set()

def getlink(hyperlink):
	page = ''
	while page == '':
	    try:
	        response = requests.get(hyperlink)
	        break
	    except:
	        print("Connection refused by the server..")
	        print("Let me sleep for 15 seconds")
	        print("ZZzzzz...")
	        time.sleep(15)
	        print("Was a nice sleep, now let me continue...")
	        continue

	soup = BeautifulSoup(response.text, 'html.parser')

	# build list of links
	links = []
	for link in soup.findAll('a'):
		hrefs = link.get('href')
		links.append(hrefs)

	# remove Nonetype
	filteredlinks = list(filter(None, links))


	# build list of indices of link with 'United' in it
	indices = []
	for i, elem in enumerate(filteredlinks):
	    if 'United_States' in elem:
	        indices.append(i)

	count = 0
	length_of_indices = len(indices)
	# if list of indices is not empty, return first viable link
	if indices != []:
		while "/wiki/" not in filteredlinks[indices[count]] or ":" in filteredlinks[indices[count]] or "(" in filteredlinks[indices[count]] or "wikimedia" in filteredlinks[indices[count]] or "Taxonomy_" in filteredlinks[indices[count]] or "Verifiability" in filteredlinks[indices[count]] or "disambiguation" in filteredlinks[indices[count]] or "#cite" in filteredlinks[indices[count]] or "p-search" in filteredlinks[indices[count]] or "action=edit" in filteredlinks[indices[count]]:
			count += 1
	if length_of_indices > count:
		if filteredlinks[indices[count]] not in set_of_links:
			set_of_links.add(filteredlinks[indices[count]])
			return "https://en.wikipedia.org" + filteredlinks[indices[count]]
		else:
			while filteredlinks[indices[count]] in set_of_links:
				count += 1
		return filteredlinks[indices[count]]

	else:
		# filter through list of links for usable link
		maxlength = len(filteredlinks) // 2.6
		counter = random.randint(0, maxlength - 1)
		while "/wiki/" not in filteredlinks[counter] or "wikimedia" in filteredlinks[counter] or "portal" in filteredlinks[counter] or ":" in filteredlinks[counter] or "(" in filteredlinks[counter] or "Taxonomy_" in filteredlinks[counter] or "Verifiability" in filteredlinks[counter] or "#cite" in filteredlinks[counter] or "disambiguation" in filteredlinks[counter] or "p-search" in filteredlinks[counter] or "action=edit" in filteredlinks[counter]:
			counter = random.randint(0, maxlength - 1)

	# return random link 
	return "https://en.wikipedia.org" + filteredlinks[counter]


def find_US():
	counter = 0
	title = "no"
	link = "https://en.wikipedia.org/wiki/Special:Random"
	while title != "https://en.wikipedia.org/wiki/United_States":
		counter += 1
		title = getlink(link)
		print(title)
		link = title

	print("\n \n \nI have found United States in ", counter - 1, " tries!")


find_US()
