from typing import List

class Transaction:
    def __init__(self, name: str, description: str, image_id: str, paid_by, posted_by: str, price: str, time_created: str):
        self._description = description
        self._image_id = image_id
        self._paid_by = paid_by
        self._name = name
        self._posted_by = posted_by
        self._price = price
        self._time_created = time_created
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description:str):
        self._description = description
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name:str):
        self._name = name
    
    @property
    def image_id(self):
        return self._image_id
    
    @image_id.setter
    def image_id(self, image_id:str):
        self._image_id = image_id
    
    @property
    def paid_by(self):
        return self._paid_by
    
    @paid_by.setter
    def paid_by(self, paid_by):
        self._paid_by = paid_by
    
    @property
    def posted_by(self) -> str:
        return self._posted_by
    
    @posted_by.setter
    def posted_by(self, posted_by: str):
        self._posted_by = posted_by
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price:str):
        self._price = price
    
    @property
    def time_created(self):
        return self._time_created
    
    @time_created.setter
    def time_created(self, time_created:str):
        self._time_created = time_created