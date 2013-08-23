import unittest

import model

OLD_STREET_ROUNDABOUT = ("51.525603","-0.087558")

class Test(unittest.TestCase):

    def test(self):
        lat, lon = OLD_STREET_ROUNDABOUT
        print model.get_articles(lat, lon)

if __name__ == "__main__":
    unittest.main()