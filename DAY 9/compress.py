'''import zipfile

# my_zip = zipfile.ZipFile('file_compressed.zip','w')
# my_zip.write('My_Text_A.txt')
# my_zip.write('My_Text_B.txt')
# my_zip.close()

open_zip = zipfile.ZipFile('file_compressed.zip','r')
open_zip.extractall()'''


# # import shutil
# #
# # source_folder = 'C:\\Users\\HP\\OneDrive\\Desktop\\Static'
# # destination_file = 'all_compressed'
# # shutil.make_archive(destination_file, 'zip', source_folder)
# #
# shutil.unpack_archive('all_compressed.zip', 'extraction_finished', 'zip')