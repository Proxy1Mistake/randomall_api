from random import choices
from requests import Session
from string import ascii_lowercase
from pydantic import parse_obj_as

from .objects import *

class RandomallAPI:
    _api = 'https://randomall.ru/api/{}'.format
    _data_d = {'d': ''.join(choices(ascii_lowercase, k = 31))}
    _headers = {
        "user-agent": "Mozilla/5.0 (Linux; U; Linux x86_64; en-US) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1452.400 Safari/536"
    }

    @classmethod
    def __request_method(cls, method: str, url: str, data: dict = None, ):
        _session = Session()

        if method == 'get': req = _session.get(url = url, headers = cls._headers)
        else: req = _session.post(url = url, json = data, headers = cls._headers)

        if req.status_code == 200: return req

        print(f'Error >>> {req.status_code} {req.text}')
        exit()

    @classmethod
    def fantasy_name(cls) -> str:
        """
        this function is designed to generate a name

        :return: string in json format or int
        """
        return str(cls.__request_method(method = 'post',
                                        url = cls._api('general/fantasy_name'),
                                        data = cls._data_d).json()
                   ).replace('<br>', ', ')


    @classmethod
    def appearance(cls, var : str) -> str:
        """
        this function is designed to generate the appearance of the characters

        :param var: var is the choice of gender to generate appearance. 1 - male, 2 - female
        :type var: :obj: `str`

        :return: int or string in the form of json
        """
        cls._data_d.update(var = var)

        return cls.__request_method(method = 'post',
                                    url = cls._api('general/appearance'),
                                    data = cls._data_d).json()

    @classmethod
    def crowd(cls) -> str:
        """
        this function is designed to generate a secondary character

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/crowd'),
                                    data = cls._data_d).json()

    @classmethod
    def character(cls) -> str:
        """
        this function is designed to generate a character

        :return: int or string in the form of json
        """
        return str(cls.__request_method(method = 'post',
                                        url = cls._api('general/fantasy_name'),
                                        data = cls._data_d).json()
                   ).replace('<br>', ', ')

    @classmethod
    def abilities(cls) -> str:
        """
        this function is designed to generate abilities

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/abilities'),
                                    data = cls._data_d).json()

    @classmethod
    def features(cls) -> str:
        """
        this function is designed to generate features

        :return: int or string in the form of json
        """
        return str(cls.__request_method(method = 'post',
                                        url = cls._api('general/features'),
                                        data = cls._data_d).json()
                   ).replace('<br>', ', ')

    @classmethod
    def jobs(cls) -> str:
        """
        this function is designed to generate jobs

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/jobs'),
                                    data = cls._data_d).json()
    @classmethod
    def race(cls) -> str:
        """
        this function is designed to generate a race

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/race'),
                                    data = cls._data_d).json()

    @classmethod
    def superpowers(cls) -> str:
        """
        this function is designed to generate superpowers

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/superpowers'),
                                    data = cls._data_d).json()

    @classmethod
    def plot(cls) -> str:
        """
        this function is designed to generate a plot

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/plot'),
                                    data = cls._data_d).json()

    @classmethod
    def plotkeys(cls, choice: int) -> Plotkeys:
        """
        this function is designed to generate keywords for the plot

        :param choice: Selection from 0 to 5. 0 - all 1 - Egabrag 2 - Talion Fonbrad 3 - Orat 4 - Campbell 5 - PhassesArc
        :type choice: :obj: `int`

        :return: int or object Plotkeys
        """
        _data = {
            'choice': choice
        }

        return Plotkeys(**cls.__request_method(method = 'get',
                                               url = cls._api('general/plotkeys'),
                                               data = _data).json())

    @classmethod
    def awkward_moment(cls) -> str:
        """
        this function is designed to generate an awkward moment

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/awkward_moment'),
                                    data = cls._data_d).json()

    @classmethod
    def unexpected_event(cls) -> str:
        """
        this function is designed to generate an unexpected turn

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/unexpected_event'),
                                    data = cls._data_d).json()

    @classmethod
    def book_name(cls) -> str:
        """
        this function is designed to generate book titles

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/bookname'),
                                    data = cls._data_d).json()

    @classmethod
    def fantasy_country(cls) -> str:
        """
        this function is designed to generate the name of a fictional country

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/fantasy_country'),
                                    data = cls._data_d).json()

    @classmethod
    def fantasy_town(cls) -> str:
        """
        this function is designed to generate the name of a fictional city

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/fantasy_town'),
                                    data = cls._data_d).json()

    @classmethod
    def fantasy_continent(cls) -> str:
        """
        this function is designed to generate the name of a fictional continent

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/fantasy_continent'),
                                    data = cls._data_d).json()

    @classmethod
    def country_description(cls) -> str:
        """
        this function is designed to generate a description of the country

        :return: int or string in the form of json
        """
        return str(cls.__request_method(method = 'post',
                                        url = cls._api('general/country_description'),
                                        data = cls._data_d).json()
                   ).replace('<br><br>', '')

    @classmethod
    def numbers(cls, min: int, max: int, count: int = 1, repeat: bool = False) -> str:
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

        _data = {
            'count': count,
            'max': max,
            'min': min,
            'repeat': repeat,
            'symbol': " "
        }

        return cls.__request_method(method = 'post',
                                    url = cls._api('general/numbers'),
                                    data = _data).json()

    @classmethod
    def names(cls, sex: int) -> str:
        """
        this function is designed to generate names

        :param sex: 1 - Male, 2  - woman
        :type sex: :obj: `int`

        :return: int or string in the form of json
        """
        _data = {'sex': sex}

        return cls.__request_method(method = 'post',
                                    url = cls._api('general/names'),
                                    data = _data
                                    ).json()

    @classmethod
    def surnames(cls) -> str:
        """
        this function is designed to generate surnames

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/surnames'),
                                    data = cls._data_d
                                    ).json()

    @classmethod
    def date(cls, start: str, end: str) -> str:
        """
        this function is designed to generate a random date between two dates

        :param start: the date from which the generation will begin : write like this : YYYY-MM-DD
        :type start: :obj: `str`

        :param end: the date on which the generation will end : write like this : YYYY-MM-DD
        :type end: :obj: `str`

        :return: int or string in the form of json
        """
        _data = {
            'start': start, 'end': end
        }

        return cls.__request_method(method = 'post',
                                    url = cls._api('general/date'),
                                    data = _data
                                    ).json()

    @classmethod
    def time(cls, start: str, end: str) -> str:
        """
        this function is designed to generate the time between two time intervals

        :param start: the minimum time from which the generation will start, example : 22:11
        :type start: :obj: `str`

        :param end: the final time at which the generation will end, example: 23:54
        :type end: :obj: `str`

        :return: int or string in the form of json
        """
        _data = {
            'start': start,
            'end': end
        }

        return cls.__request_method(method = 'post',
                                    url = cls._api('general/time'),
                                    data = _data
                                    ).json()

    @classmethod
    def countries(cls) -> str:
        """
        a function that is designed to generate countries

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/countries')
                                    ).json()

    @classmethod
    def cities(cls) -> str:
        """
        a function that is designed to generate cities

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/cities')
                                    ).json()

    @classmethod
    def draw(cls) -> str:
        """
        a function that is designed for drawing ideas

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api('general/draw')
                                    ).json()

    @classmethod
    def gens(cls, generator_id: str) -> str:
        """
        a function that is designed to generate on custom generators by means of id generators

        :param generator_id: id of the custom generator
        :type generator_id: :obj: `str`

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'post',
                                    url = cls._api(f'gens/{generator_id}')
                                    ).json()['msg']

    @classmethod
    def login(cls, email: str, password: str) -> str:
        """
        this function is designed to login to the site

        :param email: your email address that you used when registering
        :type email: :obj: `str`

        :param password: your password address that you used when registering
        :type password: :obj: `str`

        :return: int or string in the form of json
        """
        _data = {
            'login': email,
            'password': password
        }

        _req = cls.__request_method(method = 'post',
                             url = cls._api('users/login'),
                             data = _data
                             )

        cls._headers['cookie'] = f'access_c={_req.cookies["access_c"]}'

        return 'Account authorization is successful'

    @classmethod
    def logout(cls) -> str:
        """
        this function is designed to log out of the account on which you have logged in

        :return: int or string in the form of json
        """
        cls.__request_method(method = 'post',
                             url = cls._api('users/logout')
                             ).json()

        return 'Account logout is successful'

    @classmethod
    def token(cls):
        """
        function for getting a token

        :return: int or string in the form of json
        """
        return Token(**cls.__request_method(method = 'post',
                                            url = cls._api('users/token')
                                            ).json()
                     )

    @classmethod
    def profile(cls, user_id: str) -> str:
        """
        function for getting a user profile using user_id

        :param user_id: i think it's already clear, a user id is a user id
        :type user_id: :obj: `str`

        :return: int or string in the form of json
        """
        return cls.__request_method(method = 'get',
                                    url = cls._api(f'users/{user_id}/profile')
                                    ).json()

    @classmethod
    def user_gens(cls, user_id: str) -> list[Gens]:
        """
        a function that is designed to get the user's generators

        :param user_id: i think it's already clear, a user id is a user id
        :type user_id: :obj: `str`

        :return: int or string in the form of json
        """
        _req = cls.__request_method(method = 'get',
                                    url = cls._api(f'users/{user_id}/gens')
                                    )

        return parse_obj_as(list[Gens], _req.json())

    @classmethod
    def new_username(cls, username: str) -> str:
        """
        This function is designed to change your username.

        :param username: well, you understand in short.
        :type username: :obj: `str`

        :return: if there are no errors, it returns a string
        """
        data = {
            'username': username
        }

        cls.__request_method(method = 'post',
                             url = cls._api('users/me/change_username'),
                             data = data
                             )

        return 'Your username has been changed.'

    @classmethod
    def new_password(cls, old_password: str, new_password: str) -> str:
        """
        This function is designed to change your password.

        :param old_password:
        :type :obj: `str`

        :param new_password:
        :type :obj: `str`

        :return: if there are no errors, it will output a string
        """
        data = {
            'oldPassword': old_password,
            'password1': new_password,
            'password2': new_password
        }

        cls.__request_method(method = 'post',
                             url = cls._api('users/me/change_username'),
                             data = data
                             )

        return 'Your password has been changed.'

    @classmethod
    def like(cls, generator_id: str) -> None:
        """
        the function that is performed in order to like the generator

        :param generator_id:
        :type generator_id: :obj: `str`

        :return: None
        """
        cls.__request_method(method = 'post',
                             url = cls._api(f'gens/{generator_id}/like')
                             )

    @classmethod
    def fav(cls, generator_id: str) -> None:
        """
        the function that is performed in order to add the generator to favorites

        :param generator_id: id of the generator
        :type generator_id: :obj: `str`

        :return: None
        """
        cls.__request_method(method = 'post',
                             url = cls._api(f'gens/{generator_id}/fav')
                             )

    @classmethod
    def me_favs(cls) -> list[MeFavs]:
        """
        a function designed to get your favorites

        :return: int or objects MeFavs
        """
        _req = cls.__request_method(method = 'get',
                                    url = cls._api('users/me/gens/favs')
                                    )

        return parse_obj_as(list[MeFavs], _req.json())

    @classmethod
    def search(cls, sorting_by: str = 'likes_count', tags: str = None) -> list[Search]:
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

        _req = cls.__request_method(method = 'get',
                                    url = cls._api
                                    )

        return parse_obj_as(list[Search], _req.json()['items'])
