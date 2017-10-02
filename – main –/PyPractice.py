from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry('300x40')

k=0
def button_clicked():
    global k
    k+=1
    print(k)

def close():
    root.destroy()
    root.quit()

button = Button(root, text="Press Me", command=button_clicked)
button.pack(fill=BOTH)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()