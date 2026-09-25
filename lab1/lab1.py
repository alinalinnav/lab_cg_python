import numpy as np
from PIL import Image
from math import floor

def line(img_mat,x0,y0,x1,y1):
    dmax=max(abs(floor(x0)-floor(x1)), abs(floor(y0)-floor(y1)))
    L=dmax+1

    if L==1:
        img_mat[floor(y0),floor(x0)]=[0,255,0]
        return

    dx=(x1-x0)/(L-1)
    dy=(y1-y0)/(L-1)

    x=x0
    y=y0
    for i in range(L):
        img_mat[floor(y),floor(x)]=[0,0,255]
        x+=dx
        y+=dy

#line(img_mat,x0,y0,x1,y1)


img_mat=np.zeros((1000,1000,3),dtype=np.uint8)

x0,y0,x1,y1=30.5, 40.1, 500.0, 950.9

file = open('model.obj')

scale=5000

v=[]
f=[]
for s in file:
    spl=s.split()
    if(spl[0]=='v'):
        v.append([float(spl[1]),float(spl[2]),float(spl[3])])
    elif(spl[0]=='f'):
        f.append([spl[1].split('/')[0],spl[2].split('/')[0],spl[3].split('/')[0]])


for i in range(len(v)):
        x=v[i][0]*scale+500
        y=-v[i][1]*scale+500
        img_mat[int(y),int(x)]=[128,0,128]

for i in range(len(f)):
     #f[i]-номера вершин i-полигона
    x0=v[int(f[i][0])-1][0]*scale+500
    y0=-v[int(f[i][0])-1][1]*scale+500
    x1=v[int(f[i][1])-1][0]*scale+500
    y1=-v[int(f[i][1])-1][1]*scale+500
    x2=v[int(f[i][2])-1][0]*scale+500
    y2=-v[int(f[i][2])-1][1]*scale+500

    line(img_mat,x0,y0,x1,y1)
    line(img_mat,x0,y0,x2,y2)
    line(img_mat,x1,y1,x2,y2)


img=Image.fromarray(img_mat)
img.save('img.png')
