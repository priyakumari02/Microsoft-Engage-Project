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


class Face_Recognition:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition Attendance System")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="#151D3B")

        title_lbl = Label(self.master, text="Face Recognition", font=("Roboto Mono", 40, "bold"), fg="white", bg="#151D3B")
        title_lbl.pack(side=TOP, fill=X)

        bg1=Image.open(r"Videos\face-recognition.gif")
        bg1=bg1.resize((600,500))
        self.photobg1=ImageTk.PhotoImage(bg1)
        bg_img = Label(self.master,image=self.photobg1)
        bg_img.place(x=100,y=200,width=500,height=400)

        b=Button(
            self.master,
            text='RECOGNIZE',
            command=self.face_recognition,
            font=('Roboto Mono', 30, 'bold'),
            padx=10,
            pady=10,
            cursor="hand2",
            bg='#F32424',
            fg='#F2F2F2',
            activebackground='#2FA4FF',
            activeforeground='white'
        ).place(x=800, y=350)
       
        lbl = Label(self.master,text="Press Enter to close Face Detector", font=("verdana", 20, "bold"), fg="white", bg="#151D3B")
        lbl.place(x=700,y=500)
#=====================Attendance===================

    def mark_attendance(self,d,b,c,a):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((d not in name_list)) and ((b not in name_list)) and ((c not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{d}, {b}, {c}, {a} ,{dtString}, {d1}, Present")

#face recognition function
    def face_recognition(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coordinates=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y + h, x:x + w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Kumari#1207", database="face", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor(buffered=True)

                my_cursor.execute("select Department from student where StudentID="+str(id))
                a=my_cursor.fetchone()
                a=" + ".join(a)

                my_cursor.execute("select Name from student where StudentID="+str(id))
                b=my_cursor.fetchone()
                b=" + ".join(b)

                my_cursor.execute("select Roll from student where StudentID="+str(id))
                c=my_cursor.fetchone()
                c=" + ".join(c)

                my_cursor.execute("select StudentID from student where StudentID="+str(id))
                d=my_cursor.fetchone()
                d=" + ".join(d)
                
                if confidence > 77:
                    cv2.putText(img,f"ID:{d}",(x,y-110),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,0,0),2)
                    cv2.putText(img,f"Name:{b}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,0,255),2)
                    cv2.putText(img,f"Roll:{c}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,0,0),2)
                    cv2.putText(img,f"Department:{a}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    self.mark_attendance(d,b,c,a)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coordinates=[x,y,w,h]
            
            return coordinates 
            
                  
        def recognize(img,clf,faceCascade):
            coordinates=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    master = Tk()
    obj = Face_Recognition(master)
    master.mainloop()       