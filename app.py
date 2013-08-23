import web
import json
        
urls = (
    '/articles/(.+)/(.+)', 'Article'
)

class Article:
    """
    e.g. Old Street Roundabout
    GET /articles/51.525603/-0.087558
    """

    def GET(self, lat, lon):

        articles = [
            {
                "title": "Stonehenge",
                "first_sentence": "Stonehenge is a prehistoric monument in Wiltshire, England, about 2 miles (3.2 km) west of Amesbury and 8 miles (13 km) north of Salisbury.",
                "image": "http://upload.wikimedia.org/wikipedia/commons/3/3c/Stonehenge2007_07_30.jpg"
            }
        ]
        web.header('Content-Type', 'application/json')
        return json.dumps(articles)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()