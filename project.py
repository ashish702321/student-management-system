import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win = tk.Tk()
win.geometry("1350x750")
win.title("Student Management System")

title_label = tk.Label(win, text="Student Management System", font=("Arial", 25), border=12, relief=tk.GROOVE)
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20), bd=12, relief=tk.GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=420, height=575)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)

Name = tk.StringVar()
Course = tk.StringVar()
rollno = tk.StringVar()
section = tk.StringVar()
fathername = tk.StringVar()
contact = tk.StringVar()
address = tk.StringVar()
dob = tk.StringVar()
gender = tk.StringVar()

search_by = tk.StringVar()
search_text = tk.StringVar()

Name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 15), bg="lightgrey")
Name_lbl.grid(row=1, column=0, padx=2, pady=2)

Name_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=Name)
Name_ent.grid(row=1, column=1, padx=2, pady=2)

Course_lbl = tk.Label(detail_frame, text="Course", font=("Arial", 15), bg="lightgrey")
Course_lbl.grid(row=2, column=0, padx=2, pady=2)

Course_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=Course)
Course_ent.grid(row=2, column=1, padx=2, pady=2)

rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("Arial", 15), bg="lightgrey")
rollno_lbl.grid(row=3, column=0, padx=2, pady=2)

rollno_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=rollno)
rollno_ent.grid(row=3, column=1, padx=2, pady=2)

section_lbl = tk.Label(detail_frame, text="Section", font=("Arial", 15), bg="lightgrey")
section_lbl.grid(row=4, column=0, padx=2, pady=2)

section_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=section)
section_ent.grid(row=4, column=1, padx=2, pady=2)

fathername_lbl = tk.Label(detail_frame, text="Father's Name", font=("Arial", 15), bg="lightgrey")
fathername_lbl.grid(row=5, column=0, padx=2, pady=2)

fathername_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=fathername)
fathername_ent.grid(row=5, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact", font=("Arial", 15), bg="lightgrey")
contact_lbl.grid(row=6, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=contact)
contact_ent.grid(row=6, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 15), bg="lightgrey")
address_lbl.grid(row=7, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=address)
address_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = tk.Label(detail_frame, text="D.O.B", font=("Arial", 15), bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15), textvariable=dob)
dob_ent.grid(row=8, column=1, padx=2, pady=2)

gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 15), bg="lightgrey")
gender_lbl.grid(row=9, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, font=("arial", 15), state="readonly", textvariable=gender)
gender_ent['values'] = ("Male", "Female", "Others")
gender_ent.grid(row=9, column=1, padx=2, pady=2)

def fetch_data():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
            conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error due to: {str(e)}")

def add_func():
    if rollno.get() == "" or Name.get() == "" or Course.get() == "":
        messagebox.showerror("Error!", "All fields are required")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("INSERT INTO data VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                         (Name.get(), Course.get(), rollno.get(), section.get(), fathername.get(), contact.get(), address.get(), dob.get(), gender.get()))
            conn.commit()
            conn.close()
            fetch_data()
            clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

def get_cursor(event):
    '''This function will fetch data of the selected row'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    Name.set(row[0])
    Course.set(row[1])
    rollno.set(row[2])
    section.set(row[3])
    fathername.set(row[4])
    contact.set(row[5])
    address.set(row[6])
    dob.set(row[7])
    gender.set(row[8])

def clear():
    '''This is function will clear the entry boxes'''
    Name.set("")
    Course.set("")
    rollno.set("")
    section.set("")
    fathername.set("")
    contact.set("")
    address.set("")
    dob.set("")
    gender.set("")

def update_func():
    '''This function will update data according to user'''
    if rollno.get() == "" or Name.get() == "" or Course.get() == "":
        messagebox.showerror("Error!", "All fields are required")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("UPDATE data SET Name=%s, Course=%s, section=%s, fathername=%s, contact=%s, address=%s, dob=%s, gender=%s WHERE rollno=%s", 
                         (Name.get(), Course.get(), section.get(), fathername.get(), contact.get(), address.get(), dob.get(), gender.get(), rollno.get()))
            conn.commit()
            conn.close()
            fetch_data()
            clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

def delete_func():
    '''This function will delete data according to user'''
    if rollno.get() == "":
        messagebox.showerror("Error!", "Roll No is required")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("DELETE FROM data WHERE rollno=%s", rollno.get())
            conn.commit()
            conn.close()
            fetch_data()
            clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

def search_func():
    '''This function will search data according to user input'''
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        query = f"SELECT * FROM data WHERE {search_by.get()} LIKE '%{search_text.get()}%'"
        curr.execute(query)
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
            conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error due to: {str(e)}")

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=18, y=390, width=340, height=120)

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("arial", 13), width=15, command=add_func)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("arial", 13), width=15, command=update_func)
update_btn.grid(row=0, column=1, padx=3, pady=2)

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("arial", 13), width=15, command=delete_func)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("arial", 13), width=15, command=clear)
clear_btn.grid(row=1, column=1, padx=3, pady=2)

search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("arial", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly", textvariable=search_by)
search_in["values"] = ("Name", "Roll No", "Contact", "Father's Name", "Course", "Section", "D.O.B")
search_in.grid(row=0, column=1, padx=12, pady=2)

search_txt = tk.Entry(search_frame, bd=7, font=("arial", 14), textvariable=search_text)
search_txt.grid(row=0, column=2, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("arial", 13), bd=9, width=14, bg="lightgrey", command=search_func)
search_btn.grid(row=0, column=3, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=fetch_data)
showall_btn.grid(row=0, column=4, padx=12, pady=2)

main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=("Name", "Course", "Roll No", "Section", "Father's name", "Contact", "Address", "Gender", "D.O.B"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("Name", text="Name")
student_table.heading("Course", text="Course")
student_table.heading("Roll No", text="Roll No")
student_table.heading("Section", text="Section")
student_table.heading("Father's name", text="Father's name")
student_table.heading("Contact", text="Contact")
student_table.heading("Address", text="Address")
student_table.heading("Gender", text="Gender")
student_table.heading("D.O.B", text="D.O.B")

student_table['show'] = 'headings'

student_table.column("Name", width=100)
student_table.column("Course", width=100)
student_table.column("Roll No", width=100)
student_table.column("Section", width=100)
student_table.column("Father's name", width=100)
student_table.column("Contact", width=100)
student_table.column("Address", width=100)
student_table.column("Gender", width=100)
student_table.column("D.O.B", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>", get_cursor)

win.mainloop()
