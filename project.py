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

def convert_rec2pol(x):     # converts python out to polar form understandable by user
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
    # INCLUDE SIGNATURES TO DIFFERENTIATE BUSES
    
    
    if Bus == 1:
        print('Bus has been selected the slack bus')
        v1 = float(input('Enter the bus voltage magnitude: '))
        ang1 = float(input('Enter the bus voltage angle: '))
        B1 = convert_pol2rec(v1,ang1)    # converts the user input to a form that is understandable
        return (B1,1)       # the number 1 helps to identify the bus type when utilising
    
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
    

def NP():       #TO BE DONE: AUTOMATICALLY ASSIGN BUS BASED ON IMPUT
    '''
    This function solves the newton raphson load flow analysis but it is not a dynamic code
    thus inputs must be given as expected.
    Bus1  must be the slack bus and bus 2 the load bus
    '''
    
    no_of_bus = int(input('Enter the number of buses in this system: '))
    error1 = error2 = 0.1
    iterations = 0
    if no_of_bus == 2:
        A =  accept_input()     # slack (complex number of voltage)
        if A[-1] == 1:
            v1 = (A[0])
        elif A[-1] == 2:
            B2 = (A[0],A[1])
        B = accept_input()     # load bus (Pspec,Qspec)
        if B[-1] == 1:
            v1 = (B[0])
        elif B[-1] == 2:
            B2 = (B[0],B[1])
    
        Y = Y_bus(no_of_bus)            # this has to be n
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
        return 'Voltage at Load Bus' + '\n-------------------------' +'\nVoltage mag: '+ str(round(new_V,4)) + '\nVoltage angle: '+str(round(new_delta,4)) + ' No of iterations: '+str(iterations)
   
    elif no_of_bus == 3:
        '''
        The input function are such that it allows any bus number to be any type of bus
        by including a signature element for each bus type and assigning the value as required
        '''
        
        A = accept_input()     # 1st bus input
        if A[-1] == 1:
            v1 = (A[0])
        elif A[-1] == 2:
            B2 = (A[0],A[1])
        elif A[-1] == 3:
            B3 = (A[0],A[1])
        B = accept_input()     # 2nd bus input
        if B[-1] == 1:
            v1 = (B[0])
        elif B[-1] == 2:
            B2 = (B[0],B[1])
            B22 = B2        # when used for two load buses
        elif B[-1] == 3:
            B3 = (B[0],B[1])
        C = accept_input()  # third bus input
        if C[-1] == 1:
            v1 = (C[0])
        elif C[-1] == 2:
            B2 = (C[0],C[1])
            B23 = B2            # when used for two load buses
        elif C[-1] == 3:
            B3 = (C[0],C[1])
        
        Y = Y_bus(no_of_bus)    # Admittance matrix of the system
        #flat start
        PV = 0
        if A[-1] == B[-1] == 2 or C[-1] == A[-1] == 2 or B[-1] == C[-1] == 2:
            PV = 1          # Two load buses present
            v2 = v3 = 1+0j
        else:
            v2 = 1+0j
            v3 = convert_pol2rec(B3[1],0)
        error1 = error2 = error3 = 0.1
        iterations = 0
        for l in range(1):
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
                delta_P3 = B23[0] - P3cal
            else:
                delta_P3 = B3[0] - P3cal
            
            delta_P2 = B22[0] - P2cal
            delta_Q2 = B22[1] - Q2cal
            
            if PV == 1:
                delta_Q3 = B23[1] - Q3cal
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
            return (P2cal,Q2cal,P3cal,Q3cal)
        else:
            return 'Load bus: voltage mag: '+ str(round(new_V2,4)) + ', voltage angle: '+str(round(new_delta2,4)) + ' Gen bus: voltage mag: ' +str(B3[1]) +' Voltage angle '+str(round(new_delta3,4))+' No of iterations: '+str(iterations)
        
        
def Gauss_Seidel():
        n=int(input("Enter the number of buses: "))
        if n==2:
            A =  accept_input()     # slack (complex number of voltage)
            if A[-1] == 1:
                V1 = (A[0])
            elif A[-1] == 2:
                B2 = (A[0],A[1])
            B = accept_input()     # load bus (Pspec,Qspec)
            if B[-1] == 1:
                V1 = (B[0])
            elif B[-1] == 2:
                B2 = (B[0],B[1])
                
            S=complex(B2[0],-B2[1])
            Y=Y_bus(n)
            v2=1+0j
            error=0.1
            iteration=0
            while error>0.005:
                v2_old=polar(v2)
                v2_new=1/Y[1][1]*((S/v2.conjugate())-(Y[1][0]*V1))
                V2=polar(v2_new)    
                error=abs(V2[0]-v2_old[0])
                v2=v2_new
                iteration+=1
                if iteration > 50:
                    print('BLACK OUT!')
                    break
                else:
                    pass
            return 'voltage:' +str(V2)+' '+'iter:' +str(iteration)
        elif n==3:
            A = accept_input()     # 1st bus input
            if A[-1] == 1:
                V1 = (A[0])
            elif A[-1] == 2:
                B2 = (A[0],A[1])
            elif A[-1] == 3:
                B3 = (A[0],A[1])
            B = accept_input()     # 2nd bus input
            if B[-1] == 1:
                V1 = (B[0])
            elif B[-1] == 2:
                B2 = (B[0],B[1])
            elif B[-1] == 3:
                B3 = (B[0],B[1])
            C = accept_input()  # third bus input
            if C[-1] == 1:
                V1 = (C[0])
            elif C[-1] == 2:
                B2 = (C[0],C[1])
            elif C[-1] == 3:
                B3 = (C[0],C[1])
            p3=C[0]
            vol3=C[1]
            v3=complex(vol3,0)
            S2=complex(B2[0],-B2[1])
            Y=Y_bus(n)
            v2=1+0j
            error1=error2=0.1
            iteration=0
            for l in range(1):
                v2_old=polar(v2)
                v3_old=polar(v3)
                reactive3=-(((Y[1][1]*v2.real)+(Y[1][0]*V1.real)+(Y[1][2]*v3.real))*v2.conjugate())
                q3=reactive3.imag
                if q3 < -0.4:
                    S3=complex(p3,0.4)
                elif q3 > 0.7:
                    S3=complex(p3,-0.7)
                else:
                    S3=complex(p3,q3)
                #v3_old=polar(v3)
                v2_new=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*V1)-(Y[1][2]*v3))
                V2=polar(v2_new)
                v3_new=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*V1)-(Y[1][2]*v2_new))
                V3=polar(v3_new)
                error1=abs(V2[0]-v2_old[0])
                error2=abs(V3[0]-v3_old[0])
                v2=v2_new
                v3=v3_new
                iteration+=1
                if iteration > 50:
                    print('BLACK OUT!')
                    break
                else:
                    pass
            return 'voltage at bus 2:' +str(V2)+' '+'voltage at bus 3:' +str(V3)+' '+'iter:' +str(iteration)


def System_Run():
    method ={}
    method[1] = 'Gauss seidel'
    method[2] = 'Newton Raphson'
    method[3] = 'Exit'
    print('WELCOME TO POWER SYTSEM ANALYSIS - LOAD FLOW')
    print(method)
    method = int(input('Select load flow analysis method: '))
    if method == 1:
        print(" GAUSS SEIDEL's METHOD SELECTED")
        print(Gauss_Seidel())
    elif method == 2:
        print("NEWTON RAPHSON's METHOD SELECTED")
        print(NP())
    else:
        pass
System_Run()
'''    
class run():
    def __init__(self,name = None):
        self.name = name
        
    def printLine (text = ''):
        print('X {: ^47} X'.format(text))

    def printSelTitle (text = '', title = None):
        print('X{: ^9}'.format(text), end = ""),

    def printSelCheck (text = '', title = None):
        print('X   [ ]   '.format(text), end = "")

    def printBorder (title = None):
        print('X' * 51)

    def printBox (*lines, title = None, showBottomBorder = False):
        run.printBorder(title)
        printLine()
        for line in lines:
            printLine(line)
        printLine()
        if showBottomBorder:
            printBorder()

    printBox('POWER SYSTEMS ANALYSIS - LOAD FLOW')
    printBox('READY TO START?', '-' * 21, "PRESS THE 'ENTER'",\
         'KEY TO BEGIN!', '-' * 21, showBottomBorder = True)
    printSelTitle('TASK1'), printSelTitle('TASK2'),\
        printSelTitle('TASK3'), printSelTitle('TASK4'),\
        printSelTitle('TASK5'), print("X")
    printSelCheck(), printSelCheck(), printSelCheck(),\
                 printSelCheck(), printSelCheck(), print("X")
    printBorder() 
    
'''        
        
    
    