#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """ model of all basics classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop('__class__')
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        return '[{}] ({}) {}'.\
            format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        dict_ = self.__dict__
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        dict_['__class__'] = BaseModel.__name__
        return dict_
