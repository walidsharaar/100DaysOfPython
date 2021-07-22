from bs4 import BeautifulSoup
import requests

reponse = requests.get("https://news.ycombinator.com/")
web_page = reponse.text

soup = BeautifulSoup(web_page,"html.parser")
articles= soup.find_all(name="a" ,class_="storylink")
article_texts=[]
article_link=[]
for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.get("href")
    article_link.append(link)

article_upvotes= [score.getText for score in soup.find_all(name="span",class_="score")]


print(text)
print(link)
print(article_upvotes)
