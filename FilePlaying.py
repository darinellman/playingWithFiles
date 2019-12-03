

import os


for folderName, subfolders, filenames in os.walk("C:\\Users\\drnellman\\Desktop\\300 to 3k"):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
          print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for fileName in filenames:
          print('FILE INSIDE ' + folderName + ': '+ fileName)

    print('')

          
