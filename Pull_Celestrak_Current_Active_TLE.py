import os
import pprint
import Tkinter
import time
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import Tk
import tkMessageBox
import tkSimpleDialog
from datetime import datetime
import subprocess
import sys
try:
    import requests
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

now = datetime.now()
now_correct = now.strftime("%Y_%m_%d_%H_%M_%S")
root = Tk()
root.wm_attributes('-topmost', 1)
result = tkMessageBox.askyesno("Python",'''Hello, welcome to the automatic 3 line element set downloader developed by Joshua Vaughan, TSOC Instructor.\n
This program will only work on the NIPRnet and will download a new and delightful copy of all the active satellites being tracked by Celestrak.com.\n
If you are on NIPRnet and have an active internet connection click yes to continue.
''')

if result == True:
    pass
else:
    tkMessageBox.showinfo ("Program Aborted","You have chosen No, the program will now exit.")
    os._exit(0)

result = tkMessageBox.askyesno("File Directory",'You will now select where you want your new TLE file to be saved. \
\nWhen you click "Yes" a box will pop up and you will use that to select where you want your new TLE file to be saved. \
\nIf you do not understand click "No" and the program will be terminated.')

if result == True:
    pass
else:
    tkMessageBox.showinfo ("Program Aborted","You have chosen No, Please get the requisite understanding of file directory selection and run this program again. Thank You.")
    os._exit(0)


directory = tkFileDialog.askdirectory()

os.chdir(directory)


answer = tkSimpleDialog.askstring('File Name', '''Please Enter the name for your Celestrak TLE, if you leave it empty an automatically chosen name will be generated.\n
Do not enter in the file extension ".txt" or the program will break, simply enter in the name of the file you would prefer.''')

if answer != '':
    pass
else:
    answer = 'Celestrak_TLE_All_Active' + str(now_correct)

res = requests.get('https://celestrak.com/NORAD/elements/active.txt')

if res.status_code == requests.codes.ok:
    pass
else:
    tkMessageBox.showinfo("Program Aborted",'''Celestrak has returned an error on its website.  Please manually check https://celestrak.com/NORAD/elements/active.txt and see if it resolves.\
if it does, try running this program again.  If not please check your internet connection and anything else that might cause an issue reaching\
a webpage and run this program again.  Thank you''')
    os._exit(0)

write_file = open('placeholder.txt', 'w+')

for line in res.iter_content(80):
    write_file.write(line)

write_file.close()

remake_list = []

with open('placeholder.txt', 'r') as f:
    remake = f.readlines()

for line in remake:
    if line != '':
        remake_list.append(line.strip() + '\n')
    else:
        continue

write_file_final = open(str(answer) + '.txt', 'w+')

for s in remake_list:
    write_file_final.write(s)

os.remove('placeholder.txt')


write_file_final.close()
root.destroy()


tkMessageBox.showinfo("Program Completed",'''The program is now complete.  If you are seeing this message that means it all went well
and there will be a new 3 line element set sitting in the directory you chose at the beginning of this program.  That is a copy of the most 
recent Celestrak.com data directly from their website.  Please click ok to close this program.''')

os._exit(0)