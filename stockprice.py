"""import requests
inp=input('input word')
r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20191224T085756Z.5b8467f1b488ef86.d781c9b6fbae705b4d60ab6009c695c940f73da2&text=%22'+inp+'%22&lang=en-hi')
z=r.json()
ans=str(z.get('text')[0])
print(ans[1:len(ans)-1])"""

import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.moneycontrol.com/india/stockpricequote/steel-rolling/manaksia/M16"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
soup.prettify()

table = soup.find('div', attrs = {'id':'div_bse_nse_livebox_wrap'})
for row in table.findAll('div', attrs = {'class':'pcnsb div_live_price_wrap'}):
    print(row)
    
