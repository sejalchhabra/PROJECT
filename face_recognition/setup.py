import cx_Freeze
import sys
import os
base=None

if sys.platform=="win32":
    base ="win32GUI"

os.environ['TCL_LIBRARY'] =r"C:\Users\91765\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\91765\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables=[cx_Freeze.Executable("face_recognition_attendance_software.py",base=base,icon="face.ico")]

cx_Freeze.setup(
    name="Face Recognition attendance software",
    Options={"build_exe":{"packages": ["tkinter","os"],"include_files":["face.ico","tcl86t.dll","tk86t.dll","college_images","collect_sample","database","attendance"]}},
    version ="1.0",
    description="Face Recognition attendance system ",
    executables = executables
)