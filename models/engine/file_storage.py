#!/usr/bin/python3
import json


class FileStorage():
    """ Storage of my program """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__class__.__objects

    def new(self, obj):
        self.__class__.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dict_save = {}
        for key, value in self.__class__.__objects.items():
            dict_save[key] = value.to_dict()
        with open(self.__class__.__file_path, 'w', errors='ignore') as f:
            json.dump(dict_save, f, sort_keys=True, indent=4)
    def reload(self):
        try:
            with open(self.__class__.__file_path) as f:
                self.__class__.__objects =  json.load(f)
        except:
            pass
