# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')


count = int(input("Enter Count: "))
position = int(input("Enter Position: "))
index = position - 1


# http://py4e-data.dr-chuck.net/known_by_Shanna.html
# http://py4e-data.dr-chuck.net/known_by_Fikret.html

# Retrieve all of the anchor tags


i = 0
while i <= count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print("Retrieving:", url)
    url = tags[index].get('href', None)
    i += 1
