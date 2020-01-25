import tkinter as tk
import tkinter

# EXAMPLE WINDOW 1
# window = tkinter.Tk()

# window.title("Gui")

# label = tkinter.Label(window, text="Hello World").pack()
# window.mainloop()


# EXAMPLE BUTTON
# def write_slogan():
#     print("Tkinter is easy to use!")


# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame,
#                    text="QUIT",
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Hello",
#                    command=write_slogan)
# slogan.pack(side=tk.LEFT)

# root.mainloop()


# EXAMPLE COUNTER in seconds
counter = 0

def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()


root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()




# Non-starter tutorials
# l1 = tkinter.Label(window, text="edureka!" )
# font=("Arial Bold", 50))

# l1.grid(column=0, row=0)


# from tkinter import *

# window = TK()
# window.title("Example window")

# window.mainloop()


# from tkinter import *


# root = Tk()
# app = Window(root)

# class Window(Frame):
#   def __init__(self, master=None) :
#     Frame.__init__(self, master)
#     self.master = master

#     root.wm_title("Tkinter window")

#     root.mainloop()
