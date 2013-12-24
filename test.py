from Tkinter import *

root = Toplevel()
root.title('Difficulty')
difficulty = StringVar()
Radiobutton(root, text='Easy', indicatoron=0, variable=difficulty, value='E', width=10).grid(row=0)
Radiobutton(root, text='Medium', indicatoron=0, variable=difficulty, value='M', width=10).grid(row=1)
Radiobutton(root, text='Hard', indicatoron=0, variable=difficulty, value='H', width=10).grid(row=2)

#empty label for spacing
Label(root, text='').grid(row=3)

Button(root, text='Okay', command=root.destroy).grid(row=4)

root.mainloop()

print difficulty.get()