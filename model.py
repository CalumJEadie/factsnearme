import random

import wikilocation
from wikipedia import wikipedia

def get_articles(lat, lon):
    """
    :type lat: str
    :type lon: str
    :return: list of dicts representing articles
    """

    landmark_articles = wikilocation.articles(lat, lon, 1000, 5, "landmark")
    event_articles = wikilocation.articles(lat, lon, 1000, 5, "event")

    # wikilocation_articles = event_articles + landmark_articles
    # wikilocation_articles = random.sample(wikilocation_articles, 5)
    wikilocation_articles = _interleave(landmark_articles, event_articles)

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

def _interleave(l1, l2):
    return [val for pair in zip(l1, l2) for val in pair]