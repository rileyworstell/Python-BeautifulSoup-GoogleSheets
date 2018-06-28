import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import requests

pokemon_page = "https://pokemondb.net/pokedex/stats/height-weight"
response = requests.get(pokemon_page)
soup = BeautifulSoup(response.content, "html.parser")

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open("Python Writing").sheet1

x = ""
#  thisSoup = soup.find("td", class_="cell-name")
for tag in soup.findAll():
    try:
        x += "\n" + tag['title']
    except KeyError:
        pass

x = x.replace("View pokedex for ", "")
x = list(x.split("\n"))
x.pop(0)
x.pop(0)
x.pop(0)
h = ""
for y in x:
    if y[0] == "#":
        h += y
h = list(h.split("#"))
h.pop(0)
print(h)
num = 1
for pokemon in h:
    sheet.update_acell('C' + str(num), pokemon)
    num += 1
