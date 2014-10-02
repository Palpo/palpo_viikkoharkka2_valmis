# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class Animal(ndb.Model):
    name = ndb.StringProperty(required=True)
    prey = ndb.KeyProperty(kind="Animal", repeated=True)
    
    def as_dict(self):
        prey = [p.get().name for p in self.prey]
        return {'id': self.key.id(), 'name': self.name, 'prey': prey }
    