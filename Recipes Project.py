import spoonacular as sp
import PySimpleGUI as sg
import webbrowser as wb
api = sp.API("15f1634e59b646a2b48daa73b56b86af")

#all api functions found at link below
# https://spoonacular.com/food-api/docs
# Todo: add argument & choice to not have pantry items

def main_window():
    '''
    This function will display a window in which the user specifies the ingredients they wish to find a recipe for.
    :return:
    '''


    #Layout
    layout_window = [
            [sg.Text('What ingredients would you like to use? (please separate with a comma):')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Listbox([],size = (40,20), auto_size_text=True, key='-OUTPUT-')],
            [sg.Button('Open Recipe Link')]
            ]
    window = sg.Window('Find recipes with what\'s in your kitchen!', layout_window)

    #Intialize ingredients list
    ingredients = []


    #Main window loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Ok': #If Ok clicked create list with ingredients entered
            ingredients = values[0].split(',')
            recipes_dict = get_recipes(ingredients)
            window['-OUTPUT-'].update(list(recipes_dict.keys()))
        if event == 'Open Recipe Link':
            #get_url(id) Todo

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





