import re
import urllib.request


def read_from_site(url):
    req = urllib.request.urlopen(url)
    text = req.read().decode('utf-8')
    return text


text = read_from_site("https://www.ualberta.ca/mechanical-engineering/faculty-and-staff")
pattern = r"[a-z]+@[a-z]+.[a-z]+"
result = re.findall(pattern, text)
print(result)