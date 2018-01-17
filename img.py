##requires python3
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from urllib.request import urlopen
import shutil
import requests
import sys
import time
import os


 

def img_download(link):
	
	try:
		os.stat("images")
	except:
		os.mkdir("images") 

	page = requests.get( link )

	soup = BeautifulSoup(page.content, 'html.parser')
	f = open('1','wb')
	f.write(page.content)

	f.close()

	images = [img for img in soup.findAll('img')]

	##for downloading pdf external
	image_links = [each.get("src") for each in images]
	print(len(image_links))
	counter=1
	for src in image_links:
		
		try:

			response = requests.get(src, stream=True)  
			f = open("images/"+str(counter)  ,'wb')
			f.write(response.raw.read())
			f.close()
			counter=counter+1
		except:
			print ('  An error occured. Continuing.')
		print( 'Done.')





def pdf_download(link):
	try:
		os.stat("pdf_folder")
	except:
		os.mkdir("pdf_folder") 

	page = requests.get( link )

	soup = BeautifulSoup(page.content, 'html.parser')
	f = open('1','wb')
	f.write(page.content)

	f.close()

	images = [img for img in soup.findAll('a')]

	##for downloading pdf external
	image_links = [each.get("href") for each in images]

	counter=2
	for each in image_links:
		print(each)
		try:
			filename = each.strip().split('/')[-1].strip()
			src = link + each	
			if src[-1]=='p':
				continue
			print(src)
			print ('Getting: ' + filename)
			response = requests.get(src, stream=True)  
			f = open("pdf_folder/"+filename ,'wb')
			f.write(response.raw.read())
			f.close()
			counter=counter+1
		except:
			print ('  An error occured. Continuing.')
		print( 'Done.')


# here is the link for the page for pdf
#change the link for downloading pdfs
link = "http://www.cs.cmu.edu/~epxing/Class/10701-10s/HW/"
pdf_download(link)

#change the link for downloading images
link = "https://twitter.com/dishpatani"
img_download(link)



