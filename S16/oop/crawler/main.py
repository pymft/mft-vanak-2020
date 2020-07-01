import re
import urllib.request


class Website:
    history = {}

    def __init__(self, url):
        self.url = url
        self.__text = None
        self.__links = None
        # self.instances.update({self.url: self})
        self.history[self.url] = self

    def __repr__(self):
        return "site: <<" + self.url + ">>"

    @property
    def text(self):
        if self.__text is None:
            with urllib.request.urlopen(self.url) as req:
                self.__text = req.read().decode('utf-8')

        return self.__text

    @property
    def links(self):
        if self.__links is None:
            pattern = r'<a[^>]* href="(https?[^"]*)"'
            links = re.findall(pattern, self.text)
            self.__links = []
            for link in links:
                if link in self.history:
                    site = self.history[link]
                else:
                    site = Website(link)
                self.__links.append(site)
        return self.__links


url = "https://www.python.org"
website = Website(url)
print(website.links)
for inner_website in website.links:
    print(inner_website.links)
    print(len(Website.history))

