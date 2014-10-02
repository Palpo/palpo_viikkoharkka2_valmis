# -*- coding: utf-8 -*-

import os
import webapp2
import jinja2
import logging

from models import Animal
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        animals = [a.as_dict() for a in Animal.query()]
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({"animals": animals}))


class NewAnimalHandler(webapp2.RequestHandler):        
    def post(self):
        name = self.request.get('animal')
        
        if name:
            logging.info("New animal: %s " % name)
            animal = Animal(name=name)
            animal.put()
        
        self.redirect('/')
        

class NewPreyHandler(webapp2.RequestHandler):        
    def post(self):
        predator = self.request.get('predator')
        prey = self.request.get('prey')
        
        animal = Animal.get_by_id(int(predator))
        animal.prey.append(ndb.Key(Animal, int(prey)))
        animal.put()
        
        self.redirect('/')
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newanimal', NewAnimalHandler),
    ('/newprey', NewPreyHandler)], debug=True)


