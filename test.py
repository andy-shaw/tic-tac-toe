from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.grid(row=0)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.grid(row=1)

    def say_hi(self):
        print "hi there, everyone!"

# root = Tk()

# app = App(root)

# root.mainloop()
# root.destroy()


class MyDialog:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Value").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print "value is", self.e.get()

        self.top.destroy()


root = Tk()
Button(root, text="Hello!").pack()
root.update()

d = MyDialog(root)

root.wait_window(d.top)