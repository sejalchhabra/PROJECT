from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
from datetime import datetime
from tkinter import filedialog
import pyttsx3
import csv

class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

        # ==================Train label Button ===========================================

        img_logob = Image.open("college_images/BGG.PNG")
        img_logob = img_logob.resize((1530,790), Image.ANTIALIAS)
        self.photoImg_logo1b= ImageTk.PhotoImage(img_logob)
        bg_lbl=Label(self.root,image=self.photoImg_logo1b,bd=20)
        bg_lbl.place(x=0,y=0,width=1530,height=790)
        title=Label(self.root,text="TRAIN YOUR PHOTOS",font=("times new roman",35,"bold"),bg="BLACK",fg="red")
        title.place(x=0,y=0,width=1530,height=55)

        img_logo = Image.open("college_images/Infection-Control-Training-.jpg")
        img_logo = img_logo.resize((765,200), Image.ANTIALIAS)
        self.photoImg_logo1= ImageTk.PhotoImage(img_logo)
        bg_lbl1=Label(self.root,image=self.photoImg_logo1,bd=20)
        bg_lbl1.place(x=0,y=55,width=765,height=200)

        img_logo11 = Image.open("college_images/h116.jpg")
        img_logo11 = img_logo11.resize((765,200), Image.ANTIALIAS)
        self.photoImg_logo11= ImageTk.PhotoImage(img_logo11)
        bg_lbl12=Label(self.root,image=self.photoImg_logo11,bd=20)
        bg_lbl12.place(x=765,y=55,width=765,height=200)

        title1=Label(self.root,text="",font=("times new roman",35,"bold"),bg="BLACK",fg="red")
        title1.place(x=0,y=250,width=1530,height=50)

        b3 =Button(self.root,text="TRAIN DATA",command=self.train_classifier,borderwidth=15,font=("times new roman",25,"bold"),bg="darkblue",activebackground="red",fg="white",cursor="hand2")
        b3.place(x=900,y=380,width=400,height=200)

        
        btnReset=Button(title,text="Back",command=self.go_back,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        btnReset.pack(side=RIGHT)

    def go_back(self):
        self.root.destroy()

# ======================================== train datasets ===========================================
    def train_classifier(self):
        data_dir="collect_sample"
        path=[os.path.join(data_dir,f) for f in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L');  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # Train the classifier and save
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()