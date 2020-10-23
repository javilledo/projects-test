

from bs4 import BeautifulSoup as BS
import requests 

url = 'https://www.google.es/'

res = requests.get(url).content.decode("ISO-8859-1")

div_list = list(BS(res, 'html.parser').find_all('div'))

class_list= [BS(str(div), 'html.parser').find_all('', class_="gbi") for div in div_list]

print(BS(str((class_list[0])), 'html.parser')))


