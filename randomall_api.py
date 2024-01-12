from .objects import *

from random import choices
from fake_useragent import FakeUserAgent
from requests import Session
from string import ascii_lowercase

class Data:
    _api = 'https://randomall.ru/api/{}'.format
    _session = Session()
    _headers = {'user-agent': FakeUserAgent().random}
    _data_d = {'d': ''.join(choices(ascii_lowercase, k = 31))}

class RandomallAPI(Data):
    @classmethod
    def fantasy_name(cls) -> int | list:
        """
        this function is designed to generate a name

        :return: string in json format or int
        """
        _req = cls._session.post(url = cls._api('general/fantasy_name'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else str(_req.json()).replace('<br>', ', ')

    @classmethod
    def appearance(cls, var : str) -> int | str:
        """
        this function is designed to generate the appearance of the characters

        :param var: var is the choice of gender to generate appearance. 1 - male, 2 - female
        :type var: :obj: `str`

        :return: int or string in the form of json
        """
        cls._data_d.update(var = var)
        _req = cls._session.post(url = cls._api('general/appearance'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def crowd(cls) -> int | str:
        """
        this function is designed to generate a secondary character

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/crowd'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def character(cls) -> int | str:
        """
        this function is designed to generate a character

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/character'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else str(_req.json()).replace('<br>', ', ')

    @classmethod
    def abilities(cls) -> int | str:
        """
        this function is designed to generate abilities

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/abilities'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def features(cls) -> int | str:
        """
        this function is designed to generate features

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/features'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else str(_req.json()).replace('<br>', ', ')

    @classmethod
    def jobs(cls) -> int | str:
        """
        this function is designed to generate jobs

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/jobs'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def race(cls) -> int | str:
        """
        this function is designed to generate a race

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/race'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def superpowers(cls) -> int | str:
        """
        this function is designed to generate superpowers

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/superpowers'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def plot(cls) -> int | str:
        """
        this function is designed to generate a plot

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/plot'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def plotkeys(cls, choice: int) -> int | Plotkeys:
        """
        this function is designed to generate keywords for the plot

        :param choice: Selection from 0 to 5. 0 - all 1 - Egabrag 2 - Talion Fonbrad 3 - Orat 4 - Campbell 5 - PhassesArc
        :type choice: :obj: `int`

        :return: int or object Plotkeys
        """
        _data = {'choice': choice}
        _req = cls._session.get(url = cls._api('general/plotkeys'), headers = cls._headers, json = _data)
        return _req.status_code if _req.status_code != 200 else Plotkeys(**_req.json())

    @classmethod
    def awkward_moment(cls) -> int | str:
        """
        this function is designed to generate an awkward moment

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/awkward_moment'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def unexpected_event(cls) -> int | str:
        """
        this function is designed to generate an unexpected turn

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/unexpected_event'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def book_name(cls) -> int | str:
        """
        this function is designed to generate book titles

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/bookname'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def fantasy_country(cls) -> int | str:
        """
        this function is designed to generate the name of a fictional country

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/bookname'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def fantasy_town(cls) -> int | str:
        """
        this function is designed to generate the name of a fictional city

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/fantasy_town'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def fantasy_continent(cls) -> int | str:
        """
        this function is designed to generate the name of a fictional continent

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/fantasy_town'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def country_description(cls) -> int | str:
        """
        this function is designed to generate a description of the country

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/country_description'), headers = cls._headers, json = cls._data_d)
        return _req.status_code if _req.status_code != 200 else str(_req.json()).replace('<br><br>', '')

    @classmethod
    def numbers(cls, count: int, max: int, min: int, repeat: bool = False) -> int | str:
        """
        this function is designed to generate random or random numbers

        :param count: number of generated numbers
        :type count: :obj: `str`

        :param max: the maximum generated number
        :type max: :obj: `str`

        :param min: the minimum generated number
        :type min: :obj: `str`

        :param repeat: remove repetitions? - True - yes
        :type repeat: :obj: `bool`

        :return: int or string in the form of json
        """
        if repeat: repeat = repeat
        _data = {'count': count, 'max': max, 'min': min, 'repeat': repeat, 'symbol': " "}
        _req = cls._session.post(url = cls._api('general/numbers'), headers = cls._headers, json = _data)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def names(cls, sex: int) -> int | str:
        """
        this function is designed to generate names

        :param sex: 1 - Male, 2  - woman
        :type sex: :obj: `int`

        :return: int or string in the form of json
        """
        _data = {'sex': sex}
        _req = cls._session.post(url = cls._api('general/names'), headers = cls._headers, json = _data)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def surnames(cls) -> int | str:
        """
        this function is designed to generate surnames

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/surnames'), headers = cls._headers, json = cls._data_d)
        if _req.status_code != 200: return _req.status_code
        else: return _req.json()

    @classmethod
    def date(cls, start: str, end: str) -> int | str:
        """
        this function is designed to generate a random date between two dates

        :param start: the date from which the generation will begin : write like this : YYYY-MM-DD
        :type start: :obj: `str`

        :param end: the date on which the generation will end : write like this : YYYY-MM-DD
        :type end: :obj: `str`

        :return: int or string in the form of json
        """
        _data = {'start': start, 'end': end}
        _req = cls._session.post(url = cls._api('general/date'), headers = cls._headers, json = _data)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def time(cls, start: str, end: str) -> int | str:
        """
        this function is designed to generate the time between two time intervals

        :param start: the minimum time from which the generation will start, example : 22:11
        :type start: :obj: `str`

        :param end: the final time at which the generation will end, example: 23:54
        :type end: :obj: `str`

        :return: int or string in the form of json
        """
        _data = {'start': start, 'end': end}
        _req = cls._session.post(url = cls._api('general/time'), headers = cls._headers, json = _data)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def countries(cls) -> int | str:
        """
        a function that is designed to generate countries

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/countries'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def cities(cls) -> int | str:
        """
        a function that is designed to generate countries

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/cities'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def draw(cls) -> int | str:
        """
        a function that is designed for drawing ideas

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('general/draw'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def gens(cls, generator_id: str) -> int | str:
        """
        a function that is designed to generate on custom generators by means of id generators

        :param generator_id: id of the custom generator
        :type generator_id: :obj: `str`

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api(f'gens/{generator_id}'), headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        else: return _req.json()['msg']

    @classmethod
    def login(cls, email: str, password: str) -> int | str:
        """
        this function is designed to log in to the site https://randomall.ru

        :param email: your email address that you used when registering
        :type email: :obj: `str`

        :param password: your password address that you used when registering
        :type password: :obj: `str`

        :return: int or string in the form of json
        """
        _data = {'login': email, 'password': password}
        _req = cls._session.post(url = cls._api('users/login'), headers = cls._headers, json = _data)
        return _req.status_code if _req.status_code != 200 else 'Authorization is successful'

    @classmethod
    def logout(cls) -> int | str:
        """
        this function is designed to log out of the account on which you have logged in

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('users/logout'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else 'Account logout is successful'

    @classmethod
    def token(cls):
        """
        function for getting a token

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api('users/token'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else Token(**_req.json())

    @classmethod
    def profile(cls, user_id: str) -> str:
        """
        function for getting a user profile using user_id

        :param user_id: i think it's already clear, a user id is a user id
        :type user_id: :obj: `str`

        :return: int or string in the form of json
        """
        _req = cls._session.get(url = cls._api(f'users/{user_id}/profile'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def user_gens(cls, user_id: str) -> int | list:
        """
        a function that is designed to get the user's generators

        :param user_id: i think it's already clear, a user id is a user id
        :type user_id: :obj: `str`

        :return: int or string in the form of json
        """
        _req = cls._session.get(url = cls._api(f'users/{user_id}/gens'), headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        return parse_obj_as(list[Gens], _req.json())

    @classmethod
    def like(cls, generator_id: str) -> int | str:
        """
        the function that is performed in order to like the generator

        :param generator_id:
        :type generator_id: :obj: `str`

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api(f'gens/{generator_id}/like'), headers = cls.headers)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def fav(cls, generator_id: str) -> int | str:
        """
        the function that is performed in order to add the generator to favorites

        :param generator_id: id of the generator
        :type generator_id: :obj: `str`

        :return: int or string in the form of json
        """
        _req = cls._session.post(url = cls._api(f'gens/{generator_id}/fav'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else _req.json()

    @classmethod
    def me_favs(cls) -> int | MeFavs:
        """
        a function designed to get your favorites

        :return: int or objects MeFavs
        """
        _req = cls._session.get(url = cls._api('users/me/gens/favs'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else parse_obj_as(list[MeFavs], _req.json())

    @classmethod
    def search(cls, sorting_by: str, tags: str = None):
        """
        function to search for custom generators

        :param sorting_by: date_updated, date_added, likes_count, views
        :type sorting_by: :obj: `str`

        :param tags: there are a lot of tags, I won't write them all, think for yourself
        :type tags: :obj: `str`

        :return: int or objects Search
        """
        _t = ''
        api_endpoints = "gens?f={sorting_by}"
        if tags:
            for _ in list(tags): _t += "".join(f"{_}&")
        cls._api = cls._api(f"{api_endpoints}&{_t[-1:]}")
        _req = cls._session.get(url = cls._api, headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else parse_obj_as(list[Search], _req.json()['items'])