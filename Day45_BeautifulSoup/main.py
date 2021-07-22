from bs4 import BeautifulSoup
#import lxml

#read the website
with open("website.html",encoding='cp437') as f:
    contents=f.read()

soup= BeautifulSoup(contents,"html.parser")
#object then the name of the tag or string of the tag

print(soup.title.string)
