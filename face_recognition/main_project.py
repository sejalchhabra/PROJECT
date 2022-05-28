from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from tkinter import messagebox
from student import Student
from train import Train_Data
from recognition_face import Recognition_Face
from attendance import Attendace
from developer import Developer
from my_first_chatbot import ChatBot


class FaceRecognitionSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.wm_iconbitmap("face.ico")
    

        # ===============Images==================================
        img10 = Image.open("college_images//face-recognition.png")
        img10 = img10.resize((500,200), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl=Label(self.root,image=self.photoImg10)
        bg_lbl.place(x=0,y=0,width=500,height=200)

        img11 = Image.open("college_images/face.jpg")
        img11 = img11.resize((500,200), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl=Label(self.root,image=self.photoImg11)
        bg_lbl.place(x=500,y=0,width=500,height=200)

        img13 = Image.open("college_images/smart-attendance.jpg")
        img13 = img13.resize((550,200), Image.ANTIALIAS)
        self.photoImg13= ImageTk.PhotoImage(img13)
        bg_lbl=Label(self.root,image=self.photoImg13)
        bg_lbl.place(x=1000,y=0,width=550,height=200)



        # ====================Background image==============================================
        img1 = Image.open("college_images/ring.webp")
        img1 = img1.resize((1600,710), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=200,width=1600,height=710)

        # ==================== Project title ==================================================
        title=Label(bg_lbl,text="FACE RECOGNITION ATTENDACE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="black",fg="white")
        title.place(x=0,y=(-2),width=1540,height=45)

        # ==================== Project buttom(description) ==================================================
        downtitle=Label(self.root,text="",font=("times new roman",20,"bold"),bd=2,relief=RAISED,bg="black",fg="red")
        downtitle.place(x=0,y=745,width=1600,height=40)

        # =================time================================
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(title, font = ('times new roman',14, 'bold'),background = 'white',foreground = 'blue') 
        lbl.place(x=0,y=(-15),width=110,height=50) 
        time() 


        # ==================Employee Department Button ===========================================
        
        img2 = Image.open("college_images/gettyimages-1022573162.jpg")
        img2 = img2.resize((220,150), Image.ANTIALIAS)
        self.photoImg2 =  ImageTk.PhotoImage(img2)
        self.b2 =Button(self.root,image=self.photoImg2,borderwidth=2,fg="red", width=220,cursor="hand2")
        self.b2.place(x=20,y=280,width=220,height=150)


        b3 =Button(self.root,text="STUDENT DETAILS",command=self.Manage_Emp,borderwidth=5,font="comicsansns 15 bold",bg="darkblue",fg="white",cursor="hand2")
        b3.place(x=20,y=430,width=220,height=30)



        # ==================Train Button ===========================================
        img3 = Image.open("college_images/TRAIN.WEBP")
        img3 = img3.resize((220,150), Image.ANTIALIAS)
        self.photoImg3 =  ImageTk.PhotoImage(img3)
        b3 =Button(self.root,image=self.photoImg3,text="Face Detector",bd=2,relief=SUNKEN,font=("times new roman",22,"bold"),fg="white", width=220,cursor="hand2")
        b3.place(x=260,y=520,width=220,height=150)

        photo_label=Button(self.root,text="TRAIN DATA",command=self.train_window,cursor="hand2",borderwidth=8,font="comicsansns 15 bold",bg="darkblue",fg="white")
        photo_label.place(x=260,y=660,width=220,height=30)

        # ==================Face Detector Button ===========================================
        img = Image.open("college_images/face_detector1.jpg")
        img = img.resize((220,150), Image.ANTIALIAS)
        self. photoImg =  ImageTk.PhotoImage(img)
        b1 =Button(self.root,image=self.photoImg,text="FACE DETECTOR",bd=2,relief=SUNKEN,font=("times new roman",22,"bold"),fg="lime", width=220,cursor="hand2")
        b1.place(x=520,y=280,width=220,height=150)

        face_label=Button(self.root,text="FACE RECOGNITION",command=self.detect_window,cursor="hand2",bd=8,font="comicsansns 15 bold",fg="white",bg="darkblue")
        face_label.place(x=520,y=430,width=220,height=30)

        # ==================Sample Image Button ===========================================
        img4 = Image.open("college_images/sample.jpg")
        img4 = img4.resize((220,150), Image.ANTIALIAS)
        self.photoImg4 =  ImageTk.PhotoImage(img4)
        b4 =Button(self.root,image=self.photoImg4,text="Photo",font=("times new roman",22,"bold"),bd=2,relief=SUNKEN,fg="white", width=220,cursor="hand2")
        b4.place(x=780,y=520,width=220,height=150)

        photo_label=Button(self.root,text="PHOTOS",command=self.open_photo,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkblue")
        photo_label.place(x=780,y=660,width=220,height=30)

        # ==================Attendace report Button ===========================================
        img5 = Image.open("college_images/report.jpg")
        img5 = img5.resize((220,150), Image.ANTIALIAS)
        self.photoImg5 =  ImageTk.PhotoImage(img5)
        b5 =Button(self.root,image=self.photoImg5,text="Attendance Report",bd=2,relief=SUNKEN,font=("times new roman",22,"bold"),fg="red", width=220,cursor="hand2")
        b5.place(x=1040,y=280,width=220,height=150)

        photo_label=Button(self.root,text="ATTENDANCE",borderwidth=5,command=self.attendance_report,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkblue")
        photo_label.place(x=1040,y=430,width=220,height=30)
        # ==================Developer Image Button ===========================================
        img7 = Image.open("college_images/dev.jpg")
        img7 = img7.resize((220,220), Image.ANTIALIAS)
        self.photoImg7 =  ImageTk.PhotoImage(img7)
        b7 =Button(self.root,image=self.photoImg7,text="Photo",font=("times new roman",22,"bold"),bd=2,relief=SUNKEN,fg="white", width=220,cursor="hand2")
        b7.place(x=1300,y=520,width=220,height=150)

        photo_label=Button(self.root,text="DEVELOPER",command=self.developer_window,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkblue")
        photo_label.place(x=1300,y=660,width=220,height=30)

        # ==================Exit Image Button ===========================================

        photo_label=Button(self.root,text="EXIT",command=self.iExit,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkblue")
        photo_label.place(x=1450,y=20,width=70,height=30)

    def Logout(self):
        self.root.destroy()

    # ================== Exit function =======================================================================
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Detector System","Confirm you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    def open_photo(self):
        os.startfile("collect_sample")

  
# # ============================================ Another window fuctions ========================================
    def Manage_Emp(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_report(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendace(self.new_window)

    def train_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)  

    def detect_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition_Face(self.new_window) 

    def developer_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)   



if __name__ == '__main__':
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()
    
 
  


   



