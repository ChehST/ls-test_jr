class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find(self, how, what):
        return self.browser.find_element(how, what)

    def get_text(self, how, what):
        return self.find(how, what).text


    ...