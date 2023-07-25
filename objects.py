class Plotkeys:
    def __init__(self, data):
        self.json = data
        self.category = None
        self.position = None
        self.name = None
        self.title = None
        self.description_main_page = None
        self.description_generator = None
        self.meta_description = None
        self.meta_keywords = None
        self.usergen = None

    @property
    def plotkeys(self):
        try:
            self.category = self.json['category']
            self.position = self.json['position']
            self.name = self.json['name']
            self.title = self.json['title']
            self.description_main_page = self.json['descriptionMainpage']
            self.description_generator = self.json['descriptionGenerator']
            self.meta_description = self.json['metaDescription']
            self.meta_keywords = self.json['metaKeywords']
            self.usergen = self.usergen['usergen']
        except(KeyError, TypeError): pass
        return self

class Token:
    def __init__(self, data):
        self.json = data
        self.id = None
        self.username = None
        self.roles = None

    @property
    def token(self):
        try:
            self.id = self.json['id']
            self.username = self.json['username']
            self.roles = self.json['roles']
        except(KeyError, TypeError): pass
        return self

class Gens:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.userId = []
        self.username = []
        self.title = []
        self.acess = []
        self.views = []
        self.active = []
        self.likes_count = []
        self.favs_count = []

    @property
    def gens(self):
        try:
            for _ in self.json:
                self.id.append(_['id'])
                self.user_id(_['user']['id'])
                self.username.append(_['user']['username'])
                self.title.append(_['title'])
                self.acess(_['title']['acess'])
                self.views(_['title']['views'])
                self.active(_['title']['active'])
                self.likes_count.append(_['title']['likesCount'])
                self.favs_count.append(_['title']['favsCount'])
        except(KeyError, TypeError): pass
        return self

class MeFavs:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.user_id = []
        self.username = []
        self.title = []
        self.acess = []
        self.views = []
        self.active = []
        self.likes_count = []
        self.favs_count = []

    @property
    def me_favs(self):
        try:
            for _ in self.json:
                self.id.append(_['id'])
                self.user_id(_['user']['id'])
                self.username.append(_['user']['username'])
                self.title.append(_['title'])
                self.acess(_['title']['acess'])
                self.views(_['title']['views'])
                self.active(_['title']['active'])
                self.likes_count.append(_['title']['likesCount'])
                self.favs_count.append(_['title']['favsCount'])
        except(KeyError, TypeError): pass
        return self

class Search:
    def __init__(self, data):
        self.json = data
        self.items = None
        self.id = []
        self.user_info = []
        self.user_info_id = []
        self.user_info_username = []
        self.category = []
        self.subcategories = []
        self.tags = []
        self.title = []
        self.description = []
        self.access = []
        self.likes_count = []
        self.favs_count = []
        self.views = []
        self.date_added = []
        self.date_updated = []
        self.ads = []
        self.active = []
        self.copyright = []
        self.generator = []
        self.format = []
        self.format_align = []
        self.format_buttons = []
        self.format_buttons_mode = []
        self.variations = []
        self.liked = []
        self.faved = []

    @property
    def search(self):
        try:
            self.items = self.json['items']
            for _ in self.items:
                self.id.append(_['id'])
                self.user_info.append(_['user'])
                self.user_info_id.append(_['user']['id'])
                self.user_info_username.append(_['user']['id'])
                self.category.append(_['category'])
                self.subcategories.append(_['subcategories'])
                self.tags.append(_['tags'])
                self.title.append(_['title'])
                self.description.append(_['description'])
                self.access.append(_['access'])
                self.likes_count.append(_['likesCount'])
                self.favs_count.append(_['favsCount'])
                self.views.append(_['views'])
                self.date_added.append(_['dateAdded'])
                self.date_updated.append(_['dateUpdated'])
                self.ads.append(_['ads'])
                self.active.append(_['active'])
                self.copyright.append(_['copyright'])
                self.generator.append(_['generator'])
                self.format.append(_['format'])
                self.format_align.append(_['format']['align'])
                self.format_buttons.append(_['format']['buttons'])
                self.format_buttons_mode.append(_['format']['buttons']['mode'])
                self.variations.append(_['variations'])
                self.liked.append(_['liked'])
                self.faved.append(_['faved'])
        except(KeyError, TypeError): pass
        return self