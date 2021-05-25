import spoonacular as sp
import PySimpleGUI as sg
import webbrowser as wb

api_key = "15f1634e59b646a2b48daa73b56b86af"
api = sp.API(api_key)

def main_window():
    '''
    This function will display a window in which the user specifies the ingredients they wish to find a recipe for.
    In communication with the find_recipes function this function then outputs the top 10 options of recipes with
    the chosen ingredients. The user can then choose which one they would like to view.
    When they choose a recipe and click 'ok' the link to that recipe will open in their browser.

    layout_window defines the layout of the main window.
    :return:
    '''

    layout_window = [
            [sg.Text('What ingredients would you like to use? (please separate with a comma):')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Listbox([],size = (60,20), auto_size_text=True, key='-OUTPUT-')],
            [sg.Button('Find Recipes')]
            ]
    window = sg.Window('Recipe Finder', layout_window)

    #Intialize ingredients list
    ingredients = []

    #Main window loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok':
            ingredients = values[0].split(',')
            recipes_dict = find_recipes(ingredients)
            window['-OUTPUT-'].update(list(recipes_dict.keys()))
        if event == 'Find Recipes':
            chosen = values['-OUTPUT-'][0]
            chosen_id = recipes_dict[chosen]
            recipe_link(chosen_id)

def find_recipes(ingredients):
    '''
    This function searches for recipes based on the input ingredients.
    :param ingredients:
    :return:
    '''

    response = api.search_recipes_by_ingredients(ingredients, ranking=2)
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
    :param id:
    :return:
    '''
    response = api.get_recipe_information(id)
    data = response.json()
    wb.open((data['sourceUrl']))

main_window ()




