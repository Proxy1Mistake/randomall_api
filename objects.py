from pydantic import BaseModel

class Plotkeys(BaseModel):
    category: str
    descriptionMainpage: str
    id: int
    metaDescription: str
    metaKeywords: str
    name: str
    position: int
    title: str
    usergen: bool

class Token(BaseModel):
    id: int
    username: str
    roles: list

class Gens(BaseModel):
    access: int
    active: bool
    ads: bool
    category: str
    copyright: bool
    dateAdded: str
    dateUpdated: str
    description: str
    favsCount: int
    id: int
    likesCount: int
    subcategories: str | None
    tags: list
    title: str
    views: int

class MeFavs(BaseModel):
    access: int
    active: bool
    ads: bool
    category: str
    copyright: bool
    dateAdded: str
    dateUpdated: str
    description: str
    favsCount: int
    id: int
    likesCount: int
    subcategories: str | None
    tags: list
    title: str
    views: int

class Search(BaseModel):
    access: int
    active: bool
    ads: bool
    category: str
    copyright: bool
    faved: bool
    favsCount: int
    format: dict
    generator: str
    id: int
    liked: bool
    likesCount: int
    subcategories: str | None
    tags: list
    title: str
    user: list
    variations: str
    views: int