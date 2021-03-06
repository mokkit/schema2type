from __future__ import annotations
from typing import Any, Dict, List, Optional, Union
from schema2type import SchemaBasedObject

class Address(SchemaBasedObject):
    street: Optional[str] = ...
    city: Optional[str] = ...
    state: Optional[str] = ...
    zip: Optional[str] = ...

    # noinspection PyMissingConstructor
    def __init__(self, street: Optional[str] = None, city: Optional[str] = None, state: Optional[str] = None, zip: Optional[str] = None, **kwargs): ...

class ApiResponse(SchemaBasedObject):
    code: Optional[int] = ...
    type: Optional[str] = ...
    message: Optional[str] = ...

    # noinspection PyMissingConstructor
    def __init__(self, code: Optional[int] = None, type: Optional[str] = None, message: Optional[str] = None, **kwargs): ...

class Category(SchemaBasedObject):
    id: Optional[int] = ...
    name: Optional[str] = ...

    # noinspection PyMissingConstructor
    def __init__(self, id: Optional[int] = None, name: Optional[str] = None, **kwargs): ...

class Customer(SchemaBasedObject):
    id: Optional[int] = ...
    username: Optional[str] = ...
    address: Optional[List[Address]] = ...

    # noinspection PyMissingConstructor
    def __init__(self, id: Optional[int] = None, username: Optional[str] = None, address: Optional[List[Address]] = None, **kwargs): ...

class Order(SchemaBasedObject):
    id: Optional[int] = ...
    petId: Optional[int] = ...
    quantity: Optional[int] = ...
    shipDate: Optional[str] = ...
    status: Optional[str] = ...
    complete: Optional[bool] = ...

    # noinspection PyMissingConstructor
    def __init__(self, id: Optional[int] = None, petId: Optional[int] = None, quantity: Optional[int] = None, shipDate: Optional[str] = None, status: Optional[str] = None, complete: Optional[bool] = None, **kwargs): ...

class Pet(SchemaBasedObject):
    id: Optional[int] = ...
    name: str = ...
    category: Optional[Category] = ...
    photoUrls: List[str] = ...
    tags: Optional[List[Tag]] = ...
    status: Optional[str] = ...

    # noinspection PyMissingConstructor
    def __init__(self, name: str, photoUrls: List[str], id: Optional[int] = None, category: Optional[Category] = None, tags: Optional[List[Tag]] = None, status: Optional[str] = None, **kwargs): ...

class Tag(SchemaBasedObject):
    id: Optional[int] = ...
    name: Optional[str] = ...

    # noinspection PyMissingConstructor
    def __init__(self, id: Optional[int] = None, name: Optional[str] = None, **kwargs): ...

class User(SchemaBasedObject):
    id: Optional[int] = ...
    username: Optional[str] = ...
    firstName: Optional[str] = ...
    lastName: Optional[str] = ...
    email: Optional[str] = ...
    password: Optional[str] = ...
    phone: Optional[str] = ...
    userStatus: Optional[int] = ...

    # noinspection PyMissingConstructor
    def __init__(self, id: Optional[int] = None, username: Optional[str] = None, firstName: Optional[str] = None, lastName: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None, phone: Optional[str] = None, userStatus: Optional[int] = None, **kwargs): ...

