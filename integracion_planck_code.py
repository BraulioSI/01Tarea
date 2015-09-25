from math import *
from scipy import integrate as int
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
#mp.rcParams['xtick.labelsize']=13
#mp.rcParams['ytick.labelsize']=13


n=1000                  #numero de intervalos de la particion
dy=pi/(2*n)               #delta de integracion
y=numpy.zeros(n+1)
y[0]=0

for i in range(n):        #se crea el vector dominio entre o y pi/2
    y[i+1]=y[i]+dy     

f=numpy.zeros(n+1)       #vector de imagenes (valores de la funcion)
f[0]=0
f[n]=0

for i in range(n-1):
    f[i+1]=numpy.power(sin(y[i+1]),3)/(numpy.power(cos(y[i+1]),5)*(numpy.exp(tan(y[i+1]))-1))


da=numpy.zeros(n)      #vector que contiene el área acumulada de los trapecios
da[0]=((f[0]+f[1])/2)*dy

for i in range(len(da)-1):
    da[i+1]=da[i]+((f[i+2]+f[i+1])/2)*(dy)



print da[n-1]

h=6.62606957e-34   #constantes
c=3e8
k=1.3806488e-23
t=5778

flujo=(2*pi*h/numpy.power(c,2))*numpy.power(k*t/h,4)*da[n-1]  


#print flujo

#se calcula de nuevo la luminosidad (parte 2)
dat=numpy.loadtxt('sol2.txt')

lon=dat[:,0]
flu=dat[:,1]

l=len(lon)

db=numpy.zeros(l-1)
db[0]=((flu[0]+flu[1])/2)*(lon[1]-lon[0])

for i in range(len(db)-1):
    db[i+1]=db[i]+((flu[i+2]+flu[i+1])/2)*(lon[i+2]-lon[i+1])

j=db[l-2]

ua=1e5
lum=j*4*pi*numpy.power(1.496e11,2)  #luminosidad



r=numpy.power(lum/(4*pi*flujo),0.5)  #radio solar
#print r

#rutina para integrar con quad

def integrand(x):
    return numpy.power(sin(x),3)/(numpy.power(cos(x),5)*(numpy.exp(tan(x))-1))

result=int.quad(integrand, 0, pi/2)

print result

r1=numpy.power(pi,4)/15 - da[n-1]
r2=numpy.power(pi,4)/15 - result

print r1
print r2
