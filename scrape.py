from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('links.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','youtube_links'])
source = requests.get('http://coreyms.com').text

soup=BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):

#print(article.prettify())

    headline = article.h2.a.text
#print(headline)

    summary = article.find('div' , class_='entry-content').p.text
#print(summary)

    v_link = article.find('iframe' , class_= 'youtube-player')['src']
    link = v_link.split('/')
    version = link[4].split('?')
    y_link = version[0]
    y_link=f'www.youtube.com/watch?v={version[0]}'
    #print(y_link)
    csv_writer.writerow([headline,summary,y_link])
csv_file.close()