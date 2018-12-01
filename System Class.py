# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 12:28:16 2018

@author: Mohamed Omer Airaj
"""

import math
import numpy as np
from numpy import *
from numpy import matrix

class system():
    def __init__(self,number_of_buses=None,line_impedance=None,bus_voltage=None,bus_angle=None,real_power=None,reactive_power=None):
        self.number_of_buses=number_of_buses
        self.line_impedance=line_impedance
        self.bus_voltage=bus_voltage
        self.bus_angle=bus_angle
        self.real_power=real_power
        self.reactive_power=reactive_power
    def convert_pol2rec(v,ang): # converts user input to rectangular form usable by python
        return v*exp(1j*deg2rad(ang))
    def convert_rec2pol(x):     # converts python out to rectangular form understandable by user
        return (abs(x),rad2deg(angle(x)))
    def polar(z):
        p=abs(z)
        d=(math.atan(z.imag/z.real))*180/math.pi
        return(p,d)
    def accept_input():  # accepts input for all buses, output should be saved as an that object 'variable'
        Bus_type={}
        Bus_type[1] = 'Slack bus'
        Bus_type[2] = 'Load bus'
        Bus_type[3] = 'Generator bus'
        print(Bus_type)
        Bus = int(input('Enter the Bus type: '))

        if Bus == 1:
            print('Bus has been selected the slack bus')
            v1 = float(input('Enter the bus voltage magnitude: '))
            ang1 = float(input('Enter the bus voltage angle: '))
            B1 = system.convert_pol2rec(v1,ang1)    # converts the user input to a form that is understandable
            return (B1,1)
    
        if Bus == 2:
            print('Bus  has been selected as a load bus')
            Pspec = -(float(input('Enter the real power of load in pu: ')))
            Qspec = -(float(input('Enter the reactive power of load in pu: ')))
            return (Pspec,Qspec,2)
    
        if Bus == 3:
            print('Bus has been selected as a generator bus')
            p1 = float(input('Enter the real power of the generator: '))
            v1 = float(input('Enter the voltage magnitude of the generator: '))
            return (p1,v1,3)
        
    def Y_bus(n):   #n is 2 or 3 for this project - accepts line details and forms Ybus
        parameter_nature = {}
        parameter_nature[1] = ' Impedance = 1'
        parameter_nature[2] = 'Admittance = 0'
        print(parameter_nature)
        ## for each branch, compute the elements of the branch admittance matrix where
        ##
        ##             | Y11  Y12   Y13|
        ##      Ybus = | Y21  Y22  Y23| 
        ##            | Y31  Y32   Y33|   
        ##
        if n == 2:
            Y_Z = int(input('Enter 1 if line parameter is impedance value and 0 if its admittance value: '))
            L12 = complex(input('Enter line parameter: '))
            if Y_Z == 0:
                Y = L12
            elif Y_Z == 1:
                Y = 1/L12
                Y11 = Y22 = Y
                Y12 = Y21 = -Y
                Ybus = array([[Y11,Y12],[Y21,Y22]])
    
        if n == 3:
            Y_Z = int(input('Enter 1 if line parameter is impedance value and 0 if its admittance value: '))
            L12 = complex(input('Enter line 1-2 parameter: '))
            L13 = complex(input('Enter line 1-3 parameter: '))
            L23 = complex(input('Enter line 2-3 parameter: '))
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
    
    def Gauss_Seidel():
        n=int(input("Enter the number of buses: "))
        if n==2:
            B1=V1=system.accept_input()
            B2=system.accept_input()
            S=complex(B2[0],-B2[1])
            Y=system.Y_bus(n)
            v2=1+0j
            error=0.1
            iteration=0
            while error>0.005:
                v2_old=system.polar(v2)
                v2_new=1/Y[1][1]*((S/v2.conjugate())-(Y[1][0]*V1))
                V2=system.polar(v2_new)    
                error=abs(V2[0]-v2_old[0])
                v2=v2_new
                iteration+=1
            return 'voltage:' +str(V2)+' '+'iter:' +str(iteration)
        elif n==3:
            B1=V1=system.accept_input()
            B2=system.accept_input()
            B3=system.accept_input()
            S2=complex(B2[0],-B2[1])
            S3=complex(B3[0],-B3[1])
            Y=system.Y_bus(n)
            v2=1+0j
            v3=1+0j
            error1=error2=0.1
            iteration=0
            while error1>0.005 and error2>0.005:
                v2_old=system.polar(v2)
                v3_old=system.polar(v3)
                v2_new=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*V1)-(Y[1][2]*v3))
                V2=system.polar(v2_new)
                v3_new=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*V1)-(Y[1][2]*v2_new))
                V3=system.polar(v3_new)
                error1=abs(V2[0]-v2_old[0])
                error2=abs(V3[0]-v2_old[0])
                v2=v2_new
                v3=v3_new
                iteration+=1
            return 'voltage at bus 2:' +str(V2)+' '+'voltage at bus 3:' +str(V3)+' '+'iter:' +str(iteration)
                