#pip install beautifulsoup4
#pip install requests

import pprint
import requests
from bs4 import BeautifulSoup
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text)
#to clean the html
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
votes2 = soup2.select('.score')
subtext2 = soup2.select('.subtext')

mega_links = links + links2 
mega_votes = votes + votes2
mega_subtext = subtext + subtext2

# votes = [int(score.getText().split()[0]) for score in votes]
# print(votes)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
        
pprint.pprint(sort_stories_by_votes(create_custom_hn(mega_links, mega_subtext)))

#go to documentation to see how to use the find_all method with different tags
# print(soup.find_all('a'))
# print(soup.find_all('p'))
# print(soup.find_all('div'))
# print(soup.find_all('div'))
# print(soup.select('.score')) #selects all the elements with the class score
# print(soup.select('#score_28297244')) #selects the element with the id score_28297244





