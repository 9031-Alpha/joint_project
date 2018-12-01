# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:22:45 2018

@author: Mohamed Omer Airaj
"""
#import cmath
import numpy as np
import math
def polar(z):
    p=math.sqrt(z.real**2+z.imag**2)
    d=(math.atan(z.imag/z.real))*180/math.pi
    return(p,d)
def Gauss_Seidel():
    number_of_buses=int(input("Enter the number of buses: "))
    n=int(input("Enter the number of iteration: "))
    if number_of_buses==2:
        a1=float(input("Enter the real part of bus 1-2: "))
        a2=float(input("Enter the imaginary part of bus 1-2: "))
        p1=float(input("Enter the real power for bus 1 in pu: "))
        q1=float(input("Enter the  reactive power for bus 1 in pu: "))
        p2=float(input("Enter the real power for bus 2 in pu: "))
        q2=float(input("Enter the  reactive power for bus 2 in pu: "))
        z12=complex(a1,a2)
        Y=np.array([[1/z12,-(1/z12)],[-(1/z12),1/z12]])
        #Y11=Y22=1/z12
        #Y12=Y21=-(1/z12)
        print("The Y bus matrix is:" +str(Y))
        P2=-p2
        Q2=-q2
        S2=complex(P2,-Q2)
        v1_real=float(input("Enter the real part of voltage at bus 1: "))
        v1_imaginary=float(input("Enter the imaginary part of voltage at bus 1: "))
        v1=complex(v1_real,v1_imaginary)
        v2=complex(1,0)
        for i in range(1,n+1):
            V2=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1))
            v2=V2
        return(polar(V2))
    elif number_of_buses==3:
        a1=float(input("Enter the real part of bus 1-2: "))
        a2=float(input("Enter the imaginary part of bus 1-2: "))
        b1=float(input("Enter the real part of bus 1-3: "))
        b2=float(input("Enter the imaginary part of bus 1-3: "))
        c1=float(input("Enter the real part of bus 2-3: "))
        c2=float(input("Enter the imaginary part of bus 2-3: "))
        p1=float(input("Enter the real power for bus 1 in pu: "))
        q1=float(input("Enter the  reactive power for bus 1 in pu: "))
        p2=float(input("Enter the real power for bus 2 in pu: "))
        q2=float(input("Enter the  reactive power for bus 2 in pu: "))
        p3=float(input("Enter the real power for bus 3 in pu: "))
        q3=float(input("Enter the  reactive power for bus 3 in pu: "))
        z12=complex(a1,a2)
        z13=complex(b1,b2)
        z23=complex(c1,c2)
        Y=np.array([[1/z12+1/z13,-1/z12,-1/z13],[-1/z12,1/z12+1/z23,-1/z23],[-1/z13,-1/z23,1/z13+1/z23]])
        print("The Y bus matrix is:" +str(Y))
        #y12=y21=1/z12        
        #y13=y31=1/z13
        #y23=y32=1/z23
        #Y11=y12+y13
        #Y22=y21+y23
        #Y33=y31+y32
        #Y12=Y21=-y12
        #Y13=Y31=-y13
        #Y23=Y32=-y23
        v1=complex(1.05,0)
        v2=complex(1,0)
        v3=complex(1,0)
        P2=-p2
        Q2=-q2
        S2=complex(P2,-Q2)
        P3=-p3
        Q3=-q3
        S3=complex(P3,-Q3)
        for i in range(1,n+1):
            V2=1/Y[1][1]*((S2/v2.conjugate())-(Y[0][1]*v1)-(Y[1][2]*v3))
            v2=V2
            V3=1/Y[2][2]*((S3/v3.conjugate())-(Y[0][2]*v1)-(Y[1][2]*V2))
            v3=V3
            print(polar(V2))
            print(polar(V3))
        return(V2)
        return(V3)