from tkinter import*
from tkinter import ttk
from turtle import width
from tkcalendar import Calendar, DateEntry
# for image
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
import mysql.connector


class Student_Details:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition Attendance System")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="#151D3B")

# variables
        self.var_course = StringVar()
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_faculty = StringVar()
        self.var_cal = StringVar()
        self.var_gender = StringVar()

        title_lbl = Label(self.master, text="Student Details", font=(
            "verdana", 40, "bold"), fg="white", bg="#151D3B")
        title_lbl.pack(side=TOP, fill=X)
# main Frame

        Main_frame = Frame(self.master, bd=2, relief=RIDGE, bg="#2FA4FF")
        Main_frame.place(x=1, y=80, width=1360, height=610)
# left label frame
        Left_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg="#2FA4FF")
        Left_frame.place(x=1, y=0, width=850, height=590)

        Course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Branch", font=(
            "Roboto Mono", 15, "bold"), fg="#F24A72", bg="white")
        Course_frame.place(x=3, y=2, width=840, height=130)

 # Course
        Course_Label = Label(Course_frame, text="Course ",
                             font=("Roboto Mono", 14, "bold"), fg="black", bg="white")
        Course_Label.grid(row=0, column=0, sticky=W, padx=10)

        Course_entry = ttk.Entry(
            Course_frame, textvariable=self.var_course, width=20, font=("Roboto Mono", 15))
        Course_entry.grid(row=0, column=1, sticky=W, padx=2, pady=10)

# Branch
        dep_Label = Label(Course_frame, text="Department ",
                          font=("Roboto Mono", 14, "bold"), fg="black", bg="white")
        dep_Label.grid(row=0, column=2, sticky=W, padx=10)

        dep_entry = ttk.Entry(
            Course_frame, textvariable=self.var_dep, width=20, font=("Roboto Mono", 15))
        dep_entry.grid(row=0, column=3, sticky=W, padx=2, pady=10)

# year
        year_Label = Label(Course_frame, text="Year ", font=(
            "Roboto Mono", 14, "bold"), fg="black", bg="white")
        year_Label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(Course_frame, textvariable=self.var_year, width=25, font=(
            "Roboto Mono", 12), state="readonly")
        year_combo['values'] = ("Select year", "1st Year",
                                "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

# semester
        sem_Label = Label(Course_frame, text="Semester ", font=(
            "Roboto Mono", 14, "bold"), fg="black", bg="white")
        sem_Label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(Course_frame, textvariable=self.var_sem, width=25, font=(
            "Roboto Mono", 12), state="readonly")
        sem_combo['values'] = ("Select Semester", "Semester 1", "Semester 2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10)

# Student Info
        Student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Student Info", font=(
            "Roboto Mono", 15, "bold"), fg="#F24A72", bg="white")
        Student_frame.place(x=5, y=150, width=840, height=430)

 # id
        StudentId_Label = Label(Student_frame, text="Student ID ", font=(
            "Roboto Mono", 14, "bold"), fg="black", bg="white", pady=20)
        StudentId_Label.grid(row=0, column=0, sticky=W, padx=10)

        StudentID_entry = ttk.Entry(
            Student_frame, textvariable=self.var_id, font=("Roboto Mono", 15), width=20)
        StudentID_entry.grid(row=0, column=1, sticky=W)

# Name
        StudentName_Label = Label(Student_frame, text="Student Name ",
                                  font=("Roboto Mono", 14, "bold"), fg="black", bg="white")
        StudentName_Label.grid(row=0, column=2, sticky=W, padx=10)

        StudentName_entry = ttk.Entry(
            Student_frame, textvariable=self.var_name, width=20, font=("Roboto Mono", 15))
        StudentName_entry.grid(row=0, column=3, sticky=W)

# Roll No. -
        StudentRoll_Label = Label(Student_frame, text="Roll No. ", font=(
            "Roboto Mono", 14, "bold"), fg="black", bg="white", pady=20)
        StudentRoll_Label.grid(row=1, column=0, sticky=W, padx=10)

        StudentRoll_entry = ttk.Entry(
            Student_frame, textvariable=self.var_roll, width=20, font=("Roboto Mono", 15))
        StudentRoll_entry.grid(row=1, column=1, sticky=W)

# Email
        StudentEmail_Label = Label(Student_frame, text="Email ",
                                   font=("Roboto Mono", 14, "bold"), fg="black", bg="white")
        StudentEmail_Label.grid(row=1, column=2, sticky=W, padx=10)

        StudentEmail_entry = ttk.Entry(
            Student_frame, textvariable=self.var_email, width=20, font=("Roboto Mono", 15))
        StudentEmail_entry.grid(row=1, column=3, sticky=W)

# Gender
        Student_gender_Label = Label(Student_frame, text="Gender ", font=(
            "Roboto Mono", 15, "bold"), fg="black", bg="white", pady=20)
        Student_gender_Label.grid(row=2, column=0, sticky=W, padx=10)

        Student_gender_entry = ttk.Entry(
            Student_frame, textvariable=self.var_gender, width=20, font=("Roboto Mono", 15))
        Student_gender_entry.grid(row=2, column=1, sticky=W)

 # Date of Birth
        StudentDOB_Label = Label(Student_frame, text="Date of Birth-", font=(
            "Roboto Mono", 15, "bold"), fg="black", bg="white", pady=20)
        StudentDOB_Label.grid(row=2, column=2, sticky=W, padx=10)

        cal = DateEntry(Student_frame, textvariable=self.var_cal,
                        width=35, background="magenta3", foreground="white", bd=2)
        cal.grid(row=2, column=3, sticky=W)

# Phone No.
        StudentPhone_Label = Label(Student_frame, text="Contact ", font=(
            "Roboto Mono", 14, "bold"), fg="black", bg="white", pady=20)
        StudentPhone_Label.grid(row=3, column=0, sticky=W, padx=10)

        StudentPhone_entry = ttk.Entry(
            Student_frame, textvariable=self.var_phone, width=20, font=("Roboto Mono", 15, "bold"))
        StudentPhone_entry.grid(row=3, column=1, sticky=W)


# Faculty Name
        # StudentFaculty_Label = Label(Student_frame, text="Faculty Name ", font=(
        #     "Roboto Mono", 14, "bold"), fg="black", bg="white", pady=20, padx=10)
        # StudentFaculty_Label.grid(row=3, column=2, sticky=W, padx=10)

        # StudentFaculty_entry = ttk.Entry(
        #     Student_frame, textvariable=self.var_faculty, width=20, font=("Roboto Mono", 15))
        # StudentFaculty_entry.grid(row=3, column=3, sticky=W)

# Address
        StudentAddress_Label = Label(Student_frame, text="Address ", font=(
            "Roboto Mono", 14, "bold"), fg="black", bg="white", pady=20)
        StudentAddress_Label.grid(row=4, column=0, padx=10, sticky=W)

        StudentAddress_entry = ttk.Entry(
            Student_frame, textvariable=self.var_address, width=20, font=("Roboto Mono", 15))
        StudentAddress_entry.grid(row=4, column=1, sticky=W)

# radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            Student_frame, text="Photo Sample", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=4, column=2, sticky=W, padx=50)

        # self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            Student_frame, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=4, column=3, sticky=W, padx=50)

# buttons frame
        Button_frame = Frame(Student_frame, bd=2, relief=RIDGE)
        Button_frame.place(x=3, y=320, width=830, height=40)

# save
        save_btn = Button(Button_frame, text="Save", command=self.add_data, width=20, font=(
            "Roboto Mono", 12, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        save_btn.grid(row=0, column=0)

# update
        update_btn = Button(Button_frame, command=self.update_data, text="Update", width=20, font=(
            "Roboto Mono", 12, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        update_btn.grid(row=0, column=1)

# delete button
        delete_btn = Button(Button_frame, command=self.delete_data, text="Delete", width=20, font=(
            "Roboto Mono", 12, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        delete_btn.grid(row=0, column=2)

# reset button
        reset_btn = Button(Button_frame, command=self.reset_data, text="Reset", width=20, font=(
            "Roboto Mono", 12, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        reset_btn.grid(row=0, column=3)

        Button_frame1 = Frame(Student_frame, bd=2, relief=RIDGE)
        Button_frame1.place(x=3, y=360, width=830, height=40)

# take Photo
        take_photo_btn = Button(Button_frame1, command=self.generate_dataset, text="Take photo", width=40, font=(
            "Roboto Mono", 12, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        take_photo_btn.grid(row=1, column=0)

# Update Photo
        update_photo_btn = Button(Button_frame1, text="Update Photo", width=41, font=(
            "Roboto Mono", 12, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        update_photo_btn.grid(row=1, column=1)

# Right label frame
        Right_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg="#2FA4FF", font=(
            "Roboto Mono", 15, "bold"), text="Student Details", fg="#F24A72")
        Right_frame.place(x=840, y=0, width=600, height=590)

       # Searching
        Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE)
        Search_frame.place(x=3, y=10, width=500, height=50)

        Search_Label = Label(Search_frame, text="Search by Roll",
                             font=("Roboto Mono", 12, "bold"), fg="black", bg="#FF0075")
        Search_Label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        # Search_combo = ttk.Combobox(Search_frame, width=15, font=("Roboto Mono", 10), state="readonly")
        # Search_combo['values'] = ("Select", "Roll No.", "Phone No.", "Name")
        # Search_combo.current(0)
        # Search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)
        self.var_search = StringVar()
        Search_entry = ttk.Entry(
            Search_frame, textvariable=self.var_search, width=12, font=("Roboto Mono", 15))
        Search_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

# Search btn
        Search_btn = Button(Search_frame, text="Search",command=self.search_data, width=13, font=(
            "Roboto Mono", 10, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        Search_btn.grid(row=0, column=2, padx=2, pady=10, sticky=W)

# Show all btn
        Show_all_btn = Button(Search_frame, text="Show All", width=12, font=(
            "Roboto Mono", 10, "bold"), cursor="hand2", activebackground="#1EAE98", bg="#77D970", fg="white")
        Show_all_btn.grid(row=0, column=3, padx=2, pady=10, sticky=W)

# Table Frame
        Table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        Table_frame.place(x=3, y=70, width=500, height=490)

# Scrolling
        Scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.Details_table = ttk.Treeview(Table_frame, column=(
            "Course",
            "Department",
            "Year",
            "Semester",
            "Id",
            "Name",
            "Roll",
            "Email",
            "Phone",
            "Address",
            "Faculty",
            "Photo",
            "DOB",
            "Gender",
        ), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.Details_table.xview)
        Scroll_y.config(command=self.Details_table.yview)

        self.Details_table.heading("Course", text="Course")
        self.Details_table.heading("Department", text="Department")
        self.Details_table.heading("Year", text="Year")
        self.Details_table.heading("Semester", text="Semester")
        self.Details_table.heading("Id", text="StudentId")
        self.Details_table.heading("Name", text="StudentName")
        self.Details_table.heading("Roll", text="Roll No.")
        self.Details_table.heading("Email", text="Email")
        self.Details_table.heading("Phone", text="Phone")
        self.Details_table.heading("Address", text="Address")
        self.Details_table.heading("Faculty", text="Faculty")
        self.Details_table.heading("Photo", text="Photo")
        self.Details_table.heading("DOB", text="Date of Birth")
        self.Details_table.heading("Gender", text="Gender")
        self.Details_table['show'] = 'headings'

        self.Details_table.column("Course", width=100)
        self.Details_table.column("Department", width=100)
        self.Details_table.column("Year", width=100)
        self.Details_table.column("Semester", width=100)
        self.Details_table.column("Id", width=100)
        self.Details_table.column("Name", width=100)
        self.Details_table.column("Roll", width=100)
        self.Details_table.column("Email", width=100)
        self.Details_table.column("Phone", width=100)
        self.Details_table.column("Address", width=150)
        self.Details_table.column("Faculty", width=100)
        self.Details_table.column("Photo", width=150)
        self.Details_table.column("DOB", width=100)
        self.Details_table.column("Gender", width=100)

        self.Details_table.pack(fill=BOTH, expand=1)
        self.Details_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
# Function Declaration

    def add_data(self):
        if self.var_dep.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_roll.get() == "" or self.var_course.get() == "" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester":
        # if self.var_dep.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.master)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Kumari#1207", database="face", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_course.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_faculty.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_cal.get(),
                                                                                                            self.var_gender.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                print('Connected')
                messagebox.showinfo(
                    "Success", "Data Added Sucessfully", parent=self.master)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to : {str(es)}", parent=self.master)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Kumari#1207", database="face", auth_plugin='mysql_native_password')
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.Details_table.delete(*self.Details_table.get_children())
            for i in data:
                self.Details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

# get cursor function

    def get_cursor(self, event=""):
        cursor_focus = self.Details_table.focus()
        contents = self.Details_table.item(cursor_focus)
        data = contents['values']
        self.var_course.set(data[0])
        self.var_dep.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_email.set(data[7])
        self.var_phone.set(data[8])
        self.var_address.set(data[9])
        self.var_faculty.set(data[10])
        self.var_radio1.set(data[11])
        self.var_cal.set(data[12])
        self.var_gender.set(data[13])

# Update Function
    def update_data(self):
        if self.var_dep.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_roll.get() == "" or self.var_course.get() == "" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester":
        # if self.var_dep.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.master)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to Update this Student Details!", parent=self.master)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="Kumari#1207", database="face", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor(buffered=True)
                    my_cursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Gender=%s,DOB=%s,Phone=%s,Address=%s,Roll=%s,Email=%s,Faculty=%s,PhotoSample=%s where StudentID=%s", (
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_gender.get(),
                        self.var_cal.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_roll.get(),
                        self.var_email.get(),
                        self.var_faculty.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Successfully Updated!", parent=self.master)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.master)

    # ==============================Delete Function=========================================
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student Id Must be Required!", parent=self.master)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete", "Do you want to Delete?", parent=self.master)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="Kumari#1207", database="face", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor(buffered=True)
                    sql = "delete from student where StudentID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully Deleted!", parent=self.master)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.master)

    # Reset Function
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_gender.set(""),
        self.var_cal.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_faculty.set(""),
        self.var_radio1.set("")

# Generate data Set or Take Photo Sample
    def generate_dataset(self):
        if self.var_dep.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_roll.get() == "" or self.var_course.get() == "" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester":
        # if self.var_dep.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.master)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Kumari#1207", database="face", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("select * from student")
                result = my_cursor.fetchall()
                id = 0
                for x in result:
                    id += 1
                my_cursor.execute("update student set Course=%s,Department=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Email=%s,Phone=%s,Address=%s,Faculty=%s,PhotoSample=%s,DOB=%s,Gender=%s where StudentID=%s", (self.var_course.get(),
                                                                                                                                                                                                                  self.var_dep.get(),
                                                                                                                                                                                                                  self.var_year.get(),
                                                                                                                                                                                                                  self.var_sem.get(),
                                                                                                                                                                                                                  self.var_name.get(),
                                                                                                                                                                                                                  self.var_roll.get(),
                                                                                                                                                                                                                  self.var_email.get(),
                                                                                                                                                                                                                  self.var_phone.get(),
                                                                                                                                                                                                                  self.var_address.get(),
                                                                                                                                                                                                                  self.var_faculty.get(),
                                                                                                                                                                                                                  self.var_radio1.get(),
                                                                                                                                                                                                                  self.var_cal.get(),
                                                                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                                                                  self.var_id.get() == id+1,
                                                                                                                                                                                                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # scaling factor=1.3
                    # Minimum Neighbour=5
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # rectangle
                    for (x, y, w, h) in faces:
                        face_croped = img[x:x+w, y:y+h]
                        return face_croped
                    # to open web camera
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id = img_id+1
                        # passport size to crop image
                        face = cv2.resize(face_croped(my_frame), (400, 400))
                        # images from colored to gray
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path ="data/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50),cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)


                    if cv2.waitKey(1) == 13 or int(img_id) == 150:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset is generated....", parent=self.master)
            except Exception as es:
                messagebox.showerror( "Error", f"Error due to : {str(es)}", parent=self.master)

    #Search data
    def search_data(self):
        if self.var_search.get()=="":
            messagebox.showerror("Error","enter entry box",parent=self.master)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='Kumari#1207',host='localhost',database='face')
                my_cursor = conn.cursor()
                sql = "SELECT StudentID,Name,Department,Course,Year,Semester,Gender,DOB,Phone,Address,Roll,Email,Faculty,PhotoSample FROM student where Roll='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.Details_table.delete(*self.Details_table.get_children())
                    for i in rows:
                        self.Details_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.master)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.master)            


if __name__ == "__main__":
    master = Tk()
    obj = Student_Details(master)
    master.mainloop()
