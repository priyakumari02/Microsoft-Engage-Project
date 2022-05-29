from logging import root
from tkinter import*
from tkinter import ttk
from turtle import width
from tkcalendar import Calendar, DateEntry
from time import strftime
from datetime import datetime
import mysql.connector
# for image
from PIL import Image, ImageTk
import cv2
# from login import Login
# from login import CreateAcc


class Welcome:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition Attendance System")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="#151D3B")

        title_lbl = Label(self.master, text="Welcome", font=("verdana", 40, "bold"), fg="white", bg="#151D3B")
        title_lbl.place(x=540, y=150)

        b1_1 = Button(
            self.master,
            text='Log In',
            command=self.login,
            font=('verdana', 20, 'bold'),
            padx=165,
            pady=10,
            cursor="hand2",
            bg='#7FB5FF',
            fg='white',
            activebackground='#C4DDFF',
            activeforeground='red',
            borderwidth=0,
            relief="flat", highlightthickness=0,
        ).place(x=480, y=300)

        b1_2 = Button(
            self.master,
            text='Create Account',
            command=self.createacc,
            font=('verdana', 20, 'bold'),
            padx=80,
            pady=10,
            cursor="hand2",
            bg='#7FB5FF',
            fg='white',
            activebackground='#C4DDFF',
            activeforeground='red',
            borderwidth=0,
            relief="flat", highlightthickness=0,
        ).place(x=480, y=410)

    def login(self):
        self.new_window = Toplevel(self.master)
        self.app = Login(self.new_window)  

    def createacc(self):
        self.new_window = Toplevel(self.master)
        self.app = CreateAcc(self.new_window)        

if __name__ == "__main__":
    master = Tk()
    obj = Welcome(master)
    master.mainloop()  
