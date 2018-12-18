from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def home(request):
	return render(request , "home.html")


def scrap(request):
	url = request.GET.get("website")               # getting the URL from homepage
	r = requests.get(url)                          # fetching up the content by requesting
	soup = BeautifulSoup(r.content , features="lxml")  #applying beautifulsoup method and declaring parser(lxml)

	#creating a empty list to pass the data into template easily
	alist = []

	h1 = soup.find_all("h1")
	h2 = soup.find_all("h2")
	h3 = soup.find_all("h3")
	h4 = soup.find_all("h4")
	h5 = soup.find_all("h5")
	h6 = soup.find_all("h6")
	h7 = soup.find_all("h7")

	 # making a list of certain tags to loop over
	alist_1 = [h1 , h2 , h3 , h4 , h5 , h6 , h7]   

	# filling up the main list which passes the data into template
	for git in alist_1:
		for lit in git:
			alist.append(lit.text)


	# logic for fetching up the paragraphs from the web page
	para = []
	ara = soup.find_all("p")
	
	for j in ara:
		para.append(j.text)

	#passing the two lists for headlines and paragraphs respectively
	context = {
	"alist":alist,
	"para":para

	}
	return render(request , "scrap.html" , context)