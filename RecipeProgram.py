recipeList = {'omellete':{'ingredients':'eggs, milk','directions':'fry'},
              'pancake':{'ingredients':'pancake mix','directions':'cook'}
              }
'''
Data Structure
recipeList = [recipe1, recipe2, recipeN]
recipeN = [ingredients,directions]
recipe ingredients = recipeList['recipeN']['ingredients']
recipe directions = recipeList['recipeN']['directions']
'''
def showRecipes(recipes,ingredients):
    for rec in recipes:
        if ingredients == recipes[rec]['ingredients']:
            print('Recipes with these ingredients:')
            print(rec)

def showDirections(recipes,choice):
    for rec in recipes:
        if choice == rec:
            print('Directions:')
            print(recipes[rec]['directions'])

inputIngredients = input('Enter your ingredients separated by a comma:')
showRecipes(recipeList,inputIngredients)

recipeChoice = input('Choose a recipe  to view directions:')
showDirections(recipeList,recipeChoice)

#for unittest
def sum():
