from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from login import Login_Window
class enter:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("matrimonial website")
        self.root.wm_iconbitmap("face.ico")


        img=Image.open(r"college_images/Face-Recognitionfinal.jpg")
        img=img.resize((1500,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=770)
       
        title_lbl=Label(text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="WHITE",fg="BLUE")
        title_lbl.place(x=380,y=20,width=900,height=50)


        b1=Button(text="GET IN",cursor="hand2",command=self.getin,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1.place(x=780,y=450,width=220,height=100)
    def  getin(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)
if __name__=="__main__":
    root=Tk()
    obj=enter(root)
    root.mainloop()