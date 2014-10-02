# -*- coding: utf-8 -*-

import os
import webapp2
import jinja2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        
        # Placeholder:
        animals = [{"id": 1, "name": "Leijona", "prey": ["Antilooppi"]},
                   {"id": 2, "name": "Antilooppi", "prey": []}]
        
        # TODO
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({"animals": animals}))


class NewAnimalHandler(webapp2.RequestHandler):        
    def post(self):
        name = self.request.get('animal')
        
        if name:
            logging.info("New animal: %s " % name)
            
            # TODO
        
        self.redirect('/')
        

class NewPreyHandler(webapp2.RequestHandler):        
    def post(self):
        predator = self.request.get('predator')
        prey = self.request.get('prey')
        
        logging.info("%s eats %s" % (predator, prey))
        
        # TODO
        
        self.redirect('/')
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newanimal', NewAnimalHandler),
    ('/newprey', NewPreyHandler)], debug=True)


