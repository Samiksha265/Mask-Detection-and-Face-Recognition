import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os

def login():
    if v_pass.get() == "Admin@123" and v_uname.get()=="admin":
        sheets()
    else:
        tk.messagebox.showinfo('ALERT','Invalid Username or Password!')

def admin():
    m.destroy()
    global mm
    mm = tk.Tk()
    mm.title('Mask Detector and Recognizer - ADMIN LOGIN')
    canvas = Canvas(mm, width = 500, height = 350, bg = '#214B46',relief='raised')
    canvas.pack(expand=YES, fill=BOTH)
    width = mm.winfo_screenwidth()
    height = mm.winfo_screenheight()
    x = int(width / 2 - 800 / 2)
    y = int(height / 2 - 600 / 2)
    str1 = "800x600+" + str(x) + "+" + str(y)
    mm.geometry(str1)
    mm.resizable(width=False, height=False)
    mm.frame = Frame(mm, height=500, width=650, bg = '#214B46',relief='raised')
    mm.frame.place(x=80, y=50)
    x,y = 70,20
    img = PhotoImage(file='admin1.png')
    label = Label(mm, image=img)
    label.place(x=x + 250, y=y + 40)

    label = Label(mm, text="Admin Login",bg='#214B46', fg='white')
    label.config(font=("Courier", 20, 'bold'))
    label.place(x=320, y=y + 240)

    global v_uname
    global v_pass
    v_uname = StringVar()
    v_pass = StringVar()

    emlabel = Label(mm, text="USERNAME",bg='#214B46', fg='white')
    emlabel.config(font=("Courier", 14, 'bold'))
    emlabel.place(x=180, y=y + 350)

    email = Entry(mm, font='Courier 14', textvariable = v_uname, width = 27)
    email.place(x=300, y=y +350)


    pslabel = Label(mm, text="PASSWORD", bg='#214B46', fg='white')
    pslabel.config(font=("Courier", 14, 'bold'))
    pslabel.place(x=180, y=y + 400)

    password = Entry(mm, show='*', font='Courier 14',textvariable = v_pass, width=27)
    password.place(x=300, y=y + 400)

    button = Button(mm, text="Login", font='Courier 15 bold',command=login)
    button.place(x=450, y=y + 480)

    mm.mainloop()

def onClick():
    tk.messagebox.showinfo('INFO','Press "q" to close the camera!')
    os.system('python mask_face_rn.py')

def sheets():
    mm.destroy()
    global root
    root = tk.Tk()
    root.title('Mask Detector and Recognizer - Excel Files')
    canvas = Canvas(root, width = 500, height = 350, bg = '#214B46',relief='raised')
    canvas.pack(expand=YES, fill=BOTH)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = int(width / 2 - 800 / 2)
    y = int(height / 2 - 600 / 2)
    str1 = "800x600+" + str(x) + "+" + str(y)
    root.geometry(str1)
    root.resizable(width=False, height=False)
    root.frame = Frame(root, height=500, width=650, bg = '#214B46',relief='raised')
    root.frame.place(x=80, y=50)
    x,y = 70,20
    label = Label(root,text = "Select Month:",bg='#214B46', fg='white')
    label.config(font=("Courier", 12, 'bold'))
    label.place(x=x+20, y=y +80)
    global month
    month = StringVar()
    monthchoosen = ttk.Combobox(root, width = 40, textvariable=month, font=("Courier", 12, 'bold'))
    monthchoosen['values'] = ('January', 
                          'February',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September',
                          'October',
                          'November',
                          'December')
    monthchoosen.place(x = x+180, y = y+80)
    monthchoosen.current()

    label = Label(root,text = "Select Year:",bg='#214B46', fg='white')
    label.config(font=("Courier", 12, 'bold'))
    label.place(x=x+20, y=y +120)
    global year
    year = StringVar()
    yearchoosen = ttk.Combobox(root, width = 40, textvariable=year, font=("Courier", 12, 'bold'))
    yearchoosen['values'] = ('2021','2020')
    yearchoosen.place(x = x+180, y = y+120)
    yearchoosen.current()

    button = Button(root, text="SELECT", font='Courier 15 bold',command = show_sheets)
    button.place(x=350, y=y + 170)

    button = Button(root, text="LOGOUT", font='Courier 15 bold', command = logout)
    button.place(x=500, y=y + 480)
    
    root.mainloop()

def show_sheets():
    m = month.get()
    ye = year.get()
    x,y = 70,20

    global fil
    fil = StringVar()
    filechosen = ttk.Combobox(root, width=40,textvariable=fil, font=("Courier", 12, 'bold'))
    mylist = os.listdir('Fine')
    files = []
    count = 0
    for i in mylist:
        s = i.split('_')
        if s[1]==m and s[2]==ye+'.csv':
            files.append(i)
            count += 1
    if count>0:
        label = Label(root,text = "Select File:",bg='#214B46', fg='white')
        label.config(font=("Courier", 12, 'bold'))
        label.place(x=x+20, y=y +260)
        filechosen['values'] = tuple(files)
        filechosen.place(x=x+180,y=y+260)
        filechosen.current()
        
        button = Button(root, text="OPEN", font='Courier 15 bold', command = open_file)
        button.place(x=350, y=y + 320)
    else:
        tk.messagebox.showinfo('ALERT','No Files found for the entered month and year!\nTRY AGAIN!')

def open_file():
    name = fil.get()
    name = name.strip()
    os.system('start excel D:\\PROJECT\\Fine\\'+name)

def logout():
    root.destroy()
    first()

def first():
    global m 
    m = tk.Tk()
    m.title('Mask Detector and Recognizer')
    canvas = Canvas(m, width = 500, height = 350, bg = '#214B46',relief='raised')
    canvas.pack(expand=YES, fill=BOTH)
    width = m.winfo_screenwidth()
    height = m.winfo_screenheight()
    x = int(width / 2 - 800 / 2)
    y = int(height / 2 - 600 / 2)
    str1 = "800x600+" + str(x) + "+" + str(y)
    m.geometry(str1)
    m.resizable(width=False, height=False)
    m.frame = Frame(m, height=500, width=650, bg = '#214B46',relief='raised')
    m.frame.place(x=80, y=50)
    x,y = 70,20

    img = PhotoImage(file='camera.png')
    label = Button(m, image=img, command=onClick)
    label.place(x=x + 60, y=y + 175)

    label = Label(m, text="CAPTURE",bg='#214B46', fg='white')
    label.config(font=("Courier", 20, 'bold'))
    label.place(x=x+100, y=y +370)

    img1 = PhotoImage(file='admin.png')
    label = Button(m,image=img1,command = admin)
    label.place(x=x+400,y=y+175)

    label = Label(m, text="ADMIN",bg='#214B46', fg='white')
    label.config(font=("Courier", 20, 'bold'))
    label.place(x=x+450, y=y +370)
    m.mainloop()

first()

