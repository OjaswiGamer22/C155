from tkinter import *
import random
root=Tk()
root.title("Dictionary")
root.geometry("600x500")
dictionary={"colour":["maroon","lawn green","blue","orange"]}
def bg_change():
    random_no=random.randint(0,3)
    root.configure(background=dictionary["colour"][random_no])
    

    
button1=Button(root,bg="royalblue",text="Change Background colour",command=bg_change) 
button1.place(relx=0.5,rely=0.2,anchor=CENTER)
root.mainloop()

