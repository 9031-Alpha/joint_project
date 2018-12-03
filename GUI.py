from tkinter import *
#from tkinter import ttk
#
#class guiFrame:
#    def __init__(self, master):
#        self.master=master;
#        self.frame = Frame(master);
#        self.frame.grid()
#        self.r=0;
#    
#    def addLabel(self, name, height, fontSize):
#        self.name = name;
#        Label(self.frame, text=name, font=('Helvetica',fontSize), height=height).grid(row=self.r);
#        self.r+=1;
#    
def addSeperator(master,height):
    ttk.Separator(master).place(x=0, y=height, relwidth=2)


numBusses=0

def assignValues(event=None):
    global numBusses
    #global bus1
    numBusses = entry1.get()
    print(numBusses)
    first = bus1.get()
    print(first)
    second = bus2.get()
    third = bus3.get()
    print(second)
    print(third)
    solve_method = method.get()
    print(solve_method)



root = Tk();
root.title('Power System Simulator')
root.geometry('700x700')

topFrame = Frame(root)
topFrame.pack()
topLabel = Label(topFrame, text='Welcome to Group 07 Power System Simulator', font=('Helvetica',20), height=2)
topLabel.pack()

addSeperator(root,65)
mainFrame = Frame(root)

label1 = Label(mainFrame, text='Enter Number of Busses:   ', font=('Helvetica',14), height=2)
label1.grid(row=0, column=0)
entry1 = Entry(mainFrame, width=20);
entry1.grid(row=0, column=1)
#entry1.bind('<Return>', assignBusses)
#button1 = Button(mainFrame, text='Submit', command=lambda: assignBusses());
#button1.grid(row=0, column=2, padx=10)


label2 = Label(mainFrame, text='Bus #1:   ', font=('Helvetica',14), height=2)
label2.grid(row=1, column=0, sticky=E)

choices = ['Slack Bus','Load Bus','Generator Bus']
bus1 = StringVar(root)
bus1.set(choices[0])
menu1 = OptionMenu(mainFrame, bus1, *choices)
menu1.config(font=('Helvetica',12))
menu1['menu'].config(font=('Helvetica',12))
menu1.grid(row=1, column=1)

#bus1.trace('w', getBus1)
label3 = Label(mainFrame, text='Bus #2:   ', font=('Helvetica',14), height=2)
label3.grid(row=2, column=0, sticky=E)
bus2 = StringVar(root)
bus2.set(choices[0])
menu2 = OptionMenu(mainFrame, bus2, *choices)
menu2.config(font=('Helvetica',12))
menu2['menu'].config(font=('Helvetica',12))
menu2.grid(row=2, column=1)


label4 = Label(mainFrame, text='Bus #3:   ', font=('Helvetica',14), height=2)
label4.grid(row=3, column=0, sticky=E)
bus3 = StringVar(root)
bus3.set(choices[0])
menu3 = OptionMenu(mainFrame, bus3, *choices)
menu3.config(font=('Helvetica',12))
menu3['menu'].config(font=('Helvetica',12))
menu3.grid(row=3, column=1)

label5 = Label(mainFrame, text='Solver Method:   ', font=('Helvetica',14), height=2)
label5.grid(row=4, column=0, sticky=E)
methods = ['Gauss-Seidel','Newton-Raphson']
method = StringVar(root)
method.set(methods[0])
menu3 = OptionMenu(mainFrame, method, *methods)
menu3.config(font=('Helvetica',12))
menu3['menu'].config(font=('Helvetica',12))
menu3.grid(row=4, column=1)

button = Button(mainFrame, text='Solve', font=('Helvetica',12), command=assignValues)
button.grid(row=4, column=2, padx=200)


mainFrame.place(x=0, y=80, relwidth=2)
root.update()
mainFrame.winfo_height()
addSeperator(root,mainFrame.winfo_height()+100)

















root.mainloop()



