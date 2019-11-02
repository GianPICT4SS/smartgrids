import requests
import webbrowser

def display(content):
    # to see this HTML in web browser
    with open('temp.html', 'wb') as f:
        f.write(content)
        webbrowser.open('temp.html')

with requests.session() as r:

    USERNAME = "s267534@studenti.polito.it" #s257534%40studenti.polito.it
    PASSWORD = "SmartGridProject!"

    login_url = "https://transparency.entsoe.eu/homepageLogin"
    dashboard_url="https://transparency.entsoe.eu/dashboard/show"

    # load page with form - to get cookies and `csrf` from HTML
    response = r.get(login_url)

    webbrowser.open_new(login_url)


    # cookies are not part of form so you don't use in form_data,
    # session will use cookies from previous request so you don't have to copy them
    form_data = {
        'target-url': "https://transparency.entsoe.eu/dashboard/show", #probably non è necessario
        'email': USERNAME,
        'password': PASSWORD
    }

    # send form data to server
    response = r.post(login_url, data=form_data)

    print('status_code:', response.status_code)
    print('history:', response.history)
    print('url:', response.url)

    #display(response.content)

    response = r.get(dashboard_url)

    #display(response.content)
