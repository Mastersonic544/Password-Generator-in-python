from tkinter import *
from tkinter import simpledialog
from secrets import *
import os

root=Tk()
root.geometry("500x400")
root.title("Password Generator 3000")
root.iconbitmap("lock.ico")

f=open("Passwords.txt",'a')

#functions

def clean(ch):
    txt=""
    for i in range(10):
        if ch[i]!='-' and ch[i]!='_':
            txt+=ch[i]
    return txt



def gen():
    random=clean(token_urlsafe(30))
    x=slide.get()
    base=ref.get()
    result=""
    match x:
        case 0: result=base.lower()
        case 1: result=base.lower()+"123"
        case 2: result=base.lower()+"1234"
        case 3: result=base.upper()+"123"
        case 4: result=base.upper()+"1234"
        case 5: result=base.capitalize()+"123@@@"
        case 6: result=base.capitalize()+"1234@@@@"
        case 7: result=base.capitalize()+random[0:2]
        case 8: result=base.capitalize()+random[0:5]
        case 9: result=random[0:7]
        case 10: result=random[0:10]

    t.set(result)
    command = 'echo ' + result.strip() + '| clip'
    os.system(command) 


def sne():
    res=t.get()
    f.write(account+" : "+res+"\n")
    root.destroy()



#Tkinter

account = simpledialog.askstring(title="Tries", prompt="Whats the passwod for ?: ")

title=Label(root, text="Password Generator", font=('Helvatical', 18, 'bold'))
expl=Label(root, text="Enter a base for the password")
ref=Entry(root)
ref.insert(0,"Yassine")
slide=Scale(root, from_=0, to=10, orient='horizontal')
slide.set(5)
gen=Button(root, text="Generate", command=gen)
se=Button(root, text="Save & Exit", command=sne)
t=StringVar()
res=Label(root, textvariable=t)


title.pack()
expl.pack()
ref.pack()
slide.pack()
gen.pack()
se.pack()
res.pack()


title.place(relx=0.5, rely=0.2, anchor='center')
expl.place(relx=0.5, rely=0.3, anchor='center')
ref.place(relx=0.5, rely=0.4, anchor='center')
slide.place(relx=0.5, rely=0.5, anchor='center')
gen.place(relx=0.4, rely=0.6, anchor='center')
se.place(relx=0.6, rely=0.6, anchor='center')
res.place(relx=0.5, rely=0.7, anchor='center')


root.mainloop()