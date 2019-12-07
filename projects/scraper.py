import requests
from bs4 import BeautifulSoup

r=requests.get(url='https://ajin.netlify.com')

data=BeautifulSoup(r.content,'html.parser')
data=str(data)
file=open('scrappeddata.html','w+')
file.write(data)
file.close()
print(data)
