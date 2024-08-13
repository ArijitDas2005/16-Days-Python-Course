#from pathlib import Path
#folder= Path('C:/Users/HP/OneDrive/Desktop/Python Course/DAY 6/test.txt')
#print(folder.read_text())
#print('\n')
#print(folder.name)
#print(folder.suffix)
#print(folder.stem)

#if not folder.exists():
    #print("This doesn't exists")
#else:
    #print("YES. This file exists.")






from pathlib import Path, PureWindowsPath

folder = Path('C:\\Users\\HP\\OneDrive\\Desktop\\Python Course\\DAY 6\\test.txt')

windows_path = PureWindowsPath(folder)

print(windows_path)