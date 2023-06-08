from .util import *
from random import choices
from requests import Session
from string import ascii_lowercase
class randomall_api:
    def __init__(self, proxies : dict = None):
        self.api = 'https://randomall.ru/api/{}'.format
        self.session = Session()
        self.headers = headers.Headers().headers
        self.proxies = proxies
        self.d = ''.join(choices(ascii_lowercase, k=31))

    def fantasyName(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/fantasy_name'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    #var is the floor. 1 - male 0 - female
    def appearance(self, var : str) -> str:
        data = {'d': self.d, 'var': var}
        req = self.session.post(url = self.api('general/appearance'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def crowd(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/crowd'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def character(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/character'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def abilities(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/abilities'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def features(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/features'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def jobs(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/jobs'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def race(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/race'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def superpowers(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/superpowers'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def plot(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/plot'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    #the choice is given from 1 to 5
    def plotkeys(self, choice) -> str:
        data = {'choice': choice}
        req = self.session.get(url = self.api('general/plotkeys'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return plotkeys(req.json()).plotkeys

    def awkwardMoment(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/awkward_moment'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def unexpectedEvent(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/unexpected_event'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def bookName(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/bookname'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def fantasyCountry(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/bookname'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def fantasyTown(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/fantasy_town'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def fantasyContinent(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/fantasy_town'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def countryDescription(self) -> str:
        data = {'d': self.d}
        req = self.session.post(url = self.api('general/country_description'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    #repeat : true or false
    def numbers(self, count: str, max: str, min: str, repeat: str) -> str:
        data = {'count': count, 'max': max, 'min': min, 'repeat': repeat, 'symbol': " "}
        req = self.session.post(url = self.api('general/numbers'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    #1 - Male, 2 - woman
    def names(self, sex: int) -> str:
        data = {'sex': sex}
        req = self.session.post(url = self.api('general/names'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def surnames(self):
        req = self.session.post(url = self.api('general/surnames'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    #YYYY-MM-DD
    def date(self, start: str, end: str) -> str:
        data = {'start': start, 'end': end}
        req = self.session.post(url = self.api('general/date'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    #HH:MM
    def time(self, start: str, end: str) -> str:
        data = {'start': start, 'end': end}
        req = self.session.post(url = self.api('general/time'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def countries(self) -> str:
        req = self.session.post(url = self.api('general/countries'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def cities(self) -> str:
        req = self.session.post(url = self.api('general/cities'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def suggestions(self) -> str:
        req = self.session.get(url = self.api('gens/suggestions'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return suggestions(req.json()).suggestions

    def gens(self, gensId: str) -> str:
        req = self.session.post(url = self.api(f'gens/{id}'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()['msg']

    def login(self, email: str, password: str) -> str:
        data = {'login': email, 'password': password}
        req = self.session.post(url = self.api('users/login'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def exit(self):
        req = self.session.post(url = self.api('users/logout'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def token(self) -> str:
        req = self.session.post(url = self.api('users/token'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return token(req.json()).token

    def profile(self, id: str) -> str:
        req = self.session.get(url = self.api(f'users/{id}/profile'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def userGens(self, userId: str) -> str:
        req = self.session.get(url = self.api(f'users/{id}/gens'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return Gens(req.json()).Gens

    def like(self, id: str) -> str:
        req = self.session.post(url = self.api(f'gens/{id}/like'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def fav(self, id: str) -> str:
        req = self.session.post(url = self.api(f'gens/{id}/fav'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return req.json()

    def me_favs(self) -> str:
        req = self.session.get(url = self.api('users/me/gens/favs'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return me_favs(req.json()).me_favs

    #sorting_by: date_updated, date_added, likes_count, views
    def search(self, sorting_by: str, tags: str = None):
        t = ''
        if tags != None:
            tags = tags.split()
            for _ in tags: t += ''.join(f't={_}&')
            self.api = self.api(f'gens?t={t}f={sorting_by}')
        else: self.api = self.api(f'gens?f={sorting_by}')
        req = self.session.get(url = self.api, headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.json()['detail']
        else: return search(req.json()).search