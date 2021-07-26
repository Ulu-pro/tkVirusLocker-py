from tkinter import *
from tkinter import messagebox
pwd = '0123'
def btn_click():
    k = inp.get()
    if k == pwd:
        tk.destroy()
    else:
        messagebox.showwarning(title='Error',message='Wrong password\nTry again'+('-'*10)+'\nby Ulugbek')
def exits():
    if inp.get() != pwd:
        messagebox.showwarning(title='Error',message='For exit enter password\n'+('-'*10)+'\nby Ulugbek')
tk = Tk()
tk.title('PC blocked')
tk.geometry('400x150')
tk['bg'] = '#000'
tk.resizable(False,False)
tk.protocol('WM_DELETE_WINDOW',exits)
Label(tk,text='Enter password:',font='Consolas 20',bg='#000',fg='#fff').pack()
inp = Entry(tk,font='Consolas 25')
inp.pack()
Button(tk,text='OK',font='Consolas 25',bg='#0aa',fg='#fff',command=btn_click).pack()
tk.mainloop()