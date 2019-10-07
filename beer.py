#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
A program which uses the BreweryDB API http://www.brewerydb.com/developers 
that shows the beers in the database for the beer kind the user requested. 
The fields: BreweryDb.search({'type':'beer','q':'unibroue'}
'''

import json
import requests
import urllib
from brewerydb import *
import brewerydb
from brewerydb.brewerydb import BreweryDB


DEFAULT_BASE_URI = "http://api.brewerydb.com/v2"
BASE_URI = DEFAULT_BASE_URI
API_KEY = "key"

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

x = raw_input("Give name of category you want to search for ")
brew_api = BreweryDB('key')
#beers = brew_api.search_beer('fat tire')
beers = brew_api.search_beer(x)
#x= brew_api.search_categories.json()
print beers

