from tkinter import filedialog
from tkinter import *
from zipfile import *
from pathlib import Path

root = Tk()
root.title('py_zipper_unzipper')

label1=Label(root,text='zipfile name').grid(row = 0,column = 0)
text1= Entry(root,width=40)
text1.grid(row = 0,column = 1,pady=10)

text = '''click (save to save_to_desktoptop) OR
            (add last address) OR
            (add new address)-to 
            add address manually
            and save it'''

label2=Label(root,text=text).grid(row = 1,column = 0)
text2= Entry(root,width=40)
text2.grid(row = 1,column = 1,pady=10)


def zip(list,address):
    z = ZipFile(address, 'a')
    z.write(list,compress_type=ZIP_LZMA)


def address():
    c_address1 = str(text1.get())
    c_address2 = str(text2.get())
    address = c_address2 + c_address1
    filez = filedialog.askopenfilenames(parent=root, title='Choose your files to be zipped')
    lists = list(filez)
    l = len(lists)
    for i in range(0, l):
        zip(lists[i],address)


def unzip():
    import zipfile
    tkaddunzip()
    z = zipfile.ZipFile(root.filename, 'r')
    c_address1 = str(text1.get())
    c_address2 = str(text2.get())
    address = c_address2 + c_address1
    import os
    mypath = address
    if not os.path.isdir(mypath):
        os.makedirs(mypath)

    os.chdir(address)
    z.extractall()
    print('work done! so click close button')


def tkaddunzip():
    root.filename = filedialog.askopenfilename(initialdir="Desktop", title="Select file to be unzipped",
                                               filetypes=(("zip files", "*.zip"), ("all files", "*.*")))

def close():
    root.destroy()

def last_address():
    f = open((str(Path.home()) + '\Desktop' + '\\'+'address.txt'),'r+')
    last = f.read()
    text2.delete(0,'end')
    text2.insert(0,last)

def add_new_address():
    f1 = open((str(Path.home()) + '\Desktop' + '\\'+'address.txt'),'w+')
    c_address2 = str(text2.get())
    text2.delete(0, 'end')
    text2.insert(0,c_address2)
    address = c_address2
    f1.write(address)
    f1.close()


def save_to_desktop():
    address = (str(Path.home()) + '\Desktop' + '\\')
    text2.delete(0,'end')
    text2.insert(0,address)

button1 = Button(root,text = 'zip',command = address,width=20)
button1.grid(row = 2, column = 0,pady=5)

button2 = Button(root,text = 'unzip',command = unzip,width=20)
button2.grid(row = 2, column = 1,padx=5,pady=5)

button3 = Button(root,text = 'close',command = close,width=20)
button3.grid(row = 2, column = 2,pady=5)

button6 = Button(root,text = 'save to Desktop',command = save_to_desktop,width=20)
button6.grid(row = 3, column = 0,pady=5)

button4 = Button(root,text = 'add last address',command = last_address,width=20)
button4.grid(row = 3, column = 1,pady=5)

button5 = Button(root,text = 'add new address',command = add_new_address ,width=20)
button5.grid(row = 3, column = 2,pady=5)

root.mainloop()
