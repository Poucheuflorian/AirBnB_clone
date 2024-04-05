#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():
    """ model of all basics classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
    
    def __str__(self):
        return '[{}] ({}) {}'.format(BaseModel.__name__,self.id,self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dict_ = self.__dict__
        dict_[created_at] = dict_[created_at].isoformat()
        dict_[updated_at] = dict_[created_at].isoformat()
        dict_['__class__'] = BaseModel.__name__
