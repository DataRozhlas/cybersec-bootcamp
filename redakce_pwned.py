#%%
import requests
from requests.utils import requote_uri
from bs4 import BeautifulSoup
import time

#%%
r = requests.get('https://www.irozhlas.cz/redakce')
soup = BeautifulSoup(r.text)

#%%
for mail in soup.find_all(class_='b-editor__email'):
    time.sleep(0.5)
    url = requote_uri('https://haveibeenpwned.com/api/v2/breachedaccount/' + mail.text.strip())
    r = requests.get(url, headers={'user-agent': 'iROZHLAS pwner'})
    if len(r.text) > 0:
        print(mail.text.strip(), ' - breaches: ' + str(len(r.json())))
    else:
        print(mail.text.strip(), ' - ok')