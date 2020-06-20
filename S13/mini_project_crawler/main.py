import re
import urllib.request


class Website:
    def __init__(self, url):
        self.url = url
        self.__text = None
        self.__emails = None
        self.__links = None

    @property
    def text(self):
        if self.__text is None:
            with urllib.request.urlopen(self.url) as req:
                self.__text = req.read().decode('utf-8')

        return self.__text

    @property
    def emails(self):
        if self.__emails is None:
            pattern = r"[a-z]+@[a-z]+.[a-z]+"
            self.__emails = re.findall(pattern, self.text)

        return self.__emails

    @property
    def links(self):
        if self.__links is None:
            pattern = r'<a[^>]* href="([^"]*)"'
            links = re.findall(pattern, self.text)
            self.__links = [Website(link) for link in links]
        return self.__links


url = "https://www.ualberta.ca/mechanical-engineering/faculty-and-staff"
website = Website(url)
print(website.emails)
for link in website.links[0].links:
    print(link.url)

