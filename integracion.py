from math import *
from scipy import integrate as int
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
mp.rcParams['xtick.labelsize']=13
mp.rcParams['ytick.labelsize']=13


dat=numpy.loadtxt('sol2.txt')  #se leen los datos

lon=dat[:,0]
flu=dat[:,1]

l=len(lon)

da=numpy.zeros(l-1)   #vector que contiene el area acumulada de los trapecios
da[0]=((flu[0]+flu[1])/2)*(lon[1]-lon[0])

for i in range(len(da)-1):    #metodo de los trapecios
    da[i+1]=da[i]+((flu[i+2]+flu[i+1])/2)*(lon[i+2]-lon[i+1])

i=da[l-2]    #valor de la integral

ua=149597870700  #UA
p=i*4*pi*numpy.power(1.496e11,2)  #Potencia (luminosidad)


print i
print p

#integracion mediante trapz

result=int.trapz(flu, lon)

print result
    


