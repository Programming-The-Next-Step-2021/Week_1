#asking for available ingredients"""
ingredients = input("what ingredients do you have available? (please seperate each with a comma)")
print ('okay let me check what recipes we have available with', ingredients, '...')


#importing recipes and store in dict varibale
import csv
recipes = csv.DictReader(open('recipes.csv'))
for row in recipes:
    print(row)

def recipes(documentation):
""" Description of the function
Input:
Ingredients that are available to user

Output:
All recipes that require only those ingredients

"""
    return documentation


