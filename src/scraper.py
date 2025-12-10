import requests
import Insert
from datetime import date
import date_treatment
from bs4 import BeautifulSoup

url = f"https://shockmetais.com.br/lme/{date.today().month}-{date.today().year}";

response = requests.get(url);

html_content = response.content;


soup = BeautifulSoup(html_content, 'html.parser');

table = soup.find_all(
    name='table',
    attrs= {'class' : 'table table-hover table-sm table-striped shadow'}
)[0];


for row in table.find_all('tr')[1:-1]:
    colms = row.find_all('td');
    if colms:
        month_year = colms[0].text.strip();
        raw = colms[3].text.strip()
        clean = raw.replace(" ", "").replace("\n", "").replace(",", "").replace(",", ".")
        aluminium = float(clean)
        
        if "Média" in month_year:
            continue;
        else:
            Insert.insert_row(date_treatment.parse_data_br(month_year, date.today().year), aluminium);