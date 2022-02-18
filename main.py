#If you want to scrap a website:
#1. Use the API
#3. HTML Web Scrapping using some tool like bs4.

#Step 0:Install all the requirements
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#Step 1: Get the HTML
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

#Step2:Parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

#Step3: HTML free traversal
#Commonly used types of objectsL
#print(type(title)) #1.Tag
#print(type(title.string)) #2.Navigable String
#print(type(soup)) #3.Beautiful Soup
#4.Comment
markup="<p><!--this is a comment--></p>"
soup2=BeautifulSoup(markup)
#print(soup2)
#print(soup2.p)
#print(soup2.p.string)
#print(type(soup2.p.string))
#exit()


#Get the title of the HTML page
title=soup.title

#get all the paraghs from the page
paras=soup.find_all('p')
#print(paras)

#get all the anchor tags from the page
anchors=soup.find_all('a')
all_links=set()
#print(anchors)

#get all the links on the page
for link in anchors:
    if(link.get('href')!='#'):
        linkText="https://codewithharry.com"+link.get('href')
        all_links.add(link)
        #print(linkText)

#print(soup.find('p')) #get first element in the html page
#print(soup.find('p')['class']) #get classes of any element in the html page

#find all the elements with class lead
#print(soup.find_all("p", class_="lead"))

#get the text from the tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())

#.contents: A tag's children are avaialble as a list.
#.children: A tag's children are avaialble as a generator. 
navbarSupportedContent=soup.find(id='navbarSupportedContent')
#for elem in navbarSupportedContent.contents:
    #print(elem)

#for item in navbarSupportedContent.stripped_strings:
    #print(item)

#for item in navbarSupportedContent.stripped_strings:
    #print(item)

#print(navbarSupportedContent.parent)
#for item in navbarSupportedContent.parents:
    #print(item.name)

#print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

#elem=soup.select('#loginModal')
#print(elem)

#elem=soup.select('.loginModal')
#print(elem)

elem=soup.select('.modal-footer')
print(elem)