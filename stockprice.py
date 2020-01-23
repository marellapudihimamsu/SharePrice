
import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.moneycontrol.com/india/stockpricequote/steel-rolling/manaksia/M16"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
soup.prettify()

table = soup.find('div', attrs = {'id':'div_bse_nse_livebox_wrap'})
for row in table.findAll('div', attrs = {'class':'pcnsb div_live_price_wrap'}):
    print(row)
    
