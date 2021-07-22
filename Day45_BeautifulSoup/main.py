from bs4 import BeautifulSoup
#import lxml

#read the website
with open("website.html",encoding='cp437') as f:
    contents=f.read()

soup= BeautifulSoup(contents,"html.parser")
#object then the name of the tag or string of the tag

print(soup.title.string)

# read string of a related tag

all_anchor_tag = soup.find_all(name="a")
for tag in all_anchor_tag:
    print(tag.string)