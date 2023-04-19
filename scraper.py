import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

x = input('What city would you like to scrape? ')
y = input('and State(In 2-letter code)?' )
z = input('and how page would you like to scrape?' )

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
]

for i in range (1,4):
    user_agent = random.choice(user_agent_list)

def extract(page):
    header = {'user-agent': user_agent}
    url = f'https://www.apartments.com/{x}-{y}/{page}'
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    li = soup.find_all('li', {'class', 'mortar-wrapper'})
    for item in li:
        title = item.find('span').text
        address = item.find('div', {'class', 'property-address js-url'}).text.strip()
        price = item.find('p', {'class', 'property-pricing'}).text
        bed = item.find('p', {'class', 'property-beds'}).text
        info = item.find('div', {'class', 'property-actions'})
        contact_info = info.find('span').text.strip()
        links = item.find('a', {'ckass', 'property-link'}).attrs['href']
        
        apartment = {
            'title': title,
            'address': address,
            'price' : price,
            'bed': bed,
            'contact-info': contact_info,
            'link': links,
        }
        unit_apartment.append(apartment)
    return

unit_apartment = []

for i in range(1,int(z)+1):
    print(f'Getting Page: {i}')
    c= extract(i)
    transform(c)

df = pd.DataFrame(unit_apartment)
df.to_csv('apartmentunit.csv')
new_df = pd.read_csv('apartmentunit.csv')

print(new_df)