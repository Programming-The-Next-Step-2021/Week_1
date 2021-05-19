import spoonacular as sp
api = sp.API("15f1634e59b646a2b48daa73b56b86af")

# Search recipe by ingredients
#all api functions found at link below
# https://spoonacular.com/food-api/docs
# Todo: add argument & choice to not have pantry items

def get_ingredients():
    ingredients = input("what ingredients do you have available? (please seperate each with a comma)")
    print ('okay let me check what recipes we have available with', ingredients, '...')
#Todo: add error message for incorrect input

def find_recipe():

    '''
    In this function the recipes in the Spoonacular Database
    with the input ingredients are found and stored in a list.

    recipeList is the list of all the suiting recipes.
    recipeID is the ID number associated with the recipe from the databank.
    '''

    response = api.search_recipes_by_ingredients(ingredients, ranking=2)
    data = response.json()
    recipeList = []
    recipeID = []
#Todo: store the name of each recipe in choice list

for i in range(len(data)):
    recipeList += [data[i]['title']]
    recipeID += [data[i]['id']]

def choose_recipe():
    '''
    In this fuction the user can input the number associated with the recipe theu wish to view the directions for.
    The fucntion will then redirect them to the chosen recipe.
    :return:
    '''
#todo: make the recipe link open after choice
#display the recipes list
choice = 1
for entry in recipeList:
    print(str(choice) +'. ' + entry)
    choice += 1

chosen = input('Please enter the number of the recipe you wish to view the directions for: \n')
chosen = int(chosen)-1
recipeChoice = recipeID[chosen]
#recipeChoice = data[chosen]['id']

moreresponse = api.get_recipe_information(recipeChoice)
moredata = moreresponse.json()
print(moredata['sourceUrl'])
