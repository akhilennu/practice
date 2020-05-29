import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#Extracting Data from Chinese profanity
wiki_url = 'https://en.wikipedia.org/wiki/Mandarin_Chinese_profanity'
html = requests.get(wiki_url).text

soup = BeautifulSoup(html)

table = soup.select('ul')

t_headings = table[0].select('.toctext') # to extract headings

table[9].select('li')[0].select('span')[0].text.strip() # gets the first profanity word

chinese_profanity = []
for elem in table[9:68]:
  vals = elem.select('[lang|=zh]')
  for val in vals:
    chinese_profanity.append(val.text.strip())

chinese_profanity
