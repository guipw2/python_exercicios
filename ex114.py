import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('The website Pudim is down')
else:
    print('I was able to access the Pudim website successfully')
    print(site.read())
