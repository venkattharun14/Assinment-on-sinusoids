import numpy as np 
from matplotlib import pyplot as plt
n=np.arange(1,500)
x=1000
y=100
fs=10000
a=1.5*np.cos(2*np.pi*x/fs*n+np.pi/2)
b=2.5*np.cos(2*np.pi*x/fs*n+np.pi/2)
c=a+b
plt.subplot(321)
plt.plot(n,c,'g')
plt.title('change of amplitude')
d=np.cos(2*np.pi*x/fs*n+np.pi/2)
e=np.cos(2*np.pi*y/fs*n+np.pi/2)
f=d+e
plt.subplot(322)
plt.plot(n,f,'g')
plt.title('change of frequency')
g=np.cos(2*np.pi*x/fs*n+np.pi/4)
h=np.cos(2*np.pi*x/fs*n+np.pi/6)
i=g+h
plt.subplot(323)
plt.plot(n,i,'r')
plt.title('change of phase')
d1=1.5*np.cos(2*np.pi*x/fs*n+np.pi/2)
e1=2.5*np.cos(2*np.pi*x/fs*n+np.pi/2)
f1=d1*e1
plt.subplot(324)
plt.plot(n,f1,'r')
plt.title('multiplication of signals with change in aplitude')
g1=np.cos(2*np.pi*x/fs*n+np.pi/2)
h1=np.cos(2*np.pi*y/fs*n+np.pi/2)
i1=g1*h1
plt.subplot(325)
plt.plot(n,i1,'b')
plt.title('multiplication of signals with change in frequency')
j1=np.cos(2*np.pi*x/fs*n+np.pi/2)
k1=np.cos(2*np.pi*x/fs*n+np.pi/4)
l1=j1*k1
plt.subplot(326)
plt.plot(n,l1)
plt.title('multiplication of signals with change in phace')
plt.show()
