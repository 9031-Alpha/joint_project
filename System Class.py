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
            B1 = complex(v1,ang1)    # converts the user input to a form that is understandable
            return (B1)
    
        if Bus == 2:
            print('Bus  has been selected as a load bus')
            Pspec = -(float(input('Enter the real power of load in pu: ')))
            Qspec = -(float(input('Enter the reactive power of load in pu: ')))
            return (Pspec,Qspec)
    
        if Bus == 3:
            print('Bus has been selected as a generator bus')
            p1 = float(input('Enter the real power of the generator: '))
            v1 = float(input('Enter the voltage magnitude of the generator: '))
            return (p1,v1)
        
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
        B1=V1=system.accept_input()
        B2=system.accept_input()
        S=complex(B2[0],-B2[1])
#        v1=system.convert_pol2rec(B1)
        Y=system.Y_bus(2)
        v2=1+0j
        v2_old=system.polar(v2)
        error=0.1
        #error1=error2=0.1
        iteration=0
        while error>0.05:
            i=1
            for j in range(1,i+1):
                v2_new=1/Y[i+1][i+1]*((S/v2.conjugate())-(Y[i+1][j]*V1))
                v2=v2_new
                V2=system.polar(v2_new)
                #error1=abs(V2[0]-v2_old[0])
                #error2=abs(V2[1]-v2_old[0])
                error=abs(V2[0]-v2_old[0])
                v2_updated=complex(V2[0],V2[1])
                iteration+=1
        return 'voltage:' +str(v2_updated)+' '+'iter:' +str(iteration)
        #return 'voltage mag:' + str(V2[0])+' '+'voltage angle:' +str(V2[1])+' '+'No. of iterations:' +str(iteration)
#        P2=-p2
#       Q2=-q2
#        S2=complex(P2,-Q2)
#        v1_real=float(input("Enter the real part of voltage at bus 1: "))
#        v1_imaginary=float(input("Enter the imaginary part of voltage at bus 1: "))
#        v1=complex(v1_real,v1_imaginary)
#        v2=complex(1,0)
#        for i in range(1,n+1):
#            V2=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1))
#            v2=new_v2
#        return(newv2)
#    elif number_of_buses==3:
#        a1=float(input("Enter the real part of bus 1-2: "))
#        a2=float(input("Enter the imaginary part of bus 1-2: "))
#        b1=float(input("Enter the real part of bus 1-3: "))
#        b2=float(input("Enter the imaginary part of bus 1-3: "))
#        c1=float(input("Enter the real part of bus 2-3: "))
#        c2=float(input("Enter the imaginary part of bus 2-3: "))
#        p1=float(input("Enter the real power for bus 1 in pu: "))
#        q1=float(input("Enter the  reactive power for bus 1 in pu: "))
#        p2=float(input("Enter the real power for bus 2 in pu: "))
#        q2=float(input("Enter the  reactive power for bus 2 in pu: "))
#        p3=float(input("Enter the real power for bus 3 in pu: "))
#        q3=float(input("Enter the  reactive power for bus 3 in pu: "))
#        z12=complex(a1,a2)
#        z13=complex(b1,b2)
#        z23=complex(c1,c2)
#        Y=np.array([[1/z12+1/z13,-1/z12,-1/z13],[-1/z12,1/z12+1/z23,-1/z23],[-1/z13,-1/z23,1/z13+1/z23]])
#        print("The Y bus matrix is:" +str(Y))
        #y12=y21=1/z12        
        #y13=y31=1/z13
        #y23=y32=1/z23
        #Y11=y12+y13
        #Y22=y21+y23
        #Y33=y31+y32
        #Y12=Y21=-y12
        #Y13=Y31=-y13
        #Y23=Y32=-y23
#        v1=complex(1.05,0)
#        v2=complex(1,0)
#        v3=complex(1,0)
#        P2=-p2
#        Q2=-q2
#        S2=complex(P2,-Q2)
#        P3=-p3
#        Q3=-q3
#        S3=complex(P3,-Q3)
#        for i in range(1,n+1):
#            V2=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1)-(Y[1][2]*v3))
#            v2=V2
#            V3=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*v1)-(Y[1][2]*V2))
#            v3=V3
#            print(polar(V2))
#            print(polar(V3))
#        return(V2)
#        return(V3)