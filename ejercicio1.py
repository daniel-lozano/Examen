# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sol=np.exp(1)-np.exp(0)
N=np.zeros(8)
for i in range(8):
    N[i]=10**(i+1)
    
print(N)
dif_t=np.zeros(len(N))
dif_s=np.zeros(len(N))

for i in range(len(N)):
    x=np.linspace(0,1,N[i])
    
    fx=np.exp(x)
    
    dif_t[i]=sol-0.5*(x[1]-x[0])*(np.sum(fx)*2+fx[0]*fx[-1])
    dif_s[i]=sol-(1/6.0)*(x[1]-x[0])*(np.sum(fx)*2+fx[0]*fx[-1]+4*np.sum(np.exp(0.5*(x[1:-1]+x[0:-2]))))
    
plt.loglog(N,dif_t,label="error trapezoide")
plt.loglog(N,dif_s,label="error simpson")
plt.legend()
plt.savefig("error.png")



