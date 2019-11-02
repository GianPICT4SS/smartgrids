import requests
from lxml import html
import webbrowser
from robobrowser import RoboBrowser

USERNAME = "s267534@studenti.polito.it"
PASSWORD = "SmartGridProject!"

LOGIN_URL = f"https://transparency.entsoe.eu/login?&username={USERNAME}&password={PASSWORD}"
URL = "https://transparency.entsoe.eu/dashboard/show"

def main():

    session_requests = requests.session()
    result = session_requests.post(LOGIN_URL)
    f = open("dashboard.html", "w")
    f.write(result.text)
    f.close()
    webbrowser.open("dashboard.html")

    # TODO puoi cancellare le linee seguenti. La logica dello spider, almeno in questo caso, non è quella di procedere passo passo.
    # In pratica una volta fatto il login con la sessione, parti direttamente a fare le richieste get mirate per ottenere i dati.
    # Non c'è bisogno di simulare il click o altro. 
    # Quindi, in fase di debug va benissimo, ma a livello pratico e di implementazione bastano le due righe 14 e 15 per fare il login senza
    # bisogno di salvarti l'html e di visualizzarlo.
    """
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    result = session_requests.post(
    URL,
    data = payload,
    headers = dict(referer=LOGIN_URL)
    )
    """
    print("first get: " + str(result.ok))
    print("SC :" + str(result.status_code))
    
    '''


    url = "https://transparency.entsoe.eu/homepageLogin"
    myInput = {'email': USERNAME, 'password': PASSWORD}
    x = requests.get(url, data=myInput)
    y = x.text
    f = open("home.html", "a")
    f.write(y)
    f.close()
    webbrowser.open('file:///root/python/home.html')
    # print(result.headers)
    # print("text: " + result.text)
    '''
    '''
    br=RoboBrowser()
    br.open("https://transparency.entsoe.eu/homepageLogin")
    form = br.get_form()
    form['username'] = USERNAME
    form['password'] = PASSWORD
    br.submit_form(form)
    '''

    # Scrape url
    result = session_requests.get(URL, headers=dict(referer=URL))
    tree = html.fromstring(result.content)
    print("second get: " + str(result.ok))
    print("SC :" + str(result.status_code))
    # print(result.headers)
    # print("text: " + result.text)



if __name__=='__main__':
    main()
