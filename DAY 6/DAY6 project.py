#show start menu

import os
from pathlib import Path
from os import system

my_path=Path(Path.home(),'Recipes')

def count_recipes(path):
    counter=0

    for txt in Path(path).glob('**/*.txt'):
        counter+=1

    return counter



def start():
    system('cls')
    print('-'*50)
    print('!'*5 + " Welcome to the recipe book " + '!'*5)
    print('-'*50)
    print('\n')
    print(f"The recipes are in {my_path}")
    print(f"Total recipes: {count_recipes(my_path)}")

    menu_choice= 'x'
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1,7):
        print("Choose an option: ")
        print('''
        [1]-Read Recipe
        [2]-Create Recipe
        [3]-Create Category
        [4]-Delete Recipe
        [5]-Delete Category
        [6]-End Program''')
        menu_choice= input()

    return int(menu_choice)


def show_categories(path):
    print("Categories: ")
    categories_path=Path(path)
    categories_list=[]
    counter=1

    for folder in categories_path.iterdir():
        folder_str=str(folder.name)
        print(f"[{counter}] - {folder_str}")
        categories_list.append(folder)
        counter+=1

    return categories_list


def choose_categories(a_list):
    correct_choice='x'
    while not correct_choice.isnumeric() or int(correct_choice) not in range (1, len(a_list) + 1):
        correct_choice=input("\nChoose a category: ")
    return a_list[int(correct_choice)-1]


def show_recipes(path):
    print("These are the recipes: ")
    recipes_path=Path(path)
    recipes_list=[]
    counter=1

    for recipe in recipes_path.glob('*.txt'):
        recipe_str=str(recipe.name)
        print(f"[{counter}]-{recipe_str}")
        recipes_list.append(recipe)
        counter+=1

    return recipes_list



def choose_recipes(a_list):
    recipe_choice='x'
    while not recipe_choice.isnumeric() or int(recipe_choice) not in range (1, len(a_list) + 1):
        recipe_choice=input("\nChoose a recipe: ")

    return a_list[int(recipe_choice)-1]


def read_recipe(recipe):
    print(Path.read_text(recipe))




def create_recipe(path):
    exists= False

    while not exists:
        print("Write the name of your recipe: ")
        recipe_name= input() + '.txt'
        print("Write your new recipe: ")
        recipe_content= input()
        new_path=Path(path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path,recipe_content)
            print(f"Your recipe {recipe_name} has been created")
            exists=True
        else:
            print("This recipe already exists")




def create_category(path):
    exists= False

    while not exists:
        print("Write the name of the new category: ")
        category_name= input() + '.txt'
        new_path=Path(path, category_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your category {category_name} has been created")
            exists=True
        else:
            print("This category already exists")


def delete_recipe(recipe):
    Path(recipe).unlike()
    print(f"The recipe {recipe.name} has been deleted")




def return_begining():
    return_choice='x'

    while return_choice.lower() != 'b':
        return_choice=input("\nPress 'b' to return to the menu: ")



def delete_category(category):
    Path(category).rmdir()
    print(f"The category {category.name} has been removed")





finish_program=False


while not finish_program:
    menu = start()

    if menu == 1:
        # shows categories
        my_categories = show_categories(my_path)
        # choose category
        my_category = choose_categories(my_categories)
        # show recipes
        my_recipes = show_recipes(my_category)
        # choose recipes
        my_recipe = choose_recipes(my_recipes)
        # read recipe
        read_recipe(my_recipe)
        # go back to menu
        return_begining()


    elif menu == 2:
        # shows categories
        my_categories = show_categories(my_path)
        # choose category
        my_category = choose_categories(my_categories)
        # create new recipe
        create_recipe(my_category)
        # go back to menu
        return_begining()


    elif menu == 3:
        # create category
        create_category(my_path)
        # go back to menu
        return_begining()


    elif menu == 4:
        # shows categories
        my_categories = show_categories(my_path)
        # choose category
        my_category = choose_categories(my_categories)
        # show recipes
        my_recipes = show_recipes(my_category)
        # choose recipes
        my_recipe = choose_recipes(my_recipes)
        # delete recipes
        delete_recipe(my_recipe)
        # go back to menu
        return_begining()


    elif menu == 5:
        # shows categories
        my_categories = show_categories(my_path)
        # choose category
        my_category = choose_categories(my_categories)
        # delete category
        delete_category(my_category)
        # go back to menu
        return_begining()


    elif menu == 6:
        # end code
        finish_program = True






