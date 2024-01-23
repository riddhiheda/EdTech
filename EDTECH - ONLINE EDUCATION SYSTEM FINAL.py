#IMPORT

import tkinter
from tkinter import *
import mysql.connector as sq
con=sq.connect(host='localhost', user='root',
    passwd='1234', database='project2',
    charset='utf8')
cur=con.cursor()
import random
import webbrowser
from functools import partial



#MAIN HOMEPAGE

window=Tk()
window.geometry('500x500')
window.title('Mainpage')

C=Canvas(window, bg="blue", height=10, width=10)
filename=PhotoImage(file = "D:\Desktop\ip project edtech\mainpage.png")
background_label=Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

def close():
    window.destroy()

l=Label(window, text='EdTech', font=('Ink Free',30,'bold'),
        fg='black').place(x=190,y=220)

Button(window, text='Sign up / Sign in',width=20,
       bg='grey', fg='white',
       command=close).place(x=180,y=400)

window.mainloop()
        

    
#REGISTRATION

user_id= random.randint(100,999)
window=Tk()
window.geometry('500x500')
window.title('Registration')
username=StringVar()
password=StringVar()
password1=StringVar()
usertype=StringVar()

C=Canvas(window, bg="blue", height=10, width=10)
filename=PhotoImage(file = "D:\Desktop\ip project edtech\image2.png")
background_label=Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

def database():
    nm=username.get()
    pw=password.get()
    pw1=password1.get()
    ty=usertype.get()
    qry="select * from USERS where username='%s'"%(nm)
    cur.execute(qry)
    rows=cur.fetchall()
    if rows==[]:
        if pw!=pw1:
            l6=Label(window, text='Passwords do not match' ,
                     width=20, font=('bold',15),
                     fg='red').place(x=160,y=320)
        else:
            qry="insert into Users values(%s,'%s','%s','%s')"%(user_id,nm,pw,ty)
            cur.execute(qry)
            l7=Label(window, text='Registration successful',
                     width=20, font=('bold',15),
                     fg='green').place(x=160,y=320)
            con.commit()
    else:
        l8=Label(window, text='User already exists',
                 width=20, font=('bold',15),
                 fg='red').place(x=160,y=320)

L=Label(window, text="Registration", width=20,
        font=('bold',20))
L.place(x=100, y=30)

L0=Label(window,text=("Your user_id is:",user_id),
         width=20, font=('bold',10)).place(x=90, y=90)

L1=Label(window, text="Enter Username:", width=20,
         font=('bold',10))
L1.place(x=80,y=130)

e1=Entry(window, textvar=username)
e1.place(x=240,y=130)

L2=Label(window, text="Enter Password:", width=20,
         font=('bold',10))
L2.place(x=68, y=180)

e2=Entry(window, textvar=password, show='*')
e2.place(x=240,y=180)

L3=Label(window, text="Re-enter Password:", width=20,
         font=('bold',10))
L3.place(x=70, y=230)

e3=Entry(window, textvar=password1, show='*')
e3.place(x=240, y=230)

L4=Label(window, text="Usertype:", width=20, font=('bold',10))
L4.place(x=85, y=280)

Radiobutton(window, text="Teacher", padx=5, variable=usertype,
            value='Teacher', tristatevalue='x').place(x=220, y=280)
Radiobutton(window, text="Student", padx=25, variable=usertype,
            value='Student', tristatevalue='x').place(x=300, y=280)

Button(window, text='Submit', width=20, bg='grey', fg='white',
       command=database).place(x=180,y=360)
Button(window, text='Next', width=20, bg='grey', fg='white',
       command=close).place(x=180,y=400)
Button(window, text='Already a user? Click here', width=25,bg='grey',
       fg='white', command=close).place(x=160,y=440)

window.mainloop()


#ADDING TABLES
def course():
    window=Tk()
    window.geometry('400x200')
    window.title('Courses')
    cur.execute("select course_code,course_name,description from COURSE")
    i=0
    for x in cur:
        for j in range(len(x)):
            e = Entry(window, width=20, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, x[j])
        i=i+1
    window.mainloop()


def subject(coursecode1):
    window=Tk()
    window.geometry('550x200')
    window.title('Subjects')
    
    c = coursecode1.get()
    cur.execute("select sub_code,sub_name,description from SUBJECTS where course_code=%s "%(c))
    i=0
    for x in cur:
        for j in range(len(x)):
            e = Entry(window, width=30, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, x[j])
        i=i+1
    window.mainloop()

def chapter(subject_code):
    window=Tk()
    window.geometry('650x200')
    window.title('Chapters')
   
    s=subject_code.get()
    
    cur.execute("select chap_code,chap_name,description from CHAPTERS where sub_code=%s"%(s))
    i=0
    for x in cur:
        for j in range(len(x)):
            e = Entry(window, width=35, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, x[j])
        i=i+1
    window.mainloop()
    
def link(chapter_code):
    c2=chapter_code.get()
    qry="select link from CHAPTERS where chap_code=%s"%(c2)
    cur.execute(qry)
    l=cur.fetchone()
    for x in l:
        i=x
    webbrowser.open(i,new=2)
    window.mainloop()



#FOR STUDENTS

def home():
    window=Tk()
    window.geometry('500x500')
    window.title('Home')
    window.configure(bg='misty rose')

    L=Label(window, text='Home', width=20,
            font=('bold',20)).place(x=100,y=30)

    Button(window, text='Show Courses', width=20, bg='grey',
           fg='white', command=course).place(x=50,y=100)
    L1=Label(window, text='Enter CourseCode:', width=20,
             font=('bold',10)).place(x=50,y=140)
    E1=Entry(window)
    E1.place(x=200,y=140)
    Button(window, text='Show Subjects', width=20, bg='grey',
           fg='white', command=partial(subject,E1)).place(x=50,y=200)


    L2=Label(window, text='Enter SubjectCode:', width=20,
             font=('bold',10)).place(x=50,y=240)
    E2=Entry(window)
    E2.place(x=200,y=240)
    Button(window, text='Show Chapters', width=20, bg='grey',
           fg='white', command=partial(chapter,E2)).place(x=50,y=300)


    L3=Label(window, text='Enter ChapterCode:', width=20,
             font=('bold',10)).place(x=50,y=340)
    E3=Entry(window)
    E3.place(x=200,y=340)

    Button(window, text='Next', width=20, bg='grey', fg='white',
           command=partial(link,E3)).place(x=180,y=400)

    window.mainloop()    
    


#FOR TEACHERS
#UPLOAD

def home2():
    window=Tk()
    window.geometry('500x500')
    window.title("UPLOAD")
    window.configure(bg='misty rose')

    def mainpage():
        window=Tk()
        window.geometry('500x500')
        window.title("UPLOAD")
        window.configure(bg='misty rose')
        def chapter():
            chapter_code=StringVar()
            chapter_name=StringVar()
            description=StringVar()
            sub_code=StringVar()
            link=StringVar()

            window.geometry('500x550')
            window.title('upload chapters')
            window.configure(bg='misty rose')
            L=Label(window, text="UPLOAD CHAPTERS", width=20, font=('bold',20))
            L.place(x=100, y=30)

            L1=Label(window, text="Enter Chap_code:", width=20, font=('bold',10))
            L1.place(x=80,y=130)

            e1=Entry(window,width=17,font=(18))
            e1.place(x=240,y=130)

            L2=Label(window, text="Enter Chap_name:", width=20, font=('bold',10))
            L2.place(x=68, y=180)

            e2=Entry(window,width=17,font=(18))
            e2.place(x=240,y=180)

            L3=Label(window, text="Enter Description:", width=20, font=('bold',10))
            L3.place(x=70, y=230)

            e3=Entry(window,width=17,font=(18))

            e3.place(x=240, y=230)

            L4=Label(window, text="Enter Sub_code:", width=20, font=('bold',10))
            L4.place(x=85, y=280)

            e4=Entry(window,width=17,font=(18))
            e4.place(x=240, y=280)

            L5=Label(window, text="Enter link:",width=20, font=('bold',10))
            L5.place(x=89, y=330)

            e5=Entry(window,width=17,font=(18))
            e5.place(x=240, y=330)
            
            def database(a1,b1,c1,d1,e1):
                a=a1.get()
                b=b1.get()
                c=c1.get()
                d=d1.get()
                e=e1.get()
                qry="insert into chapters values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
                cur.execute(qry)
                con.commit()
            Button(window, text="Submit", width=20, bg='grey', fg='white',
                   command=partial(database,e1,e2,e3,e4,e5)).place(x=70,y=370)
            Button(window, text="Return", width=20, bg='grey', fg='white',
                   command=mainpage).place(x=70,y=400)
            window.mainloop()

        def subjects():
            sub_code=StringVar()
            sub_name=StringVar()
            course_code=StringVar()
            description=StringVar()
            window.geometry('500x550')
            window.title('upload subjects')
            window.configure(bg='misty rose')
            L=Label(window, text="UPLOAD SUBJECTS", width=20, font=('bold',20))
            L.place(x=100, y=30)

            L1=Label(window, text="Enter sub_code:", width=20, font=('bold',10))
            L1.place(x=80,y=130)

            e1=Entry(window,width=17,font=(18))
            e1.place(x=240,y=130)

            L2=Label(window, text="Enter sub_name:", width=20, font=('bold',10))
            L2.place(x=68, y=180)

            e2=Entry(window,width=17,font=(18))
            e2.place(x=240,y=180)

            L3=Label(window, text="Enter description:", width=20, font=('bold',10))
            L3.place(x=70, y=230)

            e3=Entry(window,width=17,font=(18))
            e3.place(x=240, y=230)

            L4=Label(window, text="Enter course_code:", width=20, font=('bold',10))
            L4.place(x=85, y=280)

            e4=Entry(window,width=17,font=(18))
            e4.place(x=240, y=280)
            
            def database(a1,b1,c1,d1):
                a=a1.get()
                b=b1.get()
                c=c1.get()
                d=d1.get()
                qry="insert into subjects values('%s','%s','%s','%s')"%(a,b,d,c)
                cur.execute(qry)
                con.commit()
   
            Button(window, text="Submit", width=20, bg='grey', fg='white',
                   command=partial(database,e1,e2,e3,e4)).place(x=70,y=370)
            Button(window, text="Return", width=20, bg='grey', fg='white',
                   command=mainpage).place(x=70,y=400)
            window.mainloop()    
            
        def courses():
            course_code=StringVar()
            course_name=StringVar()
            description=StringVar()
            window.geometry('500x550')
            window.title('upload courses')
            window.configure(bg='misty rose')
            L=Label(window, text="UPLOAD COURSES", width=20, font=('bold',20))
            L.place(x=100, y=30)

            L1=Label(window, text="Enter course_code:", width=20, font=('bold',10))
            L1.place(x=80,y=130)

            e1=Entry(window,width=17,font=(18))
            e1.place(x=240,y=130)

            L2=Label(window, text="Enter course_name:", width=20, font=('bold',10))
            L2.place(x=68, y=180)

            e2=Entry(window)
            e2.place(x=240,y=180,width=17,font=(18))

            L3=Label(window, text="Enter Description:", width=20, font=('bold',10))
            L3.place(x=70, y=230)
            e3=Entry(window,width=17,font=(18))
            e3.place(x=240, y=230)
            
            def database(a1,b1,c1):
                a=a1.get()
                b=b1.get()
                c=c1.get()
                qry="insert into course values('%s','%s','%s')"%(a,b,c)
                cur.execute(qry)
                con.commit()
                
            Button(window, text="Submit", width=20, bg='grey', fg='white',
                   command=partial(database,e1,e2,e3)).place(x=70,y=370)
            Button(window, text="Return", width=20, bg='grey', fg='white',
                   command=mainpage).place(x=70,y=400)
            window.mainloop()
            
        Button(window, text='Add Courses', width=20, bg='grey', fg='white',
               command=courses).place(x=240,y=130)
        Button(window, text='Add Subjects', width=20, bg='grey', fg='white',
               command=subjects).place(x=240,y=180)
        Button(window, text='Add Chapters', width=20, bg='grey', fg='white',
                   command=chapter).place(x=240, y=230)
        window.mainloop()
              

#For Return   
    def chapter():
        chapter_code=StringVar()
        chapter_name=StringVar()
        description=StringVar()
        sub_code=StringVar()
        link=StringVar()

        window.geometry('500x550')
        window.title('upload chapters')
        window.configure(bg='misty rose')
        L=Label(window, text="UPLOAD CHAPTERS", width=20, font=('bold',20))
        L.place(x=100, y=30)

        L1=Label(window, text="Enter Chap_code:", width=20, font=('bold',10))
        L1.place(x=80,y=130)

        e1=Entry(window,width=17,font=(18))
        e1.place(x=240,y=130)

        L2=Label(window, text="Enter Chap_name:", width=20, font=('bold',10))
        L2.place(x=68, y=180)

        e2=Entry(window,width=17,font=(18))
        e2.place(x=240,y=180)

        L3=Label(window, text="Enter Description:", width=20, font=('bold',10))
        L3.place(x=70, y=230)

        e3=Entry(window,width=17,font=(18))
        e3.place(x=240, y=230)

        L4=Label(window, text="Enter Sub_code:", width=20, font=('bold',10))
        L4.place(x=85, y=280)

        e4=Entry(window,width=17,font=(18))
        e4.place(x=240, y=280)

        L5=Label(window, text="Enter link:",width=20, font=('bold',10))
        L5.place(x=89, y=330)

        e5=Entry(window,width=17,font=(18))
        e5.place(x=240, y=330)

        def database(a1,b1,c1,d1,e1):
            a=a1.get()
            b=b1.get()
            c=c1.get()
            d=d1.get()
            e=e1.get()
            qry="insert into chapters values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
            cur.execute(qry)
            con.commit()

        Button(window, text="Submit", width=20, bg='grey', fg='white',
               command=partial(database,e1,e2,e3,e4,e5)).place(x=70,y=370)
        Button(window, text="Return", width=20, bg='grey', fg='white',
               command=mainpage).place(x=70,y=400)
        window.mainloop()
        

    def subjects():
        sub_code=StringVar()
        sub_name=StringVar()
        course_code=StringVar()
        description=StringVar()
        window.geometry('500x550')
        window.title('upload subjects')
        window.configure(bg='misty rose')
        L=Label(window, text="UPLOAD SUBJECTS", width=20, font=('bold',20))
        L.place(x=100, y=30)

        L1=Label(window, text="Enter sub_code:", width=20, font=('bold',10))
        L1.place(x=80,y=130)

        e1=Entry(window,width=17,font=(18))
        e1.place(x=240,y=130)

        L2=Label(window, text="Enter sub_name:", width=20, font=('bold',10))
        L2.place(x=68, y=180)

        e2=Entry(window,width=17,font=(18))
        e2.place(x=240,y=180)

        L3=Label(window, text="Enter Description:", width=20, font=('bold',10))
        L3.place(x=70, y=230)

        e3=Entry(window,width=17,font=(18))
        e3.place(x=240, y=230)

        L4=Label(window, text="Enter course_code:", width=20, font=('bold',10))
        L4.place(x=85, y=280)

        e4=Entry(window,width=17,font=(18))
        e4.place(x=240, y=280)
        
        def database(a1,b1,c1,d1):
            a=a1.get()
            b=b1.get()
            c=c1.get()
            d=d1.get()
            qry="insert into subjects values('%s','%s','%s','%s')"%(a,b,d,c)
            cur.execute(qry)
            con.commit()

        Button(window, text="Submit", width=20, bg='grey', fg='white',
               command=partial(database,e1,e2,e3,e4)).place(x=70,y=370)
        Button(window, text="Return", width=20, bg='grey', fg='white',
               command=mainpage).place(x=70,y=400)
        window.mainloop()
        
        
    def courses():       
        course_code=StringVar()
        course_name=StringVar()
        description=StringVar()
        window.geometry('500x550')
        window.title('upload courses')
        window.configure(bg='misty rose')
        L=Label(window, text="UPLOAD COURSES", width=20, font=('bold',20))
        L.place(x=100, y=30)

        L1=Label(window, text="Enter course_code:", width=20, font=('bold',10))
        L1.place(x=80,y=130)

        e1=Entry(window,width=17,font=(18))
        e1.place(x=240,y=130)

        L2=Label(window, text="Enter course_name:", width=20, font=('bold',10))
        L2.place(x=68, y=180)

        e2=Entry(window,width=17,font=(18))
        e2.place(x=240,y=180)

        L3=Label(window, text="Enter Description:", width=20, font=('bold',10))
        L3.place(x=70, y=230)
        
        e3=Entry(window,width=17,font=(18))
        e3.place(x=240, y=230)
        
        def database(a1,b1,c1):
            a=a1.get()
            b=b1.get()
            c=c1.get()
            qry="insert into course values('%s','%s','%s')"%(a,b,c)
            cur.execute(qry)
            con.commit()

        Button(window, text="Submit", width=20, bg='grey', fg='white',
               command=partial(database,e1,e2,e3)).place(x=70,y=370)
        Button(window, text="Return", width=20, bg='grey', fg='white',
               command=mainpage).place(x=70,y=400)
        window.mainloop()
        
    Button(window, text='Add Courses', width=20, bg='grey', fg='white',
           command=courses).place(x=240,y=130)
    Button(window, text='Add Subjects', width=20, bg='grey', fg='white',
           command=subjects).place(x=240,y=180)
    Button(window, text='Add Chapters', width=20, bg='grey', fg='white',
           command=chapter).place(x=240, y=230)

    window.mainloop()



#HOMEPAGE
    
def homepage():
    nm=username.get()
    qry="select user_type from USERS where username='%s'"%(nm)
    cur.execute(qry)
    ty=cur.fetchone()
    for x in ty:
        i=x
    if i=='Teacher':
        window2=Tk()
        window2.geometry('500x500')
        window2.title('Teacher View')
        window2.configure(bg='misty rose')
        L=Label(window2, text="Teacher View", width=20,
                font=('bold',20))
        L.place(x=100, y=30)
        Button(window2, text='Homepage', width=20 ,bg='grey',
               fg='white', command=home).place(x=180,y=150)
        Button(window2, text='Upload', width=20, bg='grey',
               fg='white', command=home2).place(x=180,y=250)
        window2.mainloop()
    elif i=='Student':
        window3=Tk()
        window3.geometry('500x500')
        window3.title('Student View')
        window3.configure(bg='misty rose')
        L=Label(window3, text="Student View", width=20,
                font=('bold',20))
        L.place(x=100, y=30)
        Button(window3, text='Homepage', width=20 ,bg='grey',
               fg='white', command=home).place(x=180,y=150)
        window3.mainloop()


    
#LOGIN
        
window=Tk()
window.geometry('500x400')
window.title('Login')

C = Canvas(window, bg="blue", height=10, width=10)
filename = PhotoImage(file = "D:\Desktop\ip project edtech\image2.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

username=StringVar()
password=StringVar()
usertype=StringVar()
    

def login():
    nm=username.get()
    pw=password.get()
    ty=usertype.get()
    
    if nm=='' and pw=='':
        l8=Label(window, text="Login unsuccessful \n No details entered",
                 width=15, font=(15), fg='red').place(x=182,y=243.3)
    else:    
        qry='select password from USERS where username="%s"'%(nm)
        cur.execute(qry)
        rows=cur.fetchone()
        for i in rows:
            x=i
        if x==pw:
            l7=Label(window, text='Login successful' , width=20,
                     font=('bold',15), fg='green').place(x=160,y=250)
        else:
            l6=Label(window, text='Wrong Password' ,width=20,
                     font=('bold',15), fg='red').place(x=160,y=250)

L= Label(window, text="Login", width=20,
         font=('bold',20))
L.place(x=100, y=30)

L1=Label(window, text="Enter Username:", width=20,
         font=('bold',10))
L1.place(x=80,y=130)

e1=Entry(window, textvar=username)
e1.place(x=240,y=130)

L2=Label(window, text="Enter Password:", width=20,
         font=('bold',10))
L2.place(x=68, y=180)

e2=Entry(window, textvar=password, show='*')
e2.place(x=240,y=180)

Button(window, text="Submit", width=20, bg='grey', fg='white',
       command=login).place(x=180,y=300)
Button(window, text='Next', width=20, bg='grey', fg='white',
       command=homepage).place(x=180,y=350)

window.mainloop()
