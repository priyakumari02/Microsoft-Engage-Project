# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import csv
from tkinter import filedialog
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,master):
        self.master=master
        self.master.geometry("1366x768+0+0")
        self.master.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
        self.var_faculty=StringVar()

        #title section
        title_lbl = Label(self.master,text="Welcome to Attendance Pannel",font=("verdana",40,"bold"),fg="white", bg="#151D3B")
        title_lbl.pack(side=TOP, fill=X)

        #-----------Frames-------------------

        # Creating Frame 
        main_frame = Frame(self.master,bd=2,bg="#151D3B") #bd mean border 
        main_frame.place(x=0,y=70,width=1370,height=700)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="#151D3B",relief=RIDGE,text="Student Details",font=("verdana",15,"bold"),fg="#F24A72")
        left_frame.place(x=10,y=50,width=660,height=600)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(left_frame,text="Student ID",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        studentId_label.grid(row=0,column=0,padx=5,pady=20,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=30,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=20,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Student Name",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        student_name_label.grid(row=2,column=0,padx=5,pady=20,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=30,font=("verdana",12,"bold"))
        student_name_entry.grid(row=2,column=1,padx=5,pady=20,sticky=W)

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll No.",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        student_roll_label.grid(row=1,column=0,padx=10,pady=25,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=30,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=1,padx=5,pady=20,sticky=W)

        # Department
        dep_label = Label(left_frame,text="Department",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        dep_label.grid(row=3,column=0,padx=5,pady=20,sticky=W)

        dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=30,font=("verdana",12,"bold"))
        dep_entry.grid(row=3,column=1,padx=5,pady=25,sticky=W)

        #time
        time_label = Label(left_frame,text="Time",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        time_label.grid(row=4,column=0,padx=5,pady=20,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=30,font=("verdana",12,"bold"))
        time_entry.grid(row=4,column=1,padx=5,pady=20,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        date_label.grid(row=5,column=0,padx=5,pady=20,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=30,font=("verdana",12,"bold"))
        date_entry.grid(row=5,column=1,padx=5,pady=20,sticky=W)

        #Faculty 
        fact_label = Label(left_frame,text="Faculty",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        fact_label.grid(row=5,column=0,padx=5,pady=20,sticky=W)

        fact_entry = ttk.Entry(left_frame,textvariable=self.var_faculty,width=30,font=("verdana",12,"bold"))
        fact_entry.grid(row=5,column=1,padx=5,pady=20,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status",font=("verdana",12,"bold"),fg="white",bg="#151D3B")
        student_attend_label.grid(row=6,column=0,padx=5,pady=20,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=30,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=6,column=1,padx=1,pady=20,sticky=W)

       
        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="#151D3B",relief=RIDGE)
        btn_frame.place(x=10,y=500,width=635,height=60)

        #Improt button
        import_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=17,font=("verdana",12,"bold"),cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="blue")
        import_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #Exprot button
        export_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=17,font=("verdana",12,"bold"),cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="blue")
        export_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=17,font=("verdana",12,"bold"),cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="blue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="#151D3B",relief=RIDGE,text="Student Details",font=("verdana",15,"bold"),fg="#F24A72")
        right_frame.place(x=680,y=50,width=660,height=600)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="#151D3B",relief=RIDGE)
        table_frame.place(x=10,y=10,width=635,height=550)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","RollNo","Name","Time","Date","Faculty","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Student ID")
        self.attendanceReport.heading("Name",text="Stdudent Name")
        self.attendanceReport.heading("RollNo",text="Roll No.")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Faculty",text="Faculty")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("RollNo",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Faculty",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)
    
      

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_faculty.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data  ===============

    def fetchData(self,rows):
        # global mydata
        # mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)
        
     # =========================Import Data  ===============
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.master)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #==================Export CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.master)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.master)

            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully! "+os.path.basename(fln),parent=self.master)
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.master)    

    #=============Cursur Function for CSV========================

    def get_cursor(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_faculty.set(data[5]),
        self.var_attend.set(data[6])  



if __name__ == "__main__":
    master=Tk()
    obj=Attendance(master)
    master.mainloop()