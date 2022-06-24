from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     #pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file="/Users/Arun/Desktop/HOTEL MANAGEMENT SYSTEM/IMAGES/Background.webp")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("/Users/Arun/Desktop/HOTEL MANAGEMENT SYSTEM/IMAGES/login.jpeg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started", font=("times new roman",27,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #================Icon Images=============
        img2=Image.open("/Users/Arun/Desktop/HOTEL MANAGEMENT SYSTEM/IMAGES/login.jpeg")
        img2=img1.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open("/Users/Arun/Desktop/HOTEL MANAGEMENT SYSTEM/IMAGES/password.webp")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="blue",activeforeground="black",activebackground="blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=12,y=350,width=160)

         #forgetpass button
        registerbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=10,y=370,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get()=="sssss" and self.txtpass.get()=="12345":
               messagebox.showinfo("Success", "Welcome to Sunshine Hotel")
        else:
            messagebox.showerror("Invalid","Invalid Username & Password")

            #================print row==========
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
