from tkinter import *

class Statics:
    def __init__(self, master):
        self.master = master
        root.geometry("300x400")
        master.title("Static Station Finder")

        master.bind("<Return>", lambda x: self.add())
        
        self.label = Label(master, text="Choose Map File (.htm)")
        self.label.place(x=0,y=0)


        
        frame = Frame(master)
        scrollbar = Scrollbar(master, orient=VERTICAL)
        
        self.select_button = Button(master, text="Select File", command=self.select)
        self.select_button.place(x=50, y=20, in_=root)
        
        self.e = Entry(master, width=20)
        self.e.place(x=10, y=50, in_=root)

        self.listy = Listbox(master, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listy.yview)
        scrollbar.place(x=140,y=150)
        self.listy.place(x=10, y=80)

        self.add_button = Button(master, text="Add Asset", command=self.add)
        self.add_button.place(x=140, y=45, in_=root)

        self.remove_button = Button(master, text="Remove Asset", command=self.remove)
        self.remove_button.place(x=140, y=75, in_=root)

        self.clear_button = Button(master, text="Clear List", command=self.clear)
        self.clear_button.place(x=140, y=105, in_=root)

        self.generate_button = Button(master, text="Generate Map", command=self.generate)
        self.generate_button.place(x=140, y=215, in_=root)
        

    def add(self):
        s = self.e.get()
        self.listy.insert(END, s)
        print("add item: " + s)
        self.e.delete(0,END)

    def remove(self):
        self.listy.delete(ANCHOR)
        print("remove item")

    def clear(self):
        self.listy.delete(0,END)
        print("clear list")

    def generate(self):
        print("generate map")

    def select(self):
        print("select file")


        

root = Tk()
my_gui = Statics(root)
root.mainloop()
