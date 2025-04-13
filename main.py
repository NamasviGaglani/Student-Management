from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields Cannot Be Empty')
    elif usernameEntry.get()=='John' and passwordEntry.get()=='1234':
        messagebox.showinfo('successfully Logined','Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please Enter Correct Credentials')
window=Tk()
window.geometry('1000x750+0+0')
window.title('Login System Of Student Management System') 
window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window, image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg='white')
loginFrame.place(x=300, y=150)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame, image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage, text='Username', compound=LEFT, font=('times new roman',15,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman',10,'bold'), bd=2, fg='grey')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)
passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage, text='Password', compound=LEFT, font=('times new roman',15,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20) 
passwordEntry=Entry(loginFrame,font=('times new roman',10,'bold'), bd=2, fg='grey')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)
loginButton=Button(loginFrame, text='Login', font=('times new roman',10,'bold'), width=15, fg='white', bg='black', cursor='hand2', command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()
