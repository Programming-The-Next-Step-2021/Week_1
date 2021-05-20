import spoonacular as sp
api = sp.API("15f1634e59b646a2b48daa73b56b86af")

# Search recipe by ingredients
#all api functions found at link below
# https://spoonacular.com/food-api/docs
# Todo: add argument & choice to not have pantry items
#Todo: store all in one function?

ingredients = input('What are the ingredients youd like to use?')
response = api.search_recipes_by_ingredients(ingredients, ranking=2)
#ignore typical pantry items: ignorePantry=True
data = response.json()
recipeList = []
recipeID = []

#Todo: store the name of each recipe in choice list
for i in range(len(data)):
    recipeList += [data[i]['title']]
    recipeID += [data[i]['id']]

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
#open recipe URL
import webbrowser
webbrowser.open((moredata['sourceUrl']))





