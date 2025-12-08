import requests
from bs4 import BeautifulSoup

url = 'https://shockmetais.com.br/lme';

response = requests.get(url);

html_content = response.content;


soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find_all(
    name='table',
    attrs= {'class' : 'table table-hover table-sm table-striped shadow'}
)[0]


lme_data = {}
for row in table.find_all('tr')[1:-2]:
    colms = row.find_all('td')
    if colms:
        month_year = colms[0].text.strip()
        aluminium = colms[3].text.strip().replace('\n', '').replace(' ', '');
        lme_data.update({month_year:aluminium})

for key, value in lme_data.items():
    print(key, value)