"""
Python binding for WikiLocation.

WikiLocation provides a Geolocation API for Wikipedia.

http://wikilocation.org/
"""

import requests

BASE_URL = "http://api.wikilocation.org/"

def articles(lat, lng, radius, limit, type_):
    """
    Returns nearby Wikipedia articles sorted by distance.
    """

    articles = []

    payload = {
        "lat": lat,
        "lng": lng,
        "radius": radius,
        "limit": limit,
        "type": type_
    }
    r = requests.get(BASE_URL+"articles", params=payload)
    articles = r.json()['articles']

    return articles