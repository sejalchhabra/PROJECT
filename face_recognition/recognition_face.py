from re import L
from tkinter import*
from tkinter import ttk
from turtle import heading, width
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import cv2
import os
from datetime import datetime
from tkinter import filedialog
from numpy import place
import pyttsx3
import csv
from attendance import Attendace

class Recognition_Face:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")   
        self.root.title("Face Recognition Attendance System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")
    


        # ==================Face Detector Button ===========================================
        img=Image.open("college_images/dev.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoImg1=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoImg1,bd=20)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        img_logo11 = Image.open("college_images/face_detector1.jpg")
        img_logo11 = img_logo11.resize((650,700), Image.ANTIALIAS)
        self.photoImg_logo11= ImageTk.PhotoImage(img_logo11)
        bg_lbl12=Label(self.root,image=self.photoImg_logo11,bd=20)
        bg_lbl12.place(x=0,y=40,width=650,height=700)
        title=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="black",fg="blue")
        title.place(x=0,y=0,width=1530,height=50)     
  
        title1=Label(self.root,text="Frontal Face recognition",font=("times new roman",20,"bold"),bg="white",fg="blue")
        title1.pack(side=BOTTOM,fill=X)
        Back_Button=Button(title,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.pack(side=RIGHT)

        b3 =Button(bg_img,text="Face Recognition",command=self.detect_face,borderwidth=6,font=("times new roman",18,"bold"),bg="darkblue",activebackground="red",fg="white",cursor="hand2")
        b3.place(x=900,y=300,width=400,height=200)

        

    # ======================================= mark Attendance =========================================================
    
    def mark_attendace(self,d,k,s,i):
        with open("attendance/present.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry=line.split(",")
                name_List.append(entry[0])
            if ((s not in name_List) and (i not in name_List) and(k not in name_List)  and (d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{d},{k},{i},{s},{dtString},{d1},Present")
    #************************************************************

   

    def detect_face(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coords=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                
                id,pred=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-pred/300)))

                conn=mysql.connector.connect(host='127.0.0.1',username='root',password='Sejal@oracle1',database='facee_recognition')
                my_cursor=conn.cursor()

                my_cursor.execute("select student_name from new_student where id="+str(id))
                i = my_cursor.fetchone()
                i = ''+''.join(i)

                my_cursor.execute("select department from new_student where id="+str(id))
                s = my_cursor.fetchone()
                s =''+''.join(s)

                my_cursor.execute("select roll from new_student where id="+str(id))
                k = my_cursor.fetchone()
                k = ''+''.join(k)

                my_cursor.execute("select student_id from new_student where id="+str(id))
                d = my_cursor.fetchone()
                d = ''+''.join(d)

                if confidence>77:
                    cv2.putText(img,f"Department:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2) 
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
                    cv2.putText(img,f"Roll No:{k}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
                    cv2.putText(img,f"Student Id:{d}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
                    self.mark_attendace(d,k,s,i)

                         
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
                coords=[x,y,w,h]    
            return coords

        def recognize(img,clf,faceCascade):
            coords=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        Video_Capture=cv2.VideoCapture(0,)

        while True:
            ret,img=Video_Capture.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Detector",img)
            if cv2.waitKey(1)==13:
                break    
        Video_Capture.release()
        messagebox.showinfo("Attendance Report","Attendance Saved in csv file",parent=self.root)
        cv2.destroyAllWindows()




    
if __name__ == "__main__":
    root=Tk()
    obj=Recognition_Face(root)
    root.mainloop()