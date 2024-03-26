import tkinter as tk
import numpy as np
from tkinter import *
from tkinter import TclError, ttk
from tkinter.messagebox import showinfo, askyesno, askquestion
course_id = ['01355101','01355102','01417111','01418111','01418112','01418141','01999021','01999111','02999144']
course_details = {'01355101': ('English for Everyday Life',3),
                  '01355102': ('English for University Life',3),
                  '01417111': ('Calculus I',3),
                  '01418111': ('Introduction to Computer Science',3),
                  '01418112': ('Fundamental Programming Concepts',3),
                  '01418141': ('Intellectual Properties and Professional Ethics',3),
                  '01999021': ('Thai Language for Communication',3),
                  '01999111': ('Knowledge of the Land',2),
                  '02999144': ('Life Skill for Undergraduate Student',1)}
grades = (('A', 4.0), ('B+', 3.5), ('B', 3.0), ('C+', 2.5), ('C', 2.0), 
          ('D+', 1.5), ('D', 1.0), ('F', 0.0), ('P', -1),('NP',-2), ('W',-3))
added_course = []
added_credit = []
added_grade = []


def id_changed(event): 
    """ เมื่อเลือกเปลี่ยนรหัสวิชา """
    id = selected_id.get()
    selected_name = course_details[id][0]     # เก็บชื่อวิชาใน selected_name
    txt_name.delete(0,END)
    txt_name.insert(0,selected_name)

    selected_credit = course_details[id][1]   # เก็บหน่วยกิตใน selected_credit
    txt_credit.delete(0,END)
    txt_credit.insert(0,selected_credit)



def create_input_frame(container):
    
    frame = ttk.Frame(container)
    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=3)

    # สร้าง combo box เพื่อแสดงรายการรหัสวิชาให้เลือก
    ttk.Label(frame, text='รหัสวิชา:').grid(column=0, row=0, sticky=tk.W)
    cbo_id = ttk.Combobox(frame, width=20, textvariable=selected_id)

    cbo_id['values'] = course_id
    cbo_id['state'] = 'readonly'    # prevent typing a value
    cbo_id.focus()
    cbo_id.grid(column=1, row=0, sticky=tk.W)
    
    # bind the selected value change
    # ถ้ามีการเลือก Combpbox ให้เรียก Function  id_changed
    cbo_id.bind('<<ComboboxSelected>>', id_changed)  

    # สร้าง text box เพื่อแสดงชื่อวิชา
    ttk.Label(frame, text='ชื่อวิชา:').grid(column=0, row=1, sticky=tk.W)
    txt_name = ttk.Entry(frame, width=40, textvariable=selected_name)
    txt_name.grid(column=1, row=1, sticky=tk.W)

    # สร้าง text box เพื่อแสดงหน่วยกิต
    ttk.Label(frame, text='หน่วยกิต:').grid(column=0, row=2, sticky=tk.W)
    txt_credit = ttk.Entry(frame, width=25, textvariable=selected_credit)
    txt_credit.grid(column=1, row=2, sticky=tk.W)


    # สร้าง label และ frame2 แสดงรายการผลการเรียนของรายวิชา
    label = ttk.Label(frame, text="เลือกผลการเรียน")
    label.grid(column=0, row=3, sticky=tk.W)

    frame2 = ttk.Frame(frame)
    frame2.columnconfigure(0, weight=1)
    frame2.columnconfigure(1, weight=1)
    frame2.columnconfigure(2, weight=1)
    frame2.columnconfigure(3, weight=1)
    frame2.columnconfigure(4, weight=1)

    # สร้างรายการตัวเลือกผลการเรียน (radio buttons) แบบ 5 คอลัมน์ต่อแถว
    lr = 0
    lc = i = 0
    for grade in grades:
        r = ttk.Radiobutton(frame2, text=grade[0], value=grade[1], variable=selected_grade)
        r.grid(column=lc, row=lr, padx=5, pady=5, sticky=tk.W)
        i += 1
        lc = i % 5
        # เพิ่มแถวแสดงรายการผลการเรียน เมื่อครบ 5 รายการ
        if lc == 0: lr +=1        
    frame2.grid(column=1, row=3,columnspan=2)
    return frame, cbo_id, txt_name, txt_credit

def updateGPA():
    # รวมจำนวนหน่วยกิต และ GPA
    sum_credits = np.sum(added_credit)
    sum_grades = np.sum(np.multiply(added_credit , added_grade))
    GPA = sum_grades / sum_credits
    lbl_Credits.config(text=f'จำนวนหน่วยกิต: \n {sum_credits}')
    lbl_GPA.config(text=f'ผลกาารเรียน: \n {GPA:.2f}')
    return GPA

def click (action, root, table):
    # รวมการทำงานเมื่อผู้ใช้งานคลิกปุ่ม add, delete และ close
    # กรณีที่คลิกปุ่ม add
    if action == 'add':                     
        course_id = selected_id.get()
        course_name = selected_name.get()
        credit = selected_credit.get()
        grade = selected_grade.get()
        # ถ้าไม่เลือกรหัสวิชา แจ้งข้อความผิดพลาด
        if course_id == "":                     
            showinfo(title='Error', message='กรุณาเลือกรายวิชาที่ต้องการเพิ่มในตาราง')
            return 
        # ถ้าไม่เลือกผลการเรียน แจ้งข้อความผิดพลาด
        elif grade == "":                      
            showinfo(title='Error', message='กรุณาเลือกผลการเรียนของรายวิชา')
            return
        # ถ้าเลือกรหัสวิชาไม่ซ้ำ สร้างรายการใหม่ในตาราง และเพิ่มรายการวิชา หน่วยกิต และผลการเรียน
        elif not course_id  in added_course:    
            content = [course_id , course_name , credit , grade]
            table.insert('' , tk.END , values=content)
            added_course.append(course_id)
            if float(grade) >= 0.0 :
                added_credit.append(int(credit))
                added_grade.append(float(grade))
            else:
                added_credit.append(int(0))
                added_grade.append(float(0))
            updateGPA()

        # ถ้าเลือกรหัสวิชาซ้ำ แจ้งข้อความผิดพลาด
        else:                                   
            showinfo(title='Error', message='รหัสวิชาที่ต้องการเพิ่มใหม่ซ้ำกับรหัสวิชาที่อยู่ในตารางแล้ว')
    
    # กรณีที่คลิกปุ่ม delete
    elif action == 'delete':                    
        for selected_item in table.selection():
            item = table.item(selected_item)
            record = item['values']
            id =f'0{record[0]}'
            idx = added_course.index(id)
            if idx >= 0:
                answer = askyesno(title='ยืนยันการลบ',
                          message='คุณต้องการลบรายการนี้หรือไม่?')
                if answer:
                    added_course.pop(idx)
                    added_credit.pop(idx)
                    added_grade.pop(idx)
                    table.delete(selected_item)
                    updateGPA()
    
    # กรณีที่คลิกปุ่ม close
    else:                                           
        root.destroy()
        print('Program is closed')

def create_button_frame(container, table):
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    # สร้างปุ่มการทำงาน add, delete และ close 
    # และผูกการทำงานในฟังก์ชัน click 
    btn_add = ttk.Button(frame, text='Add',command=lambda: click('add', container, table)).grid(column=0, row=0)
    btn_delete =ttk.Button(frame, text='Delete',command=lambda: click('delete',container, table)).grid(column=0, row=1)
    btn_close = ttk.Button(frame, text='Close',command=lambda: click('close', container, table)).grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_grade_table(container):
    # กำหนดคอลัมน์ของตาราง
    columns = ('course_id', 'course_name', 'credit', 'grade')
    tree = ttk.Treeview(container, columns=columns, show='headings')

    # สร้างหัวข้อคอลัมน์ของตาราง
    tree.heading('course_id', text='รหัสวิชา')
    tree.heading('course_name', text='ชื่อวิชา')
    tree.heading('credit', text='หน่วยกิต')
    tree.heading('grade', text='ผลการเรียน')

    # กำหนดความกว้างของคอลัมน์
    tree.column("course_id", minwidth=0, width=55, stretch=NO)
    tree.column("course_name", minwidth=0, width=155, stretch=NO)
    tree.column("credit", minwidth=0, width=50, stretch=NO)
    tree.column("grade", minwidth=0, width=55, stretch=NO)
    return tree

###################
# MAIN 

root = tk.Tk()
root.title('Grade Calculator')
root.resizable(0, 0)

# สร้าง StringVar สำหรับเก็บค่าการเลือกข้อมูลรายวิชาในปัจจุบัน
selected_id = tk.StringVar()
selected_name = tk.StringVar()
selected_credit = tk.StringVar()
selected_grade = tk.StringVar()

try:
 # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

# layout on the root window
root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)
root.rowconfigure(1,weight=4)
# สร้าง input_frame และ widget สำหรับนำเข้าข้อมูล
input_frame,cbo_id, txt_name, txt_credit = create_input_frame(root)   
input_frame.grid(column=0, row=0)
# สร้าง grade_table เป็นตารางแสดงรายการวิชา และผลการเรียน
grade_table = create_grade_table(root)                                
grade_table.grid(column=0, row=1, padx=5, pady=5, sticky='nsew')
# สร้าง scrollbar สำหรับตาราง grade_table
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=grade_table.yview)
grade_table.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='nwsw')

# สร้าง button_frame และ button เพื่อการทำงานต่าง ๆ
button_frame = create_button_frame(root, grade_table)                 

# สร้าง lbl_credits แสดงจำนวนหน่วยกิตทั้งหมด
lbl_Credits = tk.Label(button_frame, text="จำนวนหน่วยกิต", bg='green', fg='white')
lbl_Credits.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)

# สร้าง lbl_GPA แสดงผลการเรียน
lbl_GPA = tk.Label(button_frame, text="ผลการเรียน", bg='blue', fg='white')
lbl_GPA.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

button_frame.grid(column=1, row=0)

root.mainloop()