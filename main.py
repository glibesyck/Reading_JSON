'''
Module for discovering the .json file
'''
from os import path
import json

def get_path():
    '''
    Asks user to enter a path to the json file. Return path.
    '''
    while True:
        our_path = input('Please input the path to the file: ')
        if path.exists(our_path):
            if path.splitext(our_path)[1] == '.json':
                return our_path
            else:
                print('Wrong extension! Please input .json file!')
        else:
            print('I can\'t find this file! Please input correct path!')

def read_file(path:str) -> dict:
    '''
    Reads json file and returns a dictionary.
    '''
    file = open(path, encoding='utf-8')
    return json.load(file)

def get_categories(category:dict) :
    '''
    Print to user the information he wants.
    '''
    if isinstance(category, dict):
        print('Choose one of the following categories to discover: ')
        for key in category.keys():
            print(key)
        new_category = input('Your option: ')
        while True:
            if new_category in category.keys():
                return get_categories(category[new_category])
            else:
                new_category = input('I can\'t find such category! Please type the correct one: ')
    elif isinstance(category, list):
        print(f'Choose one the element of the list you want to see: (choose\
 from 0 to {len(category)-1}) ')
        for idx, elem in enumerate(category):
            print(idx, '-', elem)
        idx = input('Index of the element: ')
        while True:
            if idx in [str(itr) for itr in range(len(category))] :
                return get_categories(category[int(idx)])
            else :
                idx = input('I can\'t find such index! Please type the correct one: ')
    else:
        return category

if __name__ == '__main__':
    path_to_file = get_path()
    print(get_categories(read_file(path_to_file)))
    print('Thank you for using this program!')



    