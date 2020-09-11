import urllib.request


with urllib.request.urlopen('https://python.org') as req:
    text = req.read().decode('utf-8')

print(text)