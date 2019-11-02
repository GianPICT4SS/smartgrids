import requests
from lxml import html
import webbrowser
from robobrowser import RoboBrowser

USERNAME = "s26753%40studenti.polito.it" #s267534@studenti.polito.it
PASSWORD = "SmartGridProject!"

LOGIN_URL = "https://transparency.entsoe.eu/homepageLogin"
URL = "https://transparency.entsoe.eu/dashboard/show"

def main():

    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)

    f = open("dashboard.html", "a")
    f.write(result.text)
    f.close()
    webbrowser.open("dashboard.html")

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    result = session_requests.post(
    URL,
    data = payload,
    headers = dict(referer=LOGIN_URL)
    )
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
