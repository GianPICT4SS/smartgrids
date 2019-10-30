import requests
from lxml import html
#from robobrowser import RoboBrowser

USERNAME = "s267534@studenti.polito.it"
PASSWORD = "SmartGridProject!"

LOGIN_URL = "https://transparency.entsoe.eu/homepageLogin"
URL = "https://transparency.entsoe.eu/dashboard/show"

def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)

    payload = {
        "url" : "%2Fdashboard%2Fshow",
        "username": USERNAME,
        "password": PASSWORD
    }

    result = session_requests.get(
    LOGIN_URL,
    data = payload,
    headers = dict(referer=LOGIN_URL)
    )
    print("first get: " + str(result.ok))
    print("SC :" + str(result.status_code))
    # print(result.headers)
    # print("text: " + result.text)

    # Scrape url
    result = session_requests.get(URL, headers=dict(referer=URL))
    tree = html.fromstring(result.content)
    print("second get: " + str(result.ok))
    print("SC :" + str(result.status_code))
    # print(result.headers)
    # print("text: " + result.text)



if __name__=='__main__':
    main()
