import urllib.request


def some_function(url):
    req = urllib.request.urlopen(url)
    text = req.read().decode('utf-8')
    return text


text = some_function("https://python.org")
print(text)