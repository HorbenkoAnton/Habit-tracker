import tkinter
from tkinter import *

#I got saving logic, but do i need some kind of manager?
#It will be unclean to use just raw savings methods in GUI i imagine in my head
#So i need some kind of manager to communicate with GUI and use saving methods
#maybe i also need a Week class, to simplify loading, and load by weeks and not days
#cause i planned to show days by weeks, so i can just load one week and don't load whole stuff

#OKAY AND I TOTALLY FORGOT ABOUT CHOOSING A PREDICTING A PRODUCTIVITY LVL


#8 columns
#first column for habits
#then 7 days(whole week)
#first row goes for date
#second row goes for predicted productivity
#all other rows go for habits
#all habits with False state are crosses and with True state goes with a check marks
#can load next previous if i want and go back


#damn i've shoulde have started with creating GUI plan
#Now i need to rewrite whole thing. 
# It isn't that bad though, cause program is small and i got exp.

window = Tk()

label1 = Label(window, text= "Hello")
label2 = Label(window, text= "World")
label3 = Label(window,text = "Hidden label")
label1.pack()
label2.pack()

def show_the_truth():
    label3.pack()

button1 = Button(window, text="Button",command= show_the_truth )
button1.pack()
input = Entry(window,width=15)
input.pack()


def main():
    window.mainloop()

if __name__ == "__main__":
    main()