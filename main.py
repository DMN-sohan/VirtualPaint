import tkinter
import subprocess
from tkinter import CENTER, RIGHT, TOP, messagebox

top = tkinter.Tk()
top.geometry('300x200')
top.title('Paint 3D')

def color_sorter():
    messagebox.showinfo("Color Picker", "Use this tool to select your color. Keep the object of color in frame and move the slide bars until only the object is in white in the second window. Double click [q] to save the color values and double click [s] to end the program. The window will open shortly after clicking OK.")
    subprocess.run(["python","color_sorter.py"])
def paint():
    messagebox.showinfo("Paint", "Keep the object in frame and move it. If the color values have been recorded correctly then the program will trace the object and draw at a point. Double click [c] to clear the screen and double click [s] to quit.")
    subprocess.run(["python","paint.py"])

cp = tkinter.Button(top, text ="Color Picker", command = color_sorter)
p = tkinter.Button(top,text="Paint" , command = paint)

c=0.15

cp.place(relx=0.5,rely=0.125+c,anchor=CENTER)
p.place(relx=0.5,rely=0.275+c,anchor=CENTER)

top.mainloop()
