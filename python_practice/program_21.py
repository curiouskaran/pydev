#python practice - program_21.py
__author__ = 'karan sharma'

'''Take the code from the How To Decode A Website exercise (if you didnt do it or just want to play with some different code,
use the code from the solution), and instead of printing the results to a screen, write the results to a txt file.
In your code, just make up a name for the file you are saving to.'''

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,'lxml')

#clearing file every time
with open('nytimes.txt','w') as open_file:
    open_file.write("")

#writing required contents to file
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        with open('nytimes.txt','a') as open_file:
            s = story_heading.a.text.replace("\n", " ").strip().encode("utf-8")
            open_file.write(s)
    else:
        with open('nytimes.txt','a') as open_file:
            r = story_heading.contents[0].strip().encode("utf-8")
