class suggestions:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.likes_count = []
        self.title = []

    @property
    def suggestions(self):
        for x in self.json:
            self.id.append(x['id'])
            self.likes_count.append(x['likesCount'])
            self.title.append(x['title'])
        return self

class plotkeys:
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
        try: self.category = self.json['category']
        except(KeyError, TypeError): pass
        try: self.position = self.json['position']
        except(KeyError, TypeError): pass
        try: self.name = self.json['name']
        except(KeyError, TypeError): pass
        try: self.title = self.json['title']
        except(KeyError, TypeError): pass
        try: self.description_main_page = self.json['descriptionMainpage']
        except(KeyError, TypeError): pass
        try: self.description_generator = self.json['descriptionGenerator']
        except(KeyError, TypeError): pass
        try: self.meta_description = self.json['metaDescription']
        except(KeyError, TypeError): pass
        try: self.meta_keywords = self.json['metaKeywords']
        except(KeyError, TypeError): pass
        try: self.usergen = self.usergen['usergen']
        except(KeyError, TypeError): pass
        return self

class token:
    def __init__(self, data):
        self.json = data
        self.id = None
        self.username = None
        self.roles = None

    @property
    def token(self):
        try: self.id = self.json['id']
        except(KeyError, TypeError): pass
        try: self.username = self.json['username']
        except(KeyError, TypeError): pass
        try: self.roles = self.json['roles']
        except(KeyError, TypeError): pass
        return self

class gens:
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
        for x in self.json:
            try: self.id.append(x['id'])
            except(KeyError, TypeError): pass
            try: self.user_id(x['user']['id'])
            except(KeyError, TypeError): pass
            try: self.username.append(x['user']['username'])
            except(KeyError, TypeError): pass
            try: self.title.append(x['title'])
            except(KeyError, TypeError): pass
            try: self.acess(x['title']['acess'])
            except(KeyError, TypeError): pass
            try: self.views(x['title']['views'])
            except(KeyError, TypeError): pass
            try: self.active(x['title']['active'])
            except(KeyError, TypeError): pass
            try: self.likes_count.append((x['title']['likesCount']))
            except(KeyError, TypeError): pass
            try: self.favs_count.append(x['title']['favsCount'])
            except(KeyError, TypeError): pass
        return self

class me_favs:
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
        for x in self.json:
            try: self.id.append(x['id'])
            except(KeyError, TypeError): pass
            try: self.user_id(x['user']['id'])
            except(KeyError, TypeError): pass
            try: self.username.append(x['user']['username'])
            except(KeyError, TypeError): pass
            try: self.title.append(x['title'])
            except(KeyError, TypeError): pass
            try: self.acess(x['title']['acess'])
            except(KeyError, TypeError): pass
            try: self.views(x['title']['views'])
            except(KeyError, TypeError): pass
            try: self.active(x['title']['active'])
            except(KeyError, TypeError): pass
            try: self.likes_count.append((x['title']['likesCount']))
            except(KeyError, TypeError): pass
            try: self.favs_count.append(x['title']['favsCount'])
            except(KeyError, TypeError): pass
        return self

class search:
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
        try: self.items = self.json['items']
        except(KeyError, TypeError): pass
        for x in self.items:
            try: self.id.append(x['id'])
            except(KeyError, TypeError): pass
            try: self.user_info.append(x['user'])
            except(KeyError, TypeError): pass
            try: self.user_info_id.append(x['user']['id'])
            except(KeyError, TypeError): pass
            try: self.user_info_username.append(x['user']['id'])
            except(KeyError, TypeError): pass
            try: self.category.append(x['category'])
            except(KeyError, TypeError): pass
            try: self.subcategories.append(x['subcategories'])
            except(KeyError, TypeError): pass
            try: self.tags.append(x['tags'])
            except(KeyError, TypeError): pass
            try: self.title.append(x['title'])
            except(KeyError, TypeError): pass
            try: self.description.append(x['description'])
            except(KeyError, TypeError): pass
            try: self.access.append(x['access'])
            except(KeyError, TypeError): pass
            try: self.likes_count.append(x['likesCount'])
            except(KeyError, TypeError): pass
            try: self.favs_count.append(x['favsCount'])
            except(KeyError, TypeError): pass
            try: self.views.append(x['views'])
            except(KeyError, TypeError): pass
            try: self.date_added.append(x['dateAdded'])
            except(KeyError, TypeError): pass
            try: self.date_updated.append(x['dateUpdated'])
            except(KeyError, TypeError): pass
            try: self.ads.append(x['ads'])
            except(KeyError, TypeError): pass
            try: self.active.append(x['active'])
            except(KeyError, TypeError): pass
            try: self.copyright.append(x['copyright'])
            except(KeyError, TypeError): pass
            try: self.generator.append(x['generator'])
            except(KeyError, TypeError): pass
            try: self.format.append(x['format'])
            except(KeyError, TypeError): pass
            try: self.format_align.append(x['format']['align'])
            except(KeyError, TypeError): pass
            try: self.format_buttons.append(x['format']['buttons'])
            except(KeyError, TypeError): pass
            try: self.format_buttons_mode.append(x['format']['buttons']['mode'])
            except(KeyError, TypeError): pass
            try: self.variations.append(x['variations'])
            except(KeyError, TypeError): pass
            try: self.liked.append(x['liked'])
            except(KeyError, TypeError): pass
            try: self.faved.append(x['faved'])
            except(KeyError, TypeError): pass
        return self