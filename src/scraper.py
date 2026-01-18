import requests
import Insert
from datetime import date
import date_treatment
from bs4 import BeautifulSoup


for j in range(date.today().year-1, date.today().year+1):
    for i in range(1, 13):
        if j == date.today().year and i > date.today().month:
            continue;

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
                if not "feriado" in month_year.lower() and not "Média" in month_year:
                    try:
                        date_clean = date_treatment.parse_data_br(month_year, j);
                        if date_clean.month == i:
                            aluminium = float(aluminium);
                            Insert.insert_row(date_clean, aluminium);
                    except ValueError:
                        continue
        i = (i + 1);
    j = (j + 1);