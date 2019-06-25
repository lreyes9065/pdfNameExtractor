import PyPDF2
import os
import re

for filename in os.listdir('NewFile'):
    newFileName = ''
    letterOld = ''
    print filename
    for letter in filename:
        letterOld = letter
        if letterOld != ' ' and letter != ' ':
            newFileName += letter
        else:
            break
    print newFileName
