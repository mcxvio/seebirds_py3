"""
Return previous searches from repository.
"""
#from persistence import redis_instance as connection
from flask import session

def save_previous_region(region):
    """ Try to save to redis or default to flask session. """
    region_code = region[region.find("(")+1:region.find(")")]
    #if connection.get_connection() != None:
    #    connection.save_key_value(region_code, region)
    #else:
    session[region_code] = region

def get_previous_regions():
    """ Try to retrieve from redis or default to flask session. """
    #if connection.get_connection() != None:
    #    return connection.get_values()
    #else:
    data = []
    for key in session:
        data.append(session[key])
    return data

def clear_previous_regions():
    """ Clear previously searched for terms. """
    #if connection.get_connection() != None:
    #    connection.clear_values()
    #else:
    session.clear()
