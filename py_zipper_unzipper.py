from tkinter import filedialog
from tkinter import *
from zipfile import *
from pathlib import Path

root = Tk()
root.title('py_zipper_unzipper')

l1=Label(root,text='unzip/zip file name: ').grid(row = 0,column = 0)
t1= Entry(root,width=40)
t1.grid(row = 0,column = 1,pady=10)

text = '''click (save to desktop) OR
            (add last address) OR
            (add new address)-to 
            add address manually
            and save it'''

l2=Label(root,text=text).grid(row = 1,column = 0)
t2= Entry(root,width=40)
t2.grid(row = 1,column = 1,pady=10)


def zip(list,address):
    z = ZipFile(address, 'a')
    z.write(list, compress_type=ZIP_LZMA)


def add():
    c_address1 = str(t1.get())
    c_address2 = str(t2.get())
    address = c_address2 + c_address1
    filez = filedialog.askopenfilenames(parent=root, title='Choose your file to be zipped')
    lists = list(filez)
    l = len(lists)
    for i in range(0, l):
        zip(lists[i],address)
    print('work done! so you can click close button')

def unzip():
    import zipfile
    tkaddunzip()
    z = zipfile.ZipFile(root.filename, 'r')
    c_address1 = str(t1.get())
    c_address2 = str(t2.get())
    address = c_address2 + c_address1
    import os
    mypath = address
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    os.chdir(address)
    z.extractall()
    print('work done! so you can click close button')


def tkaddzip():
    root.filename = filedialog.askopenfilename(initialdir="Desktop", title="Select file",
                                               filetypes=(("all files", "*.*"),("pdf files", "*.pdf")))

def tkaddunzip():
    root.filename = filedialog.askopenfilename(initialdir="Desktop", title="Select file",
                                               filetypes=(("zip files", "*.zip"), ("all files", "*.*")))

def close():
    root.destroy()

def lastadd():
    f = open((str(Path.home()) + '\Desktop' + '\\'+'address.txt'),'r+')
    last = f.read()
    t2.delete(0,'end')
    t2.insert(0,last)

def addaddress():
    address = str(t1.get())
    c_address2 = str(t2.get())
    f1 = open((str(Path.home()) + '\Desktop' + '\\'+'address.txt'),'w+')
    t2.delete(0, 'end')
    t2.insert(0,c_address2)
    address = c_address2
    f1.write(address)
    f1.close()


def desk():
    address = (str(Path.home()) + '\Desktop' + '\\')
    t2.delete(0,'end')
    t2.insert(0,address)

b1 = Button(root,text = 'zip',command = add,width=20)
b1.grid(row = 2, column = 0,pady=5)

b2 = Button(root,text = 'unzip',command = unzip,width=20)
b2.grid(row = 2, column = 1,padx=5,pady=5)

b3 = Button(root,text = 'close',command = close,width=20)
b3.grid(row = 2, column = 2,pady=5)

b6 = Button(root,text = 'save to desktop',command = desk,width=20)
b6.grid(row = 3, column = 0,pady=5)

b4 = Button(root,text = 'add last address',command = lastadd,width=20)
b4.grid(row = 3, column = 1,pady=5)

b5 = Button(root,text = 'add new address',command = addaddress ,width=20)
b5.grid(row = 3, column = 2,pady=5)

root.mainloop()
