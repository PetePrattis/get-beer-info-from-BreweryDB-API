#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
A program which uses the BreweryDB API http://www.brewerydb.com/developers 
that shows the beers in the database for the beer kind the user requested. 
The fields: BreweryDb.search({'type':'beer','q':'unibroue'}
'''

'''
Within this archive there is extra code with which I experimented... not functional.
'''

import json
import requests
import urllib
from brewerydb import *
import brewerydb
from brewerydb.brewerydb import BreweryDB
from .beer import Beer, Beers
from .brewery import Brewery, Breweries



BASE_URL = 'http://api.brewerydb.com/v2'


class BreweryDB(object):

    resource_url = 'http://api.brewerydb.com/v2'

    def __init__(self, data):
        self.data = data

    def __unicode__(self):
        return self.name

    
    @property
    def description(self):
        """ Returns the description of the brewery """
        return self.data.get('description', None)



    def __init__(self, api_key="47f25f72907f1924061a1ee9b57d6f10"):
        self.api_key = api_key
        
    def _auth(self):
        return "47f25f72907f1924061a1ee9b57d6f10=%s" % self.api_key
        
    def _call(self, resource_url, params=None):
        url = "%s/%s" % (BASE_URL, resource_url)
        if params:
            url += "?%s&%s" % (params, self._auth())
        else:
            url += "?%s" % self._auth()
        
        return requests.get(url)
    
    def _params(self, params):
        """
        Takes dictionary of parameters and returns
        urlencoded string
        :param params: Dict of query params to encode
        :type params: dict
        
        :returns:  str -- URL encoded query parameters
        """
        return urllib.urlencode(params)
    
    def search_beer(self, beer_name='fat tire'):
        """ Search the BreweryDB for a beer.  Returns a
        list of Beer objects.
        
        get /beers/
        
        :param beer_name: Query of the beer to search for
        :type params: string
        
        :returns:  List of Beer objects
        
        """
        response = json.loads(self._call("search", self._params(params={'q': beer_name, 'withBreweries': 'Y', 'type': 'beer'})).text)
        beers = []
        for beer in response['data']:
            beers.append(Beers(beer))
        return beers
        
    def get_beer(self, id):
        """Fetches a single beer by id.
        get /beer/<id>/
        :param id: ID of beer
        :type params: int
        
        :returns:  Beer object
        """        
        response = json.loads(self._call("%s/%s" % (Beer.resource_url, id), self._params({'withBreweries': 'Y'})).text)
        return Beer(response['data'])
        
    def search_breweries(self, brewery_name):
        """Fetches a single brewery by id.
        get /breweries/
        :param brewery_name: Search query for breweries
        :type params: string
        
        :returns:  List of brewery objects
        """
        response = json.loads(self._call('search', self._params(params={'q': brewery_name, 'type': 'brewery'})).text)
        breweries = []
        for brewery in response['data']:
            breweries.append(Brewery(brewery))
        return breweries
    
    def get_brewery(self, id):
        """Fetches a single character by id.
        get /brewery/<id>/
        :param id: ID of Brewery
        :type params: int
        
        :returns:  Brewery object
        """
        response = json.loads(self._call("%s/%s" % (Brewery.resource_url, id)).text)
        return Brewery(response['data'])


DEFAULT_BASE_URI = "http://api.brewerydb.com/v2"
BASE_URI = DEFAULT_BASE_URI
API_KEY = "47f25f72907f1924061a1ee9b57d6f10"

simple_endpoints = ["beers", "breweries", "categories", "events",
                    "featured", "features", "fluidsizes", "glassware",
                    "locations", "guilds", "heartbeat", "ingredients",
                    "search", "search/upc", "socialsites", "styles"]

single_param_endpoints = ["beer", "brewery", "category", "event",
                          "feature", "glass", "guild", "ingredient",
                          "location", "socialsite", "style", "menu"]




class BreweryDb:


    @staticmethod
    def __make_simple_endpoint_fun(name):
        @staticmethod
        def _function(options={"categories"}):
            print BreweryDb._get("/" + name, options)
            return BreweryDb._get("/" + name, options)
        return _function

    @staticmethod
    def __make_singlearg_endpoint_fun(name):
        @staticmethod
        def _function(id, options={}):
            print BreweryDb._get("/" + name + "/" + id, options)
            return BreweryDb._get("/" + name + "/" + id, options)
        return _function

    @staticmethod
    def _get(request, options):
        options.update({"key" : BreweryDb.API_KEY})
        
        return requests.get(BreweryDb.BASE_URI + request, params=options).json()

    @staticmethod
    def configure(apikey=API_KEY, baseuri=DEFAULT_BASE_URI):
        BreweryDb.API_KEY = apikey
        BreweryDb.BASE_URI = baseuri
        for endpoint in simple_endpoints:
            fun = BreweryDb.__make_simple_endpoint_fun(endpoint)
            setattr(BreweryDb, endpoint.replace('/', '_'), fun)
        for endpoint in single_param_endpoints:
            fun = BreweryDb.__make_singlearg_endpoint_fun(endpoint)
            setattr(BreweryDb, endpoint.replace('/', '_'), fun)

#configure(API_KEY, DEFAULT_BASE_URI);
x = raw_input("Give name of category you want to search for ")
brew_api = BreweryDB('47f25f72907f1924061a1ee9b57d6f10')
#beers = brew_api.search_beer('fat tire')
beers = brew_api.search_beer(x)
print beers
#x= brew_api.search_categories.json()

#print beers


style('Fat Tire');
@property
def style(self):
    """ Returns the name of the style                           
    category that this beer belongs to."""
    style = self.data.get('style', None)
    if style:
        return style['category']['name']
    else:
        return None
print style('Fat Tire')




class Beer(object):
    resource_url = x
    
    def __init__(self, data):
        self.data = data

    def __unicode__(self):
        return self.name
