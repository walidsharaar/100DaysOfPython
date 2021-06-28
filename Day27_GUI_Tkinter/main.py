import tkinter

window = tkinter.Tk()
window.title("GUI In Tkinter")
window.minsize(width=500,height=300)

#label

my_label= tkinter.Label(text="I am label",font=("Arial",24,"bold"))
my_label.pack()

my_label.config(text="My Text")

#button
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text="Text Changed")

button = tkinter.Button(text="click me", command=button_clicked)
button.pack()


#Entry component

input = tkinter.Entry()
input.pack()
input.get()











window.mainloop()

