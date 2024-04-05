#!/usr/bin/python3

class BaseModel():
    """ model of all basics classes"""
    def __init__(self):
        self.id = 1
        self.created_at = 1
        self.updated_at = 1
    
    def __str__(self):
        return '[<{BaseModel}>] (<self.id>) <self.__dict__>'
