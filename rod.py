from tkinter import*
def buttonPushed():
    print("Button Pushed!");

root=Tk()
w=Label(root, text="Hello,WORLD!")#Create a label with words
w.pack()#Put the label into the window 
myButton=Button(root, text="Exit",command=buttonPushed)
myButton.pack()

root.mainloop()