from tkinter import*
from tkinter import ttk
from tkinter.filedialog import SaveAs
from turtle import width
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
# for image
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition Attendance System")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="#151D3B")

        title_lbl = Label(self.master, text="Train Dataset", font=("Roboto Mono", 40, "bold"), fg="white", bg="#151D3B")
        title_lbl.pack(side=TOP, fill=X)

        b=Button(
            self.master,
            text='TRAIN DATA',
            font=('Roboto Mono', 40, 'bold'),
            command=self.train_classifier,
            padx=10,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=500, y=300)
    

    def train_classifier(self):
        #data sample stored in data_dir
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            #Gray Scale Image
            img=Image.open(image).convert('L')
            #data type = unit8
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)   

        # Train the classifier and Save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids) 
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed",parent=self.master)

if __name__ == "__main__":
    master = Tk()
    obj = Train(master)
    master.mainloop()       