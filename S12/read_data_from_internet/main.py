import urllib.request

url = "https://python.org"

req = urllib.request.urlopen(url)

# text = req.read()  ## bytes object
text = req.read().decode('utf-8')

print(text)
