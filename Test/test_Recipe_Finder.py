import unittest
from Recipe_Finder import find_recipes, recipe_link

class TestRecipeFinder(unittest.TestCase):
    def test_find_recipes(self):
        recipes = find_recipes('eggs,bacon,cheese')
        self.assertIsNotNone(recipes,'no recipes')

    def test_recipe_link(self):
        link = recipe_link('716429')
        self.assertEqual(self, link, 'https://fullbellysisters.blogspot.com/2012/06/pasta-with-garlic-scallions-cauliflower.html' )


if __name__ == '__main__':
    unittest.main()
