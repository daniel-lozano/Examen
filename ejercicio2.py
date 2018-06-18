# Ejercicio 2 (20 puntos)
# Resuelva la ecuación de advección lineal d_t u + c d_x u = 0. 
# La condición inicial es una función gaussiana centrada en 0.0 y de sigma 0.1.
# La ecuación debe ser resuelta hasta un tiempo final T=0.5 y una velocidad c=-1.0.
# El programa debe hacer una gráfica (adveccion.png) con la condición incial y el resultado final.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
a=10
T=0.5
dt=0.001
N=T/dt
sigma=0.1
c=-1
x=np.linspace(-a,a)
dx=x[1]-x[0]
print(dx)
normal=(1/np.sqrt(2*np.pi*sigma**2))*np.exp((-x**2)/(2*sigma))

f_old=normal.copy()
f_new=np.zeros(len(normal))
D=dt/dx
print(D)
for i in range(int(N)):
    
    for j in range(len(normal)-1):
        
        f_new[j]=f_old[j]*(1-D*( f_old[j+1]-f_old[j] ))
        
    f_old=f_new.copy()
    

plt.plot(x,normal,label="initial")
plt.plot(x,f_new,label="final")
plt.title("adveccion")
plt.legend()
plt.savefig("adveccion.png")