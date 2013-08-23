import unittest

import model
import wikilocation

OLD_STREET_ROUNDABOUT = ("51.525603","-0.087558")

class Test(unittest.TestCase):

    def test_model_get_articles(self):
        lat, lon = OLD_STREET_ROUNDABOUT
        print model.get_articles(lat, lon)

    def test_wikilocation_articles(self):
        lat, lng = OLD_STREET_ROUNDABOUT
        radius = 1000
        limit = 10
        type_ = "landmark"
        print wikilocation.articles(lat, lng, radius, limit, type_)

if __name__ == "__main__":
    unittest.main()