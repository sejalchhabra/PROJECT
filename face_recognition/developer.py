from tkinter import*
from PIL import Image,ImageTk


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")
        


        title=Label(self.root,text="DEVELOPER INFORMATION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title.place(x=0,y=(-1),width=1550,height=45)


        img11 = Image.open(r"college_images\dev.jpg")
        img11 = img11.resize((1530,700), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl=Label(self.root,image=self.photoImg11)
        bg_lbl.place(x=10,y=65,width=1530,height=700)

        frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="black")
        frame.place(x=700,y=70,width=450,height=250)

        title1=Label(self.root,text="Sejal ",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title1.place(x=755,y=150,width=120,height=55)        
        title1=Label(self.root,text="sejalchhabra98@gmail.com",font=("times new roman",15,"bold"),bg="black",fg="blue")
        title1.place(x=750,y=210,width=260,height=55)   
        title1=Label(self.root,text="7652928338",font=("times new roman",15,"bold"),bg="black",fg="blue")
        title1.place(x=690,y=270,width=250,height=55)         
        btnReset=Button(title,text="Back",command=self.go_back,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        btnReset.pack(side=RIGHT)
        
    def go_back(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()