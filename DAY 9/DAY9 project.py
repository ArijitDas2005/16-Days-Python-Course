import shutil

shutil.unpack_archive('Project+Day+9.zip', 'C:\\Users\\HP\\Downloads', 'zip')


import re
import os
import time
import datetime
from pathlib import Path
import math

start = time.time()

path = 'C:\\Users\HP\\Downloads\\My_Big_Directory'
my_pattern = r'N\D{3}-\d{5}'
today = datetime.date.today()
numbers_found = []
files_found = []


def find_number(file, pattern):
    this_file = open(file, 'r')
    text = this_file.read()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


def create_lists():
    for folder, subfolder, file in os.walk(path):
        for a in file:
            result = find_number(Path(folder,a ), my_pattern)
            if result != '':
                numbers_found.append(result.group())
                files_found.append(a.title())


def show_all():
    index = 0
    print('-' * 50)
    print(f'Date of search: {today.month}/{today.day}/{today.year}')
    print('\n')
    print('FILE\t\t\tSERIAL NUMBER')
    print('----\t\t\t-------------')
    for a in files_found:
        print(f'{a}\t{numbers_found[index]}')
        index += 1
    print('\n')
    print(f'Numbers found: {len(numbers_found)}')
    end = time.time()
    duration  = end - start
    print(f'Duration of the search: {math.ceil(duration)} seconds')
    print('-' * 50)


create_lists()
show_all()
