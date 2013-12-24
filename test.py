from Tkinter import *

root = Tk()
root.title('Difficulty')
difficulty = StringVar()
Radiobutton(root, text='Easy', indicatoron=0, variable=difficulty, value='E', width=10, command=root.quit).grid(row=0)
Radiobutton(root, text='Medium', indicatoron=0, variable=difficulty, value='M', width=10, command=root.quit).grid(row=1)
Radiobutton(root, text='Hard', indicatoron=0, variable=difficulty, value='H', width=10, command=root.quit).grid(row=2)

root.mainloop()

print difficulty.get()