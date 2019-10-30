import requests as req
import bs4

def retr_s(url):
    if 'http://'or 'https://' in url:
        s = req.get(url).text
        return(s)
    else:
        return ("L'url non è valido")

def retr_h1(s):
    soup = bs4.BeautifulSoup(s)
    list = soup.findAll('h1') #Ci permette di ricercare un determinato tag all'intenro del "soup"
    if list:
        for a in list:
            print (a)
    else:
        print(" Non ci sono H1 in questa pagina ")

sites = [
    'http://www.python.org'
]
for i in sites:
    s=retr_s(i)
    print('List of H1 di ' + i)
    retr_h1(s)
    print()

site = req.get('https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show')
