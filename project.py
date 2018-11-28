# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:43:08 2018

final work is INTEGRATION
"""
# The newton Raphson project
# python solves trignometry using radian 
#x = 2*exp(1j*deg2rad(45)), (abs(x),rad2deg(angle(x)))
#d2r = lambda x: deg2rad(x)
#(m, p) = (abs(volts), r2d(angle(volts)))  recover array of in polar form, for results
#np.asmatrix(a) 

import math
import numpy as np
from numpy import *
from numpy import matrix
from numpy import linalg


def convert_pol2rec(v,ang): # converts user input to rectangular form usable by python
    return v*exp(1j*deg2rad(ang))

def convert_rec2pol(x):     # converts python out to rectangular form understandable by user
    return (abs(x),rad2deg(angle(x)))




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
        B1 = convert_pol2rec(v1,ang1)    # converts the user input to a form that is understandable
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
    

def NP():
    '''
    This function solves the newton raphson load flow analysis but it is not a dynamic code
    thus inputs must be given as expected.
    Bus1  must be the slack bus and bus 2 the load bus
    '''
    
    
    B1 = v1 = accept_input()     # slack (complex number of voltage)
    B2 = accept_input()     # load bus (Pspec,Qspec)
    Y = Y_bus(2)            # this has to be n
    v2 = 1+0j
    error1 = error2 = 0.1
    iteration = 0
    while error1 > 0.005 and error2 > 0.005:
                      #flat start
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
        iteration += 1             
    return 'voltage mag: '+ str(round(new_V,4)) + ' voltage angle: '+str(round(new_delta,4)) + ' No of iterations: '+str(iteration)
    
    
  
    