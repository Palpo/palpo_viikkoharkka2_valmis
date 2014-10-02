# -*- coding: utf-8 -*-

import os
import webapp2
import jinja2

from models import Animal
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

PARENT = ndb.Key("FoodChain", 1)


class MainPage(webapp2.RequestHandler):
    def get(self):
        animals = [a.as_dict() for a in Animal.query(ancestor=PARENT)]
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({"animals": animals}))


class NewAnimalHandler(webapp2.RequestHandler):        
    def post(self):
        name = self.request.get('animal')
        
        if name:
            animal = Animal(parent=PARENT, name=name)
            animal.put()
        
        self.redirect('/')
        

class NewPreyHandler(webapp2.RequestHandler):        
    def post(self):
        predator = self.request.get('predator')
        prey = self.request.get('prey')
        
        animal = Animal.get_by_id(int(predator), parent=PARENT)
        animal.prey.append(ndb.Key("FoodChain", 1, Animal, int(prey)))
        animal.put()
        
        self.redirect('/')
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newanimal', NewAnimalHandler),
    ('/newprey', NewPreyHandler)], debug=True)


