'''
This is the user interface of the program
'''

import PySimpleGUI as sg

sg.theme('Kayak')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Lets find you a recipe')],
            [sg.Text('What ingredients would you like to use? (please seperate with a comma)'), sg.InputText()],
            [sg.Button('Search'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('RecipeFinder', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()