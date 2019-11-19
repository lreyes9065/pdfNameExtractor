import PyPDF2
import os
from tkinter import *
import codecs
import sys

#utf8Writer = codecs.getwriter('utf8')
#sys.stdout = utf8Writer(sys.stdout)

mainForm = Tk(screenName='Name Extractor')
mainForm.title('Renamer')
formMenu = Menu(mainForm)
mainForm.config(menu=formMenu)
fileMenu = Menu(formMenu)
formMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open...')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=mainForm.quit)

#w = Canvas(mainForm)
btnGetFile = Button(mainForm, text='Open', width=15, command=mainForm.destroy)
btnGetFile.pack()
mainForm.mainloop()

for filename in os.listdir('ToConvert'):
    #print filename
    try:
        pdf_file = open('ToConvert/' + filename, 'rb')
    except:
        print('could not open .dsStore error')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    #print page_content
    #print '\n'
    testLines = page_content.splitlines()
    #print testLines[4] + testLines[5]
    testLine4 = testLines[4]
    if testLine4.endswith('.'):
        testLine4 = testLine4[:-1]
    testLine5 = testLines[5]
    if testLine5.endswith('.'):
        testLine5 = testLine5[:-1]
    #print testLine4
    testComplete = testLine4 + testLine5
    try:
        if testLine5 == '' or testLine5 == '' or testLine5[2] == ' ':
            testComplete = testLine4
        else:
            testComplete = testLine4 + testLine5
            testComplete = testComplete.replace('/', '')
    except:
        print('I had a problem with ' + filename)
    if 'Dear Sirs' in testComplete:
        testComplete = ''
    #print testComplete.encode('utf8')
    newFile = 'NewFile/PureProfile AUD Releases - ' + testComplete.replace('/', '') + '.pdf'
    num = 0
    while True:
        exists = os.path.isfile(newFile)
        print(newFile)
        if exists:
            num = num + 1
            newFile = 'NewFile/PureProfile AUD Releases - ' + testComplete.replace('/', '') + str(num) + '.pdf'
        else:
            break
    try:
        os.rename('ToConvert/' + filename, newFile)
        pdf_file.close()
    except:
        print(filename)
        print(newFile)
