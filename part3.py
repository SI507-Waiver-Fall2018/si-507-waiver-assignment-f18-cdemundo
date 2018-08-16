#Name: Chris Demundo
#Umich ID: cdemundo

# these should be the only imports you need

import requests
from bs4 import BeautifulSoup


# write your code here
# usage should be python3 part3.py

pageAddress = 'https://www.michigandaily.com/'

def main():
	page = GetHTML(pageAddress)

	#first find the div that contains the most read articles
	if page:
		results = GetMostReadDiv(page)
	else:
		print("Couldn't get HTML from page")

	#extract and store the titles from that div
	GetArticles(results)

def GetHTML(page): 
	try: 
		page = requests.get(page)
		return page
	except requests.exceptions.RequestException as e:
		print(e)

	return none


def GetMostReadDiv(html):
	soup = BeautifulSoup(html.text, 'html.parser')

	#extract the links from the Most Read div
	mostReadDiv = soup.find("div", {"class": "view-most-read"}).find_all('a')

	return mostReadDiv


def GetArticles(resultsObj):
	#get the titles for the links
	for link in resultsObj:
		print(link.text)

		#go into the article to try to find the author for each page
		author_page = GetHTML("{basepage}{link}".format(basepage=pageAddress, link=link['href']))
		soup = BeautifulSoup(author_page.text, 'html.parser')
	
		try:
			result = soup.find("div", {"class":"byline"})
			author = result.find('div', {"class": "link"}).find('a')
			print(author.text)
		except:
			print("No author listed")

if __name__ == "__main__":
    main()