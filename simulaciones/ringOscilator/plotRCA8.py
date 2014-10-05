#!/usr/bin/python
# coding: latin-1
# La segunda línea (# coding: latin-1) es necesaria para poder usar acentos y ñ. Para entender el porqué, visitar:
# http://www.python.org/dev/peps/pep-0263/
from numpy import * 
#import pylab
import matplotlib.pyplot as plt # Primero cargo el resultado de la simulación en un arreglo:
data = genfromtxt('rippleCarry8_10ns.out', unpack=True)
t=data[0]
a0=data[1]
s0=data[2]
s1=data[3]
s2=data[4]
s3=data[5]
s4=data[6]
s5=data[7]
s6=data[8]
s7=data[9]
cout=data[10]
# Defino un 
# http://matplotlib.sourceforge.net/api/figure_api.html#module-matplotlib.figure 

#plt.figure(1)

## Primero grafico la vpulse
#ax1 = plt.subplot(211)
##ax1.set_xscale("log")
#ax1.grid(True)
#plt.title('a[0],s[0]')
#plt.plot(data[0],a0)
#plt.plot(data[0],s0)
##plt.plot(data[0],s1)
##plt.plot(data[0],s2)
##plt.plot(data[0],s3)
##plt.plot(data[0],s4)
##plt.plot(data[0],s5)
##plt.plot(data[0],s6)
##plt.plot(data[0],s7)
##plt.plot(data[0],cout)
## Luego la fase 
#plt.ylabel('a[1],s[1]')
#ax2 = plt.subplot(212)
##ax2.set_xscale("log")
#ax2.grid(True)
#plt.plot(data[0],s1)
#plt.plot(data[0],s2)
#plt.plot(data[0],s3)
## Le agrego la leyenda en el eje de las abscisas
#plt.xlabel('Tiempo [s]')



###########################
# Nine subplots sharing both x/y axes
f, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(10, sharex=True, sharey=False)

ax1.plot(data[0], data[1])
#ax1.plot(data[0], data[12])
ax1.set_ylabel('a0')


ax1.set_title('Ripple Carry Adder 8 bits')

ax2.plot(data[0], data[2])
ax2.set_ylabel('s0')

ax3.plot(data[0], data[3])
ax3.set_ylabel('s1')

ax4.plot(data[0], data[4])
ax4.set_ylabel('s2')

ax5.plot(data[0], data[5])
ax5.set_ylabel('s3')

ax6.plot(data[0], data[6])
ax6.set_ylabel('s4')

ax7.plot(data[0], data[7])
ax7.set_ylabel('s5')

ax8.plot(data[0], data[8])
ax8.set_ylabel('s6')

ax9.plot(data[0], data[9])
ax9.set_ylabel('s7')

ax10.plot(data[0], data[10])
ax10.set_ylabel('cout')



# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

# Escondo los ticks de todos los ejes Y:
plt.setp([a.get_yticklabels() for a in f.axes[:]], visible=False)

plt.show()



# Con este comando aparece la ventana con los gráficos
plt.show()
#plt.plot(data[0],fase)
#plt.show()
