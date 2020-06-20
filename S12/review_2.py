import re
import urllib.request


url = "https://www.ualberta.ca/mechanical-engineering/faculty-and-staff"
req = urllib.request.urlopen(url)
response = req.read()
text = response.decode('utf-8')

pattern = r"(\w+)@(\w+)\.(\w+)"

result = re.findall(pattern, text)


for user, domain, suffix in result:
    print(user)
