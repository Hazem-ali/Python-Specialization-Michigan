import urllib.request, urllib.parse, urllib.error
import json
import ssl

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

#  Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_905225.json (Sum ends with 33)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
# print('User count:', len(info))
numbers = []
for item in info['comments']:
    numbers.append(int(item['count']))

print("Count", len(numbers))
print("Sum", sum(numbers))
