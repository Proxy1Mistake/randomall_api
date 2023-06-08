from fake_useragent import FakeUserAgent

class Headers:
    def __init__(self):
        self.headers = {'user-agent': FakeUserAgent().random}