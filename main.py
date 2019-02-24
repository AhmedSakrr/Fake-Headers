from browsers import chrome, firefox, opera, random_browser
from platforms import linux, macos, random_os, windows
from headers import make_header


class Headers:
    '''
    browser - str, chrome/firefox/opera. User Agent browser. Default: random\n
    os - str, win/mac/lin. OS of User Agent. Default: random\n
    headers - bool, True/False. Generate random headers or no. Default: False
    '''

    __os = {
        'win': windows,
        'mac': macos,
        'lin': linux
    }

    __browser = {
        'chrome': chrome,
        'firefox': firefox,
        'opera': opera
    }

    def __init__(self, browser=None, os=None, headers=False):
        self.platform = self.__os[os]() if os else random_os()
        self.browser = (
            self.__browser[browser]() if browser else random_browser()
        )
        self.headers = make_header() if headers else {}

    def generate(self):
        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'User-Agent': self.browser.replace('%PLAT%', self.platform)
        }

        headers.update(self.headers)

        return headers
