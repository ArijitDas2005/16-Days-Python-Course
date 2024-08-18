import os
# print(os.getcwd())
#
# file =open('course.txt1','w')
# file.write('test.txt')
# file.close()

import shutil
# shutil.move('course.txt2','C:\\Users\\HP\\OneDrive')


import send2trash
#send2trash.send2trash('course.txt1')

print(os.walk('C:\\Users\\HP\\OneDrive\\Documents\\Wondershare'))

path = 'C:\\Users\\HP\\OneDrive\\Documents\\Wondershare'

for folder, subfolder, file in os.walk(path):
    print(f'In folder: {folder}')
    print(f'Subfolders are: ')
    for sub in subfolder:
        print(f'\t{sub}')
    print('Files are: ')
    for fi in file:
        if fi.startswith('2015'):
            print(f'\t{fi}')
    print('\t')
