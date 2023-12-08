import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name':'sunwei'}),encoding='utf-8')
response = urllib.request.urlopen('https://www.httpbin.org/post',data=data)
print(response.read().decode('utf-8'))