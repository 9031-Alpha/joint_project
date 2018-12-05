from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class myFrame(Tk):
    def __init__(self, master, region=None):
        Frame.__init__(self, master)
        self.master=master
        self.region=region
        self.inputs = {}
        self.frame = Frame(master)
        self.entry0 = StringVar(master)
        self.entry0.set('')
        self.entry1 = StringVar(master)
        self.entry1.set('')
        self.entry2 = StringVar(master)
        self.entry2.set('')
        self.entry3 = StringVar(master)
        self.entry3.set('')
        self.entry4 = StringVar(master)
        self.entry4.set('')
        self.entry5 = StringVar(master)
        self.entry5.set('')
        self.entry6 = StringVar(master)
        self.entry6.set('')
        self.line12_Real = StringVar(master)
        self.line12_Real.set('')
        self.line12_Imag = StringVar(master)
        self.line12_Imag.set('')
        self.line13_Real = StringVar(master)
        self.line13_Real.set('')
        self.line13_Imag = StringVar(master)
        self.line13_Imag.set('')
        self.line23_Real = StringVar(master)
        self.line23_Real.set('')
        self.line23_Imag = StringVar(master)
        self.line23_Imag.set('')
        self.choices = {'Slack Bus':['1', 'Voltage Magnitude of Slack:', 'Voltage Angle of Slack:'],
                        'Load Bus':['2', 'Real Power of Load:', 'Reactive Power of Load:'],
                        'Generator Bus':['3', 'Real Power of Generator:', 'Voltage Magnitude of Generator:']}
        self.methods = {'Gauss-Seidel':1,'Newton-Raphson':2}
        self.method = StringVar(master)
        self.method.set(list(self.methods.keys())[0])
        self.param1 = StringVar(master)
        self.param1.set(self.choices['Slack Bus'][1])
        self.param2 = StringVar(master)
        self.param2.set(self.choices['Slack Bus'][2])
        self.param3 = StringVar(master)
        self.param3.set(self.choices['Load Bus'][1])
        self.param4 = StringVar(master)
        self.param4.set(self.choices['Load Bus'][2])
        self.param5 = StringVar(master)
        self.param5.set(self.choices['Generator Bus'][1])
        self.param6 = StringVar(master)
        self.param6.set(self.choices['Generator Bus'][2])
        self.line = {'Impedence':1, 'Admittance':0}
        self.lineParam = StringVar(master)
        self.lineParam.set(list(self.line.keys())[0])
        self.bus1 = StringVar(master)
        self.bus1.set(list(self.choices.keys())[0])
        self.bus2 = StringVar(master)
        self.bus2.set(list(self.choices.keys())[1])
        self.bus3 = StringVar(master)
        self.bus3.set(list(self.choices.keys())[2])
        self.result = StringVar(master)
        if self.region == 'TOP':
            self.addTitle()
            self.frame.pack()
            self.addSeperator()
        elif self.region == 'MID':
            self.addBus_number()
            self.frame.pack(fill=BOTH, pady=15)
            self.addSeperator()
        elif self.region == 'BOT':
            self.frame.pack(fill=BOTH, pady=10, expand=1)
            
    def __str__(self):
        Label(self.frame, text='Result:', font=('Helvetica',14), height=2).grid(row=0, column=0, sticky=W)
        Label(self.frame, textvariable=self.result, font=('Helvetica',14), height=2).grid(row=1, column=0)
        return ''
            
    def exitCommand(self):
        self.master.destroy()
            
    def resetBus_number(self, n=None):
        for child in self.frame.winfo_children():
            child.destroy()
        self.addBus_number()
        if n == 1:
            self.getBus_number()
    
    def addBus_number(self):
        Label(self.frame, text='Enter Number of Busses:   ', font=('Helvetica',12), height=2).grid(row=0, column=0, sticky=E)
        Entry(self.frame, width=20, textvariable=self.entry0).grid(row=0, column=1)
        self.submitButton = Button(self.frame, text='Submit', font=('Helvetica',10), command=lambda: self.resetBus_number(1))
        self.submitButton.grid(row=0, column=2, padx=10)
        self.exitButton = Button(self.frame, text='Exit', font=('Helvetica',12), command=lambda: self.exitCommand())
        self.exitButton.grid(row=11, column=8, ipadx=10, pady=30, sticky=W)
    
    def getBus_number(self):
        try:
            self.NumberOfBusses = int(self.entry0.get())
            if self.NumberOfBusses != 2 and self.NumberOfBusses != 3:
                messagebox.showerror('Error','Number of busses should be either 2 or 3 busses.')
            else:
                self.addLabels()
                self.solveButton = Button(self.frame, text='Solve', font=('Helvetica',12), command=lambda: self.getInput_string())
                self.solveButton.grid(row=11, column=6, ipadx=10, pady=30, sticky=E)
                self.resetButton = Button(self.frame, text='Reset', font=('Helvetica',12), command=lambda: self.resetBus_number())
                self.resetButton.grid(row=11, column=7, ipadx=10, pady=30, sticky=W)
        except ValueError:
            messagebox.showerror('Error','Number of busses should be a numeric value.')
                
    def addEntries(self):
        Entry(self.frame, width=20, textvariable=self.entry1).grid(row=1, column=4)
        Entry(self.frame, width=20, textvariable=self.entry2).grid(row=2, column=4)
        Entry(self.frame, width=20, textvariable=self.entry3).grid(row=3, column=4)
        Entry(self.frame, width=20, textvariable=self.entry4).grid(row=4, column=4)
        Entry(self.frame, width=15, textvariable=self.line12_Real).grid(row=8, column=1, sticky=E)
        Entry(self.frame, width=15, textvariable=self.line12_Imag).grid(row=8, column=3, sticky=W)
        if self.NumberOfBusses == 3:
            Entry(self.frame, width=20, textvariable=self.entry5).grid(row=5, column=4)
            Entry(self.frame, width=20, textvariable=self.entry6).grid(row=6, column=4)
            Entry(self.frame, width=15, textvariable=self.line13_Real).grid(row=9, column=1, sticky=E)
            Entry(self.frame, width=15, textvariable=self.line13_Imag).grid(row=9, column=3, sticky=W)
            Entry(self.frame, width=15, textvariable=self.line23_Real).grid(row=10, column=1, sticky=E)
            Entry(self.frame, width=15, textvariable=self.line23_Imag).grid(row=10, column=3, sticky=W)
        self.addOptions()
    
    def addLabels(self):
        Label(self.frame, text='Parameters:', font=('Helvetica',12), height=2).grid(row=0, column=3, padx=50, sticky=E)
        Label(self.frame, text='Bus #1:   ', font=('Helvetica',12), height=2).grid(row=1, column=0, sticky=E)
        Label(self.frame, text='Bus #2:   ', font=('Helvetica',12), height=2).grid(row=3, column=0, sticky=E)
        Label(self.frame, textvariable=self.param1, font=('Helvetica',12), height=2).grid(row=1, column=3, padx=50, sticky=E)
        Label(self.frame, textvariable=self.param2, font=('Helvetica',12), height=2).grid(row=2, column=3, padx=50, sticky=E)
        Label(self.frame, textvariable=self.param3, font=('Helvetica',12), height=2).grid(row=3, column=3, padx=50, sticky=E)
        Label(self.frame, textvariable=self.param4, font=('Helvetica',12), height=2).grid(row=4, column=3, padx=50, sticky=E)
        Label(self.frame, text='Line Parameter:', font=('Helvetica',12), height=2).grid(row=7, column=0, pady=3, sticky=E)
        Label(self.frame, text='Line 1-2:', font=('Helvetica',12), height=2).grid(row=8, column=0, sticky=E)
        Label(self.frame, text='+', font=('Helvetica',12), height=2).grid(row=8, column=2)
        Label(self.frame, text='j', font=('Helvetica',12), height=2).grid(row=8, column=3)
        Label(self.frame, text='Solver Method:', font=('Helvetica',12), height=2).grid(row=8, column=4, sticky=E)
        if self.NumberOfBusses == 3:
            Label(self.frame, text='Bus #3:   ', font=('Helvetica',12), height=2).grid(row=5, column=0, sticky=E)
            Label(self.frame, textvariable=self.param5, font=('Helvetica',12), height=2).grid(row=5, column=3, padx=50, sticky=E)
            Label(self.frame, textvariable=self.param6, font=('Helvetica',12), height=2).grid(row=6, column=3, padx=50, sticky=E)
            Label(self.frame, text='Line 1-3:', font=('Helvetica',12), height=2).grid(row=9, column=0, sticky=E)
            Label(self.frame, text='+', font=('Helvetica',12), height=2).grid(row=9, column=2)
            Label(self.frame, text='j', font=('Helvetica',12), height=2).grid(row=9, column=3)
            Label(self.frame, text='Line 2-3:', font=('Helvetica',12), height=2).grid(row=10, column=0, sticky=E)
            Label(self.frame, text='+', font=('Helvetica',12), height=2).grid(row=10, column=2)
            Label(self.frame, text='j', font=('Helvetica',12), height=2).grid(row=10, column=3)
        self.addEntries()
    
    def addOptions(self):
        self.menu1 = OptionMenu(self.frame, self.bus1, *list(self.choices.keys()), command=self.getChoices)
        self.menu1.config(font=('Helvetica',10))
        self.menu1['menu'].config(font=('Helvetica',10))
        self.menu1.grid(row=1, column=1, sticky=E)
        
        self.menu2 = OptionMenu(self.frame, self.bus2, *list(self.choices.keys()), command=self.getChoices)
        self.menu2.config(font=('Helvetica',10))
        self.menu2['menu'].config(font=('Helvetica',10))
        self.menu2.grid(row=3, column=1, sticky=E)
        
        self.menu4 = OptionMenu(self.frame, self.lineParam, *list(self.line.keys()))
        self.menu4.config(font=('Helvetica',10))
        self.menu4['menu'].config(font=('Helvetica',10))
        self.menu4.grid(row=7, column=1, sticky=E)
        
        self.menu5 = OptionMenu(self.frame, self.method, *list(self.methods.keys()))
        self.menu5.config(font=('Helvetica',10))
        self.menu5['menu'].config(font=('Helvetica',10))
        self.menu5.grid(row=8, column=5, sticky=W)
        
        if self.NumberOfBusses == 3:
            self.menu3 = OptionMenu(self.frame, self.bus3, *list(self.choices.keys()), command=self.getChoices)
            self.menu3.config(font=('Helvetica',10))
            self.menu3['menu'].config(font=('Helvetica',10))
            self.menu3.grid(row=5, column=1, sticky=E)
    
    def getChoices(self, event=None):
        self.firstBus = self.bus1.get()
        self.secondBus = self.bus2.get()
        self.lineValue = self.lineParam.get()
        self.solverMethod = self.method.get()
        if self.NumberOfBusses == 3:
            self.thirdBus = self.bus3.get()
        self.updateLabels()
    
    def updateLabels(self, event=None):
        self.param1.set(self.choices[self.firstBus][1])
        self.param2.set(self.choices[self.firstBus][2])
        self.param3.set(self.choices[self.secondBus][1])
        self.param4.set(self.choices[self.secondBus][2])
        if self.NumberOfBusses == 3:
            self.param5.set(self.choices[self.thirdBus][1])
            self.param6.set(self.choices[self.thirdBus][2])
    
    def addTitle(self):
        Label(self.frame, text='Welcome to Group 07 Power System Simulator', font=('Helvetica',20), height=2).pack()
    
    def addSeperator(self):
        ttk.Separator(self.master).pack(fill=X)

    def getInput_string(self):
        try:
            self.bus1_firstParameter = float(self.entry1.get())
            self.bus1_secondParameter = float(self.entry2.get())
            self.bus2_firstParameter = float(self.entry3.get())
            self.bus2_secondParameter = float(self.entry4.get())
            self.line12 = complex(float(self.line12_Real.get()),float(self.line12_Imag.get()))
            if self.NumberOfBusses == 3:
                self.bus3_firstParameter = float(self.entry5.get())
                self.bus3_secondParameter = float(self.entry6.get())
                self.line13 = complex(float(self.line13_Real.get()),float(self.line13_Imag.get()))
                self.line23 = complex(float(self.line23_Real.get()),float(self.line23_Imag.get()))
        except ValueError:
                messagebox.showerror('Error','Inputs should be numeric values.')
        self.getInputs()
                
    def getInputs(self):
        self.NumberOfBusses = int(self.entry0.get())
        self.getChoices()
        self.firstParameter = self.choices[self.firstBus][1]
        self.secondParameter = self.choices[self.firstBus][2]
        self.thirdParameter = self.choices[self.secondBus][1]
        self.fourthParameter = self.choices[self.secondBus][2]
        self.inputs['Number of busses'] = self.NumberOfBusses
        self.inputs['Bus 1'] = int(self.choices[self.firstBus][0])
        self.inputs['Bus 2'] = int(self.choices[self.secondBus][0])
        self.inputs[self.firstParameter[:-1]] = self.bus1_firstParameter
        self.inputs[self.secondParameter[:-1]] = self.bus1_secondParameter
        self.inputs[self.thirdParameter[:-1]] = self.bus2_firstParameter
        self.inputs[self.fourthParameter[:-1]] = self.bus2_secondParameter
        self.inputs['Line Parameter'] = self.line[self.lineValue[:]]
        self.inputs['Line 1-2'] = self.line12
        self.inputs['Analysis Method'] = self.methods[self.solverMethod]
        if self.NumberOfBusses == 3:
            self.fifthParameter = self.choices[self.thirdBus][1]
            self.sixthParameter = self.choices[self.thirdBus][2]
            self.inputs['Bus 3'] = int(self.choices[self.thirdBus][0])
            self.inputs[self.fifthParameter[:-1]] = self.bus3_firstParameter
            self.inputs[self.sixthParameter[:-1]] = self.bus3_secondParameter
            self.inputs['Line 1-3'] = self.line13
            self.inputs['Line 2-3'] = self.line23
        main()
    
def main():
    print(midFrame.inputs)
    botFrame.result.set('This is the results section')
    print(botFrame)



root = Tk();
root.title('Power System Simulator')
root.geometry('1220x850')
topFrame = myFrame(root, 'TOP')
midFrame = myFrame(root, 'MID')
botFrame = myFrame(root, 'BOT')
root.mainloop()
        
        













