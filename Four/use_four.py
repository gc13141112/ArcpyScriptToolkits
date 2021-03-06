import os
import math
import string
dx=-403.275
dy=178.190
rot_s=-10.300182
k=1.00009495477874
def fourptrans(x0in,y0in,dxin,dyin,rotin,kin):
    rot_rad=rotin/3600./180.*math.pi
    sinr=math.sin(rot_rad)
    cosr=math.cos(rot_rad)
    x=dxin+kin*x0in*cosr-kin*y0in*sinr
    y=dyin+kin*x0in*sinr+kin*y0in*cosr
    return(x,y)

f1=open("bz.txt","r")
f2=open("bz2000out.txt","w")
bz=[]
rdl=f1.readline()
index=1
while(rdl):
    dataline=rdl.split("\t")
    x0=string.atof(dataline[1])
    y0=string.atof(dataline[2])
    x,y=fourptrans(x0,y0,dx,dy,rot_s,k)
    ptl="{0}\t{1:.4f}\t{2:.4f}\t{3:.4f}\t{4:.4f}".format(dataline[0],x0,y0,x,y)
    print ptl
    wtl="{0}\t{1:.4f}\t{2:.4f}\t{3:.4f}\t{4:.4f}\n".format(dataline[0],x0,y0,x,y)
    f2.write(wtl)
    rdl=f1.readline()
    index=index+1
f1.close()
f2.close()
