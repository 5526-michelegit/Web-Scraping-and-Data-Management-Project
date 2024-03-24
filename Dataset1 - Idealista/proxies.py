import requests
import requests_html
from lxml.html import fromstring
import pandas as pd

def get_proxies():
    #url = 'https://free-proxy-list.net/'
    url = 'http://list.didsoft.com/get?email=p.comensoli@campus.unimib.it&pass=66kbq6&pid=http3000&showcountry=no'
    response = requests.get(url)
    df = pd.read_html(response.text)[0]

    # Optional filter
    #proxies = df.loc[(df['Code'] == 'IT') & (df['Anonymity'] == 'anonymous')][['IP Address', 'Port']]
    #proxies = df.loc[(df['Anonymity'] == 'anonymous')][['IP Address', 'Port']]
    
    proxies = proxies['IP Address'] + ':' + proxies['Port'].astype(str)
    proxies = proxies.tolist()
    return proxies