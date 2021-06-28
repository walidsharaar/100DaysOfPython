import tkinter

window = tkinter.Tk()
window.title("GUI In Tkinter")
window.minsize(width=500,height=300)

#label

my_label= tkinter.Label(text="I am label",font=("Arial",24,"bold"))
my_label.pack()

def add(*args):
    sum=0
    for n in args:
        sum +=n
    return  sum

print(add(121,323,4123,123,1231,11))













window.mainloop()

