import web
import json

import model
        
urls = (
    '/articles/(.+)/(.+)', 'Article'
)

class Article:
    """
    e.g. Old Street Roundabout
    GET /articles/51.525603/-0.087558
    """

    def GET(self, lat, lon):
        articles = model.get_articles(lat, lon)
        web.header('Content-Type', 'application/json')
        return json.dumps(articles)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()