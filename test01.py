import requests
from bs4 import BeautifulSoup


url = requests.get('https://dolarhoje.com/')



soup = BeautifulSoup(url.text,'lxml')

test = soup.find(id='nacional')

print(test.get('value'))
