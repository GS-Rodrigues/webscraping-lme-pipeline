import requests
import Insert
from datetime import date
import date_treatment
from bs4 import BeautifulSoup

j = 2008

month_to_year = {
    "jan": 1,
    "fev": 2,
    "mar": 3,
    "abr": 4,
    "mai": 5,
    "jun": 6,
    "jul": 7,
    "ago": 8,
    "set": 9,
    "out": 10,
    "nov": 11,
    "dez": 12
}

while j <= date.today().year:
    i = 1;
    while i <= 12:
        if not (j == date.today().year and i > date.today().month):
            url = f"https://shockmetais.com.br/lme/{i}-{j}";
            
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
                    raw_number = colms[3].text.strip();
                    clean_number = raw_number.replace(" ", "").replace("\n", "").replace(",", "");
                    aluminium = clean_number;
                    if not ("feriado" in month_year.lower() or "Média" in month_year):
                        aluminium = float(aluminium);
                        Insert.insert_row(date_treatment.parse_data_br(month_year, j), aluminium);
            i = (i + 1);
    j = (j + 1);