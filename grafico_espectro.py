###############################
#Como leer un cubo de datos
###############################

from math import *
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
mp.rcParams['xtick.labelsize']=13
mp.rcParams['ytick.labelsize']=13


a=numpy.loadtxt('sol.txt')  #se leen los datos

l=a[:,0]*10  #vector longitud de onda

f=a[:,1]*100  #vector flujo


p.plot(l,f)
p.xlabel('Longitud de onda [A]')
p.ylabel('Flujo $[ \\frac{erg}{cm^2A}]$ ', fontsize=15)
p.title('Espectro solar')
p.show()








            
