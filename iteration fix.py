# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:07:59 2018

@author: Mohamed Omer Airaj
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
import numpy as np
from numpy import *
from numpy import matrix
from numpy import linalg


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
            self.frame.pack(fill=BOTH, pady=13)
            self.addSeperator()
        elif self.region == 'BOT':
            self.frame.pack(fill=BOTH, pady=10, expand=1)
            
    def __str__(self):
        Label(self.frame, text='Result:', font=('Helvetica',14), height=2).grid(row=0, column=0, sticky=W)
        Label(self.frame, textvariable=self.result, font=('Helvetica',10), height=6).grid(row=1, column=0)
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
        Label(self.frame, text='Enter Number of Buses:   ', font=('Helvetica',12), height=2).grid(row=0, column=0, sticky=E)
        Entry(self.frame, width=20, textvariable=self.entry0).grid(row=0, column=1)
        self.submitButton = Button(self.frame, text='Submit', font=('Helvetica',10), command=lambda: self.resetBus_number(1))
        self.submitButton.grid(row=0, column=2, padx=10)
        self.exitButton = Button(self.frame, text='Exit', font=('Helvetica',12), command=lambda: self.exitCommand())
        self.exitButton.grid(row=11, column=8, ipadx=10, pady=30, sticky=W)
    
    def getBus_number(self):
        try:
            self.NumberOfBusses = int(self.entry0.get())
            if self.NumberOfBusses != 2 and self.NumberOfBusses != 3:
                messagebox.showerror('Error','Number of buses should be either 2 or 3 busses.')
            else:
                self.addLabels()
                self.solveButton = Button(self.frame, text='Solve', font=('Helvetica',12), command=lambda: self.getInput_string())
                self.solveButton.grid(row=11, column=6, ipadx=10, pady=30, sticky=E)
                self.resetButton = Button(self.frame, text='Reset', font=('Helvetica',12), command=lambda: self.resetBus_number())
                self.resetButton.grid(row=11, column=7, ipadx=10, pady=30, sticky=W)
        except ValueError:
            messagebox.showerror('Error','Number of buses should be a numeric value.')
                
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
        self.inputs['Number of buses'] = self.NumberOfBusses
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

def convert_pol2rec(v,ang): # converts user input to rectangular form usable by python
    return v*exp(1j*deg2rad(ang))

def convert_rec2pol(x):     # converts python out to polar form understandable by user
    return (abs(x),rad2deg(angle(x)))
def polar(z):
    p=abs(z)
    d=(math.atan(z.imag/z.real))*180/math.pi
    return(p,d)


def Y_bus(n,line_parameter, Line1_2 = None, Line1_3=None,Line2_3 = None):   #n is 2 or 3 for this project - accepts line details and forms Ybus
    Y_Z = line_parameter  
    if n == 2:
        L12 = Line1_2
        if Y_Z == 0:
            Y = L12
        elif Y_Z == 1:
            Y = 1/L12
        Y11 = Y22 = Y
        Y12 = Y21 = -Y
        Ybus = array([[Y11,Y12],[Y21,Y22]])
    
    if n == 3:
        Y_Z = line_parameter
        L12 = Line1_2
        L13 = Line1_3
        L23 = Line2_3
        if Y_Z == 0:
            Y1_2 = L12
            Y1_3 = L13
            Y2_3 = L23
        elif Y_Z == 1:
            Y1_2 = 1/L12
            Y1_3 = 1/L13
            Y2_3 = 1/L23
    
        Y11 = Y1_2 + Y1_3
        Y12 = Y21 = -Y1_2
        Y13 = Y31 = -Y1_3
        Y22 = Y1_2 + Y2_3
        Y23 = Y32 = -Y2_3
        Y33 = Y1_3 + Y2_3
        Ybus = array([[Y11,Y12,Y13],[Y21,Y22,Y23],[Y31,Y32,Y33]])
    return Ybus
    
def main():
    print(midFrame.inputs)
    
    
    no_of_bus = midFrame.inputs['Number of buses']
    solver = midFrame.inputs['Analysis Method']
    line_parameter = midFrame.inputs['Line Parameter']
    
    if midFrame.inputs['Bus 1'] == 1:
        v1 = convert_pol2rec(midFrame.inputs['Voltage Magnitude of Slack'],midFrame.inputs['Voltage Angle of Slack']) 
    if midFrame.inputs['Bus 2'] == 2: 
        B2 = (-(midFrame.inputs['Real Power of Load']),-(midFrame.inputs['Reactive Power of Load']))
      #no input fr bus 3 as load bus, should be unique compared to bus2
        
    # converts the user
    
    
    error1 = error2 = 0.1
    iterations = 0
    if solver == 2:
        if no_of_bus == 2:
            Line1_2 = midFrame.inputs['Line 1-2']
            Y = Y_bus(no_of_bus,line_parameter,Line1_2)         # this has to be n
            v2 = 1+0j               #flat start
            while error1 > 0.005 and error2 > 0.05:
                volts = array([[v1],[v2]])
                (Vm,Vang) = (abs(volts),angle(volts))
                (Ym,Yang) =(abs(Y),angle(Y))
                # for a two bus sytem
                i = 1
                Pcal = Qcal = 0
                for j in range(0,i+1):
                    Pcal +=  Vm[i]*Vm[j]*Ym[i,j]*math.cos(Yang[i,j]+Vang[j]-Vang[i])
                    Qcal -=  Vm[i]*Vm[j]*Ym[i,j]*math.sin(Yang[i,j]+Vang[j]-Vang[i])
                Pcal = round((Pcal.tolist()[0]),4)
                Qcal = round((Qcal.tolist()[0]),4)
    
                delta_P = B2[0] - Pcal
                delta_Q = B2[1] - Qcal
                MM = matrix([[delta_P],[delta_Q]])     #mismatchvector
    
                # forming the Jacobian matrix
                # demo for two buses. Bus MUST be slack and Bus 2 load
                j = 0
                J11 = dp_delta = (Vm[i]*Vm[j]*Ym[i,j]*math.sin(Yang[i,j]+Vang[j]-Vang[i]))[0]
                J12 = dp_dV = (Vm[j]*Ym[i,j]*math.cos(Yang[i,j]+Vang[j]-Vang[i]) + 2*Vm[i]*Ym[i,i]*math.cos(Yang[i,i]))[0]
                J21 = dQ_delta = (Vm[i]*Vm[j]*Ym[i,j]*math.cos(Yang[i,j]+Vang[j]-Vang[i]) - Vm[i]*Vm[i]*Ym[i,i]*math.cos(Yang[i,i]))[0]
                J22 = dQ_dV = (-Vm[i]*Ym[i,j]*math.sin(Yang[i,j]+Vang[j]-Vang[i]) - 2*Vm[i]*Ym[i,i]*math.sin(Yang[i,i]))[0]
    
                Jbus = array([[J11,J12],[J21,J22]])         # Jacobian matrix
                Jmat = np.asmatrix(Jbus)
                Inv_Jmat = Jmat.I                           # inverse of the J matrix
                deltas = np.asarray(Inv_Jmat * MM) 
                delta_ang = deltas[0][0]
                delta_V = deltas[1][0]
                new_delta = math.degrees(Vang[1] + delta_ang)
                new_V = Vm[1][0] + delta_V
                error1 = abs(new_V - Vm[1])
                error2 = abs(new_delta - Vang[1])
                v2= convert_pol2rec(new_V,new_delta)         # angle has to be in degrees 
                iterations += 1  
                if iterations > 50:
                    print('BLACKOUT!')
                    break
                else:
                    pass
            Answer = 'System Voltage Profile \n-------------------------' +'\nBus 1 (Slack): ' + str(convert_rec2pol(v1)) + '\nBus 2 (Load): |V| ' + str(round(new_V,4)) + ' <angle: '+str(round(new_delta,4)) + '\nNo of iterations: '+str(iterations)
   
        elif no_of_bus == 3:
            PV = 0      # initalise condition to distinguisg laod bus and PV bus
            if midFrame.inputs['Bus 3'] == 3:
                B3 = (midFrame.inputs['Real Power of Generator'],midFrame.inputs['Voltage Magnitude of Generator'])
                v2 = 1+0j
                v3 = convert_pol2rec(B3[1],0)
            elif midFrame.inputs['Bus 3'] == 2:
                PV = 1      # Bus is a PQ bus
                v2 = v3 = 1+0j   #flat start
                B3 = (midFrame.inputs['Real Power of Load'],midFrame.inputs['Reactive Power of Load']) 
            Line1_2 = midFrame.inputs['Line 1-2']
            Line1_3 = midFrame.inputs['Line 1-3']
            Line2_3 = midFrame.inputs['Line 2-3']
        
            Y = Y_bus(no_of_bus,line_parameter,Line1_2,Line1_3,Line2_3)    # Admittance matrix of the system
            error1 = error2 = error3 = 0.1
            iterations = 0
            while error1 > 0.005 and error2 > 0.05:
                volts = array([[v1],[v2],[v3]])
                (Vm,Vang) = (abs(volts),angle(volts))
                (Ym,Yang) =(abs(Y),angle(Y))
         
                i = 1
                P2cal = Q2cal = P3cal = Q3cal = 0
                for j in range(0,i+2):
                    P2cal +=  Vm[i]*Vm[j]*Ym[i,j]*math.cos(Yang[i,j]+Vang[j]-Vang[i])
                    Q2cal -=  Vm[i]*Vm[j]*Ym[i,j]*math.sin(Yang[i,j]+Vang[j]-Vang[i])
                    P3cal +=  Vm[i+1]*Vm[j]*Ym[i+1,j]*math.cos(Yang[i+1,j]+Vang[j]-Vang[i+1])
                    if PV == 1:
                        Q3cal -= Vm[i+1]*Vm[j]*Ym[i+1,j]*math.sin(Yang[i+1,j]+Vang[j]-Vang[i+1]) 
                P2cal = round((P2cal.tolist()[0]),4)
                Q2cal = round((Q2cal.tolist()[0]),4)
                P3cal = round((P3cal.tolist()[0]),4)
                if PV == 1:
                    Q3cal = round((Q3cal.tolist()[0]),4)
                    delta_P3 = B3[0] - P3cal
                else:
                    delta_P3 = B3[0] - P3cal
            
                delta_P2 = B2[0] - P2cal
                delta_Q2 = B2[1] - Q2cal
            
                if PV == 1:
                    delta_Q3 = B3[1] - Q3cal
                    MM = matrix([[delta_P2],[delta_Q2],[delta_P3],[delta_Q3]])
                else:
                    MM = matrix([[delta_P2],[delta_Q2],[delta_P3]])
                j = 0
                k =2
                # jacobian matrix 
                J11 = dp2_delta2 = (Vm[i]*Vm[j]*Ym[i,j]*math.sin(Yang[i,j]+Vang[j]-Vang[i]) + Vm[i]*Vm[k]*Ym[i,k]*math.sin(Yang[i,k]+Vang[k]-Vang[i]))[0]
                J12 = dp2_dV = (Vm[j]*Ym[i,j]*math.cos(Yang[i,j]+Vang[j]-Vang[i]) + 2*Vm[i]*Ym[i,i]*math.cos(Yang[i,i]) + Vm[k]*Ym[i,k]*math.cos(Yang[i,k]+Vang[k]-Vang[i]))[0]
                J13 = dp2_delta3 = (-Vm[i]*Vm[k]*Ym[i,k]*math.sin(Yang[i,k]+Vang[k]-Vang[i]))[0]
                J21 = dQ_delta2 = (Vm[i]*Vm[j]*Ym[i,j]*math.cos(Yang[i,j]+Vang[j]-Vang[i]) - Vm[i]*Vm[i]*Ym[i,i]*math.cos(Yang[i,i]) + Vm[i]*Vm[k]*Ym[i,k]*math.cos(Yang[i,k]+Vang[k]-Vang[i]))[0]
                J22 = dQ_dV = (-Vm[i]*Ym[i,j]*math.sin(Yang[i,j]+Vang[j]-Vang[i]) - 2*Vm[i]*Ym[i,i]*math.sin(Yang[i,i]) - Vm[k]*Ym[i,k]*math.sin(Yang[i,k]+Vang[k]-Vang[i]))[0]
                J23 = dQ_delta3 = (-Vm[i]*Vm[k]*Ym[i,k]*math.cos(Yang[i,k]+Vang[k]-Vang[i]))[0]
                J31 = dp3_delta2 = (-Vm[k]*Vm[i]*Ym[k,i]*math.sin(Yang[k,i]+Vang[i]-Vang[k]))[0]
                J32 = dp3_dV = (Vm[k]*Ym[k,i]*math.cos(Yang[k,i]+Vang[i]-Vang[k]))[0]
                J33 = dp3_delta3 = (Vm[k]*Vm[j]*Ym[k,j]*math.sin(Yang[k,j]+Vang[j]-Vang[k]) + Vm[k]*Vm[i]*Ym[k,i]*math.sin(Yang[k,i]+Vang[i]-Vang[k]))[0]
            
                if PV ==1 :
                    J14 = (Vm[i]*Ym[i,k]*math.cos(Yang[i,k]+Vang[k]-Vang[i]))[0]
                    J24 = (-Vm[i]*Ym[i,k]*math.sin(Yang[i,k]+Vang[k]-Vang[i]))[0]
                    J34 = (Vm[j]*Ym[k,j]*math.cos(Yang[k,j]+Vang[j]-Vang[k]) + Vm[i]*Ym[k,i]*math.cos(Yang[k,i]+Vang[i]-Vang[k]) + 2*Vm[k]*Ym[k,k]*math.cos(Yang[k,k]))[0]
                    J41 = (-Vm[k]*Vm[i]*Ym[k,i]*math.cos(Yang[k,i]+Vang[i]-Vang[k]))[0]
                    J42 = (-Vm[k]*Ym[k,i]*math.sin(Yang[k,i]+Vang[i]-Vang[k]))[0]
                    J43 = (Vm[k]*Vm[j]*Ym[k,j]*math.cos(Yang[k,j]+Vang[j]-Vang[k]) + Vm[k]*Vm[i]*Ym[k,i]*math.cos(Yang[k,i]+Vang[i]-Vang[k]))[0]
                    J44 = (-Vm[j]*Ym[k,j]*math.sin(Yang[k,j]+Vang[j]-Vang[k]) - Vm[i]*Ym[k,i]*math.sin(Yang[k,i]+Vang[i]-Vang[k]) - 2*Vm[k]*Ym[k,i]*math.sin(Yang[k,k]))[0]
                
                    Jbus = array([[J11,J12,J13,J14],[J21,J22,J23,J24],[J31, J32, J33,J34],[J41,J42,J43,J44]])
                else:
                    Jbus = array([[J11,J12,J13],[J21,J22,J23],[J31, J32, J33]])
        
                Jmat = np.asmatrix(Jbus)
                Inv_Jmat = Jmat.I                           # inverse of the J matrix
                deltas = np.asarray(Inv_Jmat * MM) 
                delta_ang2 = deltas[0][0]
                delta_V2 = deltas[1][0]
                delta_ang3 = deltas[2][0]
                if PV == 1:
                    delta_V3 = deltas[3][0]
                    new_V3 = Vm[2][0] + delta_V3
                new_delta2 = math.degrees(Vang[1] + delta_ang2)
                new_delta3 = math.degrees(Vang[2] + delta_ang3)
                new_V2 = Vm[1][0] + delta_V2
                error1 = abs(new_V2 - Vm[1])
                error2 = abs(new_delta2 - Vang[1])
                error3 = abs(new_delta3 - Vang[2])
                v2= convert_pol2rec(new_V2,new_delta2)
                if PV == 1:
                    v3 = convert_pol2rec(new_V3,new_delta3) 
                else:
                    v3 = convert_pol2rec(B3[1],new_delta3)
                iterations += 1
                if iterations > 50:
                    print('BLACK OUT!')
                    break
                else:
                    pass
            if PV == 1:
                Answer = (P2cal,Q2cal,P3cal,Q3cal)
            else:
                Answer = 'System Voltage Profile\n-------------------------' + '\nBus 1 (slack): ' +str(convert_rec2pol(v1))+ '\nBus 2 (Load): |V| : '+ str(round(new_V2,4)) + ', <angle: '+str(round(new_delta2,4)) + '\nBus 3 (Gen bus): |V|: ' +str(B3[1]) +' <angle '+str(round(new_delta3,4))+'\nNo of iterations: '+str(iterations)
        
        
    elif solver == 1:     # Gauss seidel method selected
        if no_of_bus == 2:
            Line1_2 = midFrame.inputs['Line 1-2']
            Y = Y_bus(no_of_bus,line_parameter,Line1_2)   
            S=complex(B2[0],-B2[1])
            v2=1+0j
            error=0.1
            iteration=0
            while error>0.005:
                v2_old=polar(v2)
                v2_new=1/Y[1][1]*((S/v2.conjugate())-(Y[1][0]*v1))
                V2=polar(v2_new)    
                error=abs(V2[0]-v2_old[0])
                v2=v2_new
                iteration+=1
                if iteration > 50:
                    print('BLACK OUT!')
                    break
                else:
                    pass
            Answer = 'System Voltage Profile\n-------------------------'+'\nBus 1(Slack):' +str(convert_rec2pol(v1)) +'\nBus 2(Load): |V| '+ str(round(V2[0],4)) +'<angle '+ str(round(V2[1],4))+'\nNo of iterations:' +str(iteration)
        
        if no_of_bus == 3:
            if midFrame.inputs['Bus 3'] == 3:
                B3 = (midFrame.inputs['Real Power of Generator'],midFrame.inputs['Voltage Magnitude of Generator'])
                v2 = 1+0j
                v3 = convert_pol2rec(B3[1],0)
            elif midFrame.inputs['Bus 3'] == 2:
                PV = 1      # Bus is a PQ bus
                v2 = v3 = 1+0j   #flat start
                B3 = (midFrame.inputs['Real Power of Load'],midFrame.inputs['Reactive Power of Load']) 
            Line1_2 = midFrame.inputs['Line 1-2']
            Line1_3 = midFrame.inputs['Line 1-3']
            Line2_3 = midFrame.inputs['Line 2-3']
        
            Y = Y_bus(no_of_bus,line_parameter,Line1_2,Line1_3,Line2_3)    # Admittance matrix of the system
            
            error1=error2=0.1
            iteration=0
            
            if midFrame.inputs['Bus 2'] == 2 and midFrame.inputs['Bus 3'] == 2:
                PV=1
                v2=1+0j
                v3=1+0j
                S2=complex(B2[0],-B2[1])
                S3=complex(B3[0],-B3[1])
                while error1>0.005 and error2>0.005:
                    v2_old=polar(v2)
                    v3_old=polar(v3)
                    v2_new=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1)-(Y[1][2]*v3))
                    v3_new=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*v1)-(Y[1][2]*v2_new))
                    V2=polar(v2_new)
                    V3=polar(v3_new)
                    error1=abs(V2[0]-v2_old[0])
                    error2=abs(V3[1]-v3_old[0])
                    v2=v2_new
                    v3=v3_new
                    iteration += 1  
                    if iteration > 50:
                        print('BLACKOUT!')
                        break
                    else:
                        pass
                Answer = 'System Voltage Profile \n-------------------------' +'\nBus 1 (Slack): ' + str(convert_rec2pol(v1)) + '\nBus 2 (Load): |V| ' + str(round(V2[0],4)) + ' <angle: '+str(round(V2[1],4))+ '\nBus 3 (Load): |V| ' + str(round(V3[0],4)) + ' <angle: '+str(round(V3[1],4)) + '\nNo of iterations: '+str(iteration)
                
            if midFrame.inputs['Bus 2'] == 2 and midFrame.inputs['Bus 3'] == 3:
                #PV=1
                v2 = 1+0j   #flat start
                S2=complex(B2[0],-B2[1])
                p3=B3[0]
                vol3=B3[1]
                v3=complex(vol3,0)
                #error1=error2=0.1
                #iteration=0
                while error1>0.005 and error2>0.005:
                     v2_old=polar(v2)
                     v3_old=polar(v3)
                     reactive3=-(((Y[2][2]*v3)+(Y[2][0]*v1)+(Y[2][1]*v2))*v3.conjugate())
                     q3=reactive3.imag
                     if q3 < -0.4:
                         S3=complex(p3,0.4)
                         v2_new=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1)-(Y[1][2]*v3))
                         V2=polar(v2_new)
                         v3_new=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*v1)-(Y[1][2]*v2_new))
                         V3=polar(v3_new)
                         error1=abs(V2[0]-v2_old[0])
                         error2=abs(V3[0]-v3_old[0])
                         #z=convert_pol2rec(vol3,V3[1])
                         V3_limit=V3
                         v2=v2_new
                         v3=v3_new
                         iteration+=1
                         if iteration > 50:
                             print('BLACKOUT!')
                             break
                         else:
                             pass
                         #Answer = 'System Voltage Profile \n-------------------------' +'\nBus 1 (Slack): ' + str(convert_rec2pol(v1)) + '\nBus 2 (Load): |V| ' + str(round(V2[0],4)) + ' <angle: '+str(round(V2[1],4))+ '\nBus 3 (Generator): |V| ' + str(round(V3[0],4)) + ' <angle: '+str(round(V3[1],4)) + '\nNo of iterations: '+str(iteration)
                     elif q3 > 0.7:
                        S3=complex(p3,-0.7)
                        v2_new=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1)-(Y[1][2]*v3))
                        V2=polar(v2_new)
                        v3_new=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*v1)-(Y[1][2]*v2_new))
                        V3=polar(v3_new)
                        error1=abs(V2[0]-v2_old[0])
                        error2=abs(V3[0]-v3_old[0])
                        #z=convert_pol2rec(V3[0],V3[1])
                        V3_limit=V3
                        v2=v2_new
                        v3=v3_new
                        iteration+=1
                        if iteration > 50:
                            print('BLACKOUT!')
                            break
                        else:
                            pass
                        #Answer = 'System Voltage Profile \n-------------------------' +'\nBus 1 (Slack): ' + str(convert_rec2pol(v1)) + '\nBus 2 (Load): |V| ' + str(round(V2[0],4)) + ' <angle: '+str(round(V2[1],4))+ '\nBus 3 (Generator): |V| ' + str(round(V3[0],4)) + ' <angle: '+str(round(V3[1],4)) + '\nNo of iterations: '+str(iteration)
                     elif -0.4<q3<0.7:
                        S3=complex(p3,-q3)
                        v2_new=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1)-(Y[1][2]*v3))
                        V2=polar(v2_new)
                        v3_new=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*v1)-(Y[1][2]*v2_new))
                        V3=polar(v3_new)
                        error1=abs(V2[0]-v2_old[0])
                        error2=abs(vol3-v3_old[0])
                        #v3_updated=complex(vol3,v3_new.imag)
                        #z=convert_pol2rec(vol3,V3[1])
                        V3_limit=(vol3,V3[1])
                        v2=v2_new
                        v3=convert_pol2rec(vol3,V3[1])
                        iteration+=1
                        if iteration > 50:
                            print('BLACKOUT!')
                            break
                        else:
                            pass
                Answer = 'System Voltage Profile \n-------------------------' +'\nBus 1 (Slack): ' + str(convert_rec2pol(v1)) + '\nBus 2 (Load): |V| ' + str(round(V2[0],4)) + ' <angle: '+str(round(V2[1],4))+ '\nBus 3 (Generator): |V| ' + str(round(V3_limit[0],4)) + ' <angle: '+str(round(V3_limit[1],4)) + '\nNo of iterations: '+str(iteration) 
                                    
    botFrame.result.set(Answer)
    print(botFrame)

root = Tk();
root.title('Power System Simulator')
root.geometry('1220x850')
topFrame = myFrame(root, 'TOP')
midFrame = myFrame(root, 'MID')
botFrame = myFrame(root, 'BOT')
root.mainloop()