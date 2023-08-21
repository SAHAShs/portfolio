#13//09/22

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import random

class Login:

    
    def bill_area(self):
        #to generate bill number
        x = random.randint(1000,9999)
        self.c_bill_no=StringVar()
        self.c_bill_no.set(str(x))
        self.welcome_soft()
#function to insert values to bill       
    def welcome_soft(self):
        a=(self.current.get()-self.previous.get())*5
        self.txt.delete('1.0',END)
        self.txt.insert(END,"          water bill")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\ncouster name : {str(self.emailid.get())}")
        self.txt.insert(END,f"\nMeter number : {str(self.meter.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\nPrevious reading : {self.previous.get()}")
        self.txt.insert(END,f"\nCurrent reading : {(self.current.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\ntotal liters consumed : {(self.current.get()-self.previous.get())}")
        self.txt.insert(END,"\nper liter cost(INR) : 5")
        self.txt.insert(END,f"\npayment mode :{self.e.get()}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\npayable amount(INR) :{a}")
        messagebox.showinfo("Success","bill generated",parent=self.root)
    
    
    def __init__(self,root):
       
       self.root=root
       self.root.title("Login and registration")
       self.root.geometry("1366x700+0+0")

      #self.root.resizable(False,False)
       self.emailid=StringVar()
       self.password=StringVar()
       self.username=StringVar()
       self.confirmpassword=StringVar()

       self.loginform()
       
#creating login form
    def loginform(self):

      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1366)
#background image
      self.img=ImageTk.PhotoImage(file=r"D:\academics\internship\projects\water billing system\water.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)
#main label
      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white').place(x=75,y=20)
#username
      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=95)

      self.emalid=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.emailid).place(x=30,y=145,width=270,height=35)
#password
      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=195)

      self.pasword=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',show="*",textvariable=self.password).place(x=30,y=245,width=270,height=35)
#login button
      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",
                  bd=0,width=15,height=1).place(x=73,y=340)
#register window button  
      btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',
                  fg="black",bd=0).place(x=100,y=390)


#chekking conditon for logging in
    def login(self):
       
       if self.emailid.get()=="" or self.password.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)

       else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='',database='pythongui')

            cur=con.cursor()

            cur.execute('select * from register where emailid=%s and password=%s',(self.emailid.get(),self.password.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)

               self.email_txt.focus()

            else:

               self.appscreen()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

            
#creaating registration form
    def Register(self):

      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=700,width=1366)
#background image

      self.img=ImageTk.PhotoImage(file=r"D:\academics\internship\projects\water billing system\water.jpg")

      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)
#frame 2
      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=320,y=130,height=450,width=630)


#main label
      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white').place(x=45,y=20)


#username
      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white').place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.username).place(x=30,y=145,width=270,height=35)

      
#password
      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',show="*",textvariable=self.password).place(x=30,y=245,width=270,height=35)

#email id

      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',textvariable=self.emailid).place(x=330,y=145,width=270,height=35)


#confirm password
      label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',show="*",textvariable=self.confirmpassword).place(x=330,y=245,width=270,height=35)


#register button
      btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1).place(x=200,y=340)

        
#login page button
      btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("calibri",10),
                  bg='white',fg="black",bd=0).place(x=215,y=390)




#chekking conditio for registration
    def register(self):
      

       if self.username.get()==""or self.password.get()==""or self.emailid.get()==""or self.confirmpassword.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

       elif self.password.get()!=self.confirmpassword.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

       else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="",database="pythongui")

            cur=con.cursor()

            cur.execute("select * from register where emailid=%s",self.emailid.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)

               self.entry.focus()

            else:
               sql='INSERT INTO register(username,emailid,password,confirmpassword)VALUES(%s,%s,%s,%s)'
               val=(self.username.get(),self.emailid.get(),self.password.get(),self.confirmpassword.get())
               cur.execute(sql,val)

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull",parent=self.root)


         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


#final window 
    def appscreen(self):
        
        Frame_login=Frame(self.root,bg="lightblue")
        Frame_login.place(x=0,y=0,height=700,width=1366)


       
#welcome
        label1=Label(Frame_login,text="Welcome To Water Billing System",font=('times new roman',32,'bold'),fg="black",bg='lightblue')
        label1.place(x=100,y=100)

#meter number
        label2=Label(Frame_login,text="Meter Number",width=20,font=('times new roman',20,'bold'),fg="black",bg='lightblue').place(x=0,y=200)
        self.meter=StringVar()
        e1=Entry(Frame_login,textvariable=self.meter,bd=3,width=15,font=("times new roman",15,"bold"),bg='white').place(x=400,y=205)
#mobile number
        label4=Label(Frame_login,text="Mobile Number",width=20,font=('times new roman',20,'bold'),fg="black",bg='lightblue').place(x=0,y=240)
        self.phone=StringVar()
        e4=Entry(Frame_login,textvariable=self.phone,bd=3,width=15,font=("times new roman",15,"bold"),bg='white').place(x=400,y=245)

#previous reading
        label3=Label(Frame_login,text="Previous Reading",width=20,font=('times new roman',20,'bold'),fg="black",bg='lightblue').place(x=0,y=280)
        self.previous=IntVar()
        e2=Entry(Frame_login,textvariable=self.previous,bd=3,width=15,font=("times new roman",15,"bold"),bg='white').place(x=400,y=285)

#current reading
        label5=Label(Frame_login,text="Current Reading",width=20,font=('times new roman',20,'bold'),fg="black",bg='lightblue').place(x=0,y=320)
        self.current=IntVar()
        e3=Entry(Frame_login,textvariable=self.current,bd=3,width=15,font=("times new roman",15,"bold"),
                bg='white').place(x=400,y=325)
       
#payment mode
        mode=['CASH','UPI','offline']
        self.e=StringVar()
        a=OptionMenu(Frame_login,self.e, *mode).place(x=400,y=360)
        label6=Label(Frame_login,text='Payment mode',width=20,font=('times new roman',20,'bold'),fg="black",bg='lightblue').place(x=0,y=360)

       
#clear button
        clear_btn = Button(Frame_login,text = "Clear",bg = 'orangered',fg ='white',font=("times new roman",15,"bold"),bd = 0,relief = GROOVE,
                          command = self.clear,cursor="hand2")
        clear_btn.place(x=395,y=450)
 
#logout button
        btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",15,"bold"),fg="white",
                   bg="orangered",bd=0,width=15,height=1).place(x=1000,y=30)

#generate billl button
        genbill_btn = Button(Frame_login,text = "Generate Bill",cursor="hand2",bg = 'orangered',fg = 'white',font=("times new roman",15,"bold"),bd = 0,
                            relief = GROOVE,command=self.bill_area)
        genbill_btn.place(x=150,y=450)
       
#exit button
        exit_btn = Button(Frame_login,text = "Exit",bg = 'orangered',fg = 'white',font=("times new roman",15,"bold"),bd = 0,relief = GROOVE,
                         command = self.exit,cursor="hand2")
        exit_btn.place(x=310,y=450)

#Bill Aera
        F3 = Label(self.root,bd = 10,relief = RIDGE,bg='orangered')#border
        F3.place(x = 900,y = 180,width = 325,height = 380)

        bill_title = Label(F3,text = "Bill Area",bg='orangered',font = ("Lucida",13,"bold"),bd= 7,relief = RIDGE)
        bill_title.pack(fill = X)
#scroll bar
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)
        messagebox.showinfo("Success","logged in successfully",parent=self.root)
    
   
 #exit from application     
    def exit(self):
        #s=messagebox.askyesno("alert","do you want to log out",parent=self.root)
        #if self.s.get()=='No':
        self.root.destroy()
        
#claear the billing the area
    def clear(self):
        self.txt.delete('1.0','end')
        messagebox.showinfo("Success","cleared",parent=self.root)
    

root=Tk()

ob=Login(root)

root.mainloop()
