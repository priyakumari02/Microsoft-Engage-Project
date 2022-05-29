from tkinter import*
from tkinter import ttk
# for image
from PIL import Image, ImageTk
from attendance import Attendance
from studentdetails import Student_Details
import os
from facerecognition import Face_Recognition
from train import Train
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition Attendance System")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="#151D3B")

        title_lbl = Label(self.master, text="Easy Attendance ", font=(
            "verdana", 40, "bold"), fg="white", bg="#151D3B")
        title_lbl.pack(side=TOP, fill=X)
        b1_1 = Button(
            self.master,
            text='Student Details',
            command=self.student,
            font=('Roboto Mono', 20, 'bold'),
            padx=80,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='darkblue',
            activeforeground='white',
            borderwidth=0,
            relief="flat", highlightthickness=0,
        ).place(x=500, y=180)

        b1_2 = Button(
            self.master,
            text='Train Dataset',
            command=self.train,
            font=('Roboto Mono', 20, 'bold'),
            padx=90,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=500, y=265)

        b1_3=Button(
            self.master,
            text='Attendance',
            command=self.attendance,
            font=('Roboto Mono', 20, 'bold'),
            padx=103,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=500, y=445)

        b1_5=Button(
            self.master,
            text='Track Face',
            command=self.face_recognition,
            font=('Roboto Mono', 20, 'bold'),
            padx=105,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=500, y=355)

        b1_6=Button(
            self.master,
            text='Photos',
            command=self.open_img,
            font=('Roboto Mono', 20, 'bold'),
            padx=130,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=500, y=535)

        b1_7=Button(
            self.master,
            text='Exit',
            command=master.destroy,
            font=('Roboto Mono', 20, 'bold'),
            padx=152,
            pady=10,
            cursor="hand2",
            bg='Red',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=500, y=625)

    def open_img(self):
        os.startfile("data")


#Function Buttons

    def student(self):
        self.new_window = Toplevel(self.master)
        self.app = Student_Details(self.new_window)

    def train(self):
        self.new_window = Toplevel(self.master)
        self.app = Train(self.new_window) 

    def face_recognition(self):
        self.new_window = Toplevel(self.master)
        self.app = Face_Recognition(self.new_window) 

    def attendance(self):
        self.new_window = Toplevel(self.master)
        self.app = Attendance(self.new_window)          
        

if __name__ == "__main__":
    master = Tk()
    obj = Face_Recognition_System(master)
    master.mainloop()
