import random

import wikilocation
from wikipedia import wikipedia

def get_articles(lat, lon):
    """
    :type lat: str
    :type lon: str
    :return: list of dicts representing articles
    """

    # Use really large radius, in case very far away from somewhere.
    # Results are sorted by distance and limited so that works fine.
    radius = 20000 # Upper limit
    landmark_articles = wikilocation.articles(lat, lon, radius, 10, "landmark")
    # event_articles = wikilocation.articles(lat, lon, radius, 5, "event")

    if len(landmark_articles) == 0:
        OLD_STREET_ROUNDABOUT = ("51.525603","-0.087558")
        lat, lon = OLD_STREET_ROUNDABOUT
        landmark_articles = wikilocation.articles(lat, lon, radius, 10, "landmark")

    # wikilocation_articles = event_articles + landmark_articles
    # wikilocation_articles = random.sample(wikilocation_articles, 5)
    # wikilocation_articles = _interleave(landmark_articles, event_articles)
    wikilocation_articles = landmark_articles
    wikilocation_articles = _remove_lists(wikilocation_articles)

    articles = []
    for wikilocation_article in wikilocation_articles:

        article = {}

        title = wikilocation_article["title"]
        article["title"] = title

        # first_sentence = wikipedia.summary(title, sentences=1)
        page = wikipedia.page(title)
        # article["first_sentence"] = first_sentence
        article["summary"] = page.summary

        article["image"] = "http://upload.wikimedia.org/wikipedia/commons/3/3c/Stonehenge2007_07_30.jpg"

        article["url"] = page.url

        articles.append(article)

    return articles

# def _interleave(l1, l2):
#     return [val for pair in zip(l1, l2) for val in pair]

def _remove_lists(articles):
    def not_list(article):
        return "list" not in article["title"].lower()
    return filter(not_list, articles)