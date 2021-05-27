import csv
import spoonacular as sp
import PySimpleGUI as sg
import webbrowser as wb

api_key = "15f1634e59b646a2b48daa73b56b86af"
api = sp.API(api_key)

layout_window = [
        [sg.Text('What ingredients would you like to use? (please separate with a comma):')],
        [sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')],
        [sg.Listbox([],size = (60,20), auto_size_text=True, key='-OUTPUT-')],
        [sg.Button('Open')]
        ]
window = sg.Window('Recipe Finder', layout_window)

def main_loop():
    '''
    This function takes the user input from the main window and creates the flow of the window in communication with other functions.
    In communication with the find_recipes function this function then outputs the top 10 options of recipes with
    the chosen ingredients. The user can then choose which one they would like to view.
    When they choose a recipe and click 'ok' the link to that recipe will open in their browser, this is done in communication with
    the recipe_link(id) function.

    ingredients = will be filled by the input text of the user.
    chosen = will be filled by the recipe choice the user makes.
    chosen_id = assigns the ID associated with the chosen recipe in the API.

    '''

    ingredients = []
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            ingredients = values[0]
            recipes_dict = find_recipes(ingredients)
            window['-OUTPUT-'].update(list(recipes_dict.keys()))
        if event == 'Open':
            chosen = values['-OUTPUT-'][0]
            chosen_id = recipes_dict[chosen]
            recipe_link(chosen_id)

def find_recipes(ingredients):
    '''
    This function searches for recipes based on the input ingredients.

    response = communicates with the API to search recipes by ingredients.
    recipe_name = will be filled based on the recipes found.
    recipe_id = will be filled based on the recipes found.
    ranking = 1 defines the way the recipes are sorted (in this case by minimizing additional ingredients).
    '''
    response = api.search_recipes_by_ingredients(ingredients, ranking=1)
    api.search_recipes_by_ingredients(ingredients)
    data = response.json()
    recipe_name = []
    recipe_id = []

    for i in range(len(data)):
        recipe_name += [data[i]['title']]
        recipe_id += [data[i]['id']]
    recipe_dict = dict(zip(recipe_name, recipe_id))
    return recipe_dict

def recipe_link(id):
    '''
    This function opens the link associated with the chosen recipe through its ID number.

    'sourceUrl' will be the url of the chosen recipe.
    '''
    response = api.get_recipe_information(id)
    data = response.json()
    wb.open((data['sourceUrl']))
    return data['sourceUrl']

main_loop()
