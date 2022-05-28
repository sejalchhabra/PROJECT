from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    #pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from setuptools import Command
from main_project import FaceRecognitionSystem
from my_first_chatbot import ChatBot


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")

        img1 = Image.open("college_images/2-AI-invades-automobile-industry-in-2019.jpeg")
        img1 = img1.resize((1530,800), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,width=1530,height=800)

        title=Label(bg_lbl,text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title.place(x=0,y=120,width=1550,height=45)

        
        img10 = Image.open("college_images/facial-recognition_0.jpg")
        img10 = img10.resize((500,120), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl1=Label(bg_lbl,image=self.photoImg10)
        bg_lbl1.place(x=0,y=0,width=500,height=120)

        img11 = Image.open("college_images/face.jpg")
        img11 = img11.resize((500,120), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl22=Label(bg_lbl,image=self.photoImg11)
        bg_lbl22.place(x=500,y=0,width=500,height=120)

        img13 = Image.open("college_images/smart-attendance.jpg")
        img13 = img13.resize((550,120), Image.ANTIALIAS)
        self.photoImg13= ImageTk.PhotoImage(img13)
        bg_lbl12=Label(bg_lbl,image=self.photoImg13)
        bg_lbl12.place(x=1000,y=0,width=550,height=120)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=430)

        img14 = Image.open("college_images/chat.jpg")
        img14 = img14.resize((50,50), Image.ANTIALIAS)
        self.photoImg14= ImageTk.PhotoImage(img14)
        bg_lbl3=Label(frame,image=self.photoImg14)
        bg_lbl3.place(x=290,y=380,width=50,height=50)
        photo_label=Button(frame,text="chat",command=self.chat,borderwidth=5,cursor="hand2",font="comicsansns 7 bold",fg="white",bg="darkblue")
        photo_label.place(x=290,y=370,width=50,height=20)



        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=85)

        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="black")
        username.place(x=70,y=125)


        self.txtuser=StringVar()
        self.txtpass=StringVar()

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        txtuser.place(x=40,y=150,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="black")
        password.place(x=70,y=195)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"),show="*")
        txtpass.place(x=40,y=220,width=270)


        # LoginButton
        btn_login=Button(frame,text="Login",borderwidth=3,relief=RAISED,command=self.login,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        btn_login.place(x=110,y=270,width=120,height=35)
        # registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=320,width=160)

        # forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=340,width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="Sejal@oracle1",database="facee_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Inavalid Username & password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority Person",parent=self.root)
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
    def chat(self):    
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)     

    # =====================reset password=======================================
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="root",password="Sejal@oracle1",database="facee_recognition")
                cur=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error","Please select the correct security quetion/Enter answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    cur.execute(query,value)
                    # row2=cur.fetchone()
                    conn.commit() 
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    # self.reset()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root2)
        
        
    # =============================================forgrt password window=============================      
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plaese Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="Sejal@oracle1",database="facee_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Plaese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+200")
                self.root2.configure(bg="white")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_securiy_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_securiy_Q.place(x=50,y=110,width=250)
                self.combo_securiy_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="White",bg="green")
                btn.place(x=120,y=290,width=100)
 


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==================varibles====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        

        # ============bg image==================
        self.bg=ImageTk.PhotoImage(file="college_images/employee_img2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        # ============left image==================
        self.bg1=ImageTk.PhotoImage(file="college_images/thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # ==============main Frame=====================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ==============label and entry============================
        # ------------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # -----------------row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # ------------------row3

        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_securiy_Q.place(x=50,y=270,width=250)
        self.combo_securiy_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # ----------------------row4

        pswd=Label(frame,text="Password ",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ===================checkbutton=================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",bg='white',font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        b1=Button(frame,text="Register Now",command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg='green',fg='white')
        b1.place(x=50,y=420,width=200)

        b2=Button(frame,text="Login",command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg='blue',fg='white')
        b2.place(x=330,y=420,width=200)



    # =================Function declaration============================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plaese agree our terms ane condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="Sejal@oracle1",database="facee_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,plaese try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()
            



if __name__ == "__main__":
    main()
  