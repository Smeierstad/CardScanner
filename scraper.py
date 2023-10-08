import requests
from bs4 import BeautifulSoup
import pickle

url = 'https://aetherhub.com/Card/Set'  # Replace with the URL of the webpage you want to scrape
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'id': 'setTable'})
# <td class="set_list_abbreviation"><span>RVR</span></td>

# print(table)

rows = table.find_all('tr')[1:]

table_data = []

for row in rows:
    cells = row.find_all('td')
    name = cells[0].text
    abbr = cells[1].text

    table_data.append(abbr)


setList = []

for sets in table_data:
    words = sets.split()
    setList.append(words[-1])

print(setList)


with open("setList", "wb") as f:
    pickle.dump(setList, f)