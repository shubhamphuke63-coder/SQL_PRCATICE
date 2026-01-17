import matplotlib.pyplot as plt 
import numpy as np
x=["python","c","c++","java"]
y=[80,70,60,50]
z=[20,30,40,50]
width=0.4

p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel('languages',color='r',fontsize=15)
plt.ylabel('value',color='r',fontsize=15)
plt.title('SHUBHAM',fontsize=10)

plt.bar(p,y,width,color='g',label='USEAGE',align='center')
plt.bar(p1,z,width,color='r',label='USEAGE',align='center')

plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()



x=["python","c","c++","java"]
y=[80,70,60,50]
z=[20,30,40,50]
width=0.4

p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel('languages',color='r',fontsize=15)
plt.ylabel('value',color='r',fontsize=15)
plt.title('SHUBHAM',fontsize=10)

plt.barh(p,y,width,color='g',label='USEAGE',align='center')
plt.barh(p1,z,width,color='r',label='USEAGE',align='center')

plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()

