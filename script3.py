import urllib.request
from lxml import html
wiki = 'http://www.saihebro.com/saihebro/index.php?url=/datos/ficha/estacion:A095'
page = urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")
# print(soup.prettify())
tablas = soup.find_all("table")
#print(tablas[1])
A=[]
B=[]
C=[]
D=[]

i = 0
for row in tablas[1].findAll("tr"):
	cells = row.findAll("td")
	if len(cells)==6 and i>1:
		A.append(cells[0].find(text=True))
		B.append(cells[1].find(text=True))
		C.append(cells[2].find(text=True))
		D.append(cells[3].find(text=True))
	i+=1

import pandas as pd
df=pd.DataFrame(A,columns=['Descripcion'])
df['Fecha']=B
df['Valor']=C
df['Unidad']=D
print(df)



