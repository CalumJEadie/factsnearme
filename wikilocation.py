"""
Python binding for WikiLocation.

WikiLocation provides a Geolocation API for Wikipedia.

http://wikilocation.org/
"""

import requests

BASE_URL = "http://api.wikilocation.org/"

def articles(lat, lng, radius):

    payload = {
        "lat": lat,
        "lng": lng,
        "radius": radius
    }
    r = requests.get(BASE_URL+"articles", params=payload)
    articles = r.json()['articles']

    return articles