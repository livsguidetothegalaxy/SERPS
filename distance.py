#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
import subprocess as sb
import shlex 

#code for distance to your pulsar, as well as plots for the xy and xz distances

#To loop through all pulsars
#with open("JName", "r") as myfile:
     #name = myfile.readlines()
     #names = [x.rstrip() for x in name]
     #for name in names:
         # j = name
         # print j

j = raw_input( "Please enter J name of your pulsar.") 
#gives the distance to the pulsar 

from math import sqrt 

#finds values for x,y, and z values from PSRCat for each pulsar, splits each value into a list, and then strips any whitespace from the list.

distx= 'psrcat -nohead -nonumber -o short -c "XX" %s' %j
distx_list = shlex.split(distx)
x =sb.Popen(distx_list, stdout=sb.PIPE)
out, err = x.communicate()
dist_x = out.splitlines()

dist_x2 = dist_x[0].strip().split()
x = dist_x2[0]

disty= 'psrcat -nohead -nonumber -o short -c "YY" %s' %j
disty_list = shlex.split(disty)
y = sb.Popen(disty_list, stdout=sb.PIPE)
out, err = y.communicate()
dist_y = out.splitlines()

dist_y2= dist_y[0].strip().split()
y = dist_y2[0]

dist_y_plot = []
dist_x_plot = []

for i in xrange(len(dist_x)):
    if dist_y[i].strip()!="," and dist_x[i].strip()!=",":
          dist_y_plot.append(float(dist_y[i]))
          dist_x_plot.append(float(dist_x[i]))


distz='psrcat -nohead -nonumber -o short -c "ZZ" %s' %j
distz_list = shlex.split(distz)
z = sb.Popen(distz_list, stdout=sb.PIPE)
out, err = z.communicate()
dist_z = out.splitlines()

dist_z_plot = []
dist_x_plot2 = []
for i in xrange(len(dist_x)):
    if dist_x[i].strip()!= "," and dist_z[i].strip()!= ",":
          dist_x_plot2.append(float(dist_x[i]))
          dist_z_plot.append(float(dist_z[i]))

dist_z2 = dist_z[0].strip().split()
z =  dist_z2[0] 

xdist = 'psrcat -nohead -nonumber -o short -c "XX"'
xdist_list = shlex.split(xdist)
xd = sb.Popen(xdist_list, stdout=sb.PIPE)
out, err = xd.communicate()
x_dist = out.splitlines()

ydist = 'psrcat -nohead -nonumber -o short -c "YY"'
ydist_list = shlex.split(ydist)
yd = sb.Popen(ydist_list, stdout=sb.PIPE)
out, err = yd.communicate()
y_dist = out.splitlines()

x_dist_plot = []
y_dist_plot = []

for i in xrange(len(x_dist)):
    if x_dist[i].strip()!= "," and y_dist[i].strip()!= ",":
          x_dist_plot.append(float(x_dist[i]))
          y_dist_plot.append(float(y_dist[i]))


zdist = 'psrcat -nohead -nonumber -o short -c "ZZ"'
zdist_list = shlex.split(zdist)
zd = sb.Popen(zdist_list, stdout=sb.PIPE)
out, err = zd.communicate()
z_dist = out.splitlines()

z_dist_plot = []
x_dist_plot2 =[]

for i in xrange(len(x_dist)):
    if x_dist[i].strip()!= "," and y_dist[i].strip()!=",":
       x_dist_plot2.append(float(x_dist[i]))
       z_dist_plot.append(float(z_dist[i])) 
#plots xy values
fig = plt.figure()
fig.suptitle('XY Distance Plot')
plt.xlabel('kpc in the x direction')
plt.ylabel('kpc in the y direction')
others, = plt.plot(x_dist_plot, y_dist_plot, '.', color = "blue", markersize = 1)
blackhole, = plt.plot(0,0, 'o', color = "black", markersize = 5)
sun, = plt.plot(0,8, "x", color = "yellow", markersize = 3)
pulsars, = plt.plot(dist_x_plot, dist_y_plot, '*', color = "red", markersize = 3)
yourpulsar = "%s" %j
plt.legend([blackhole,sun,others,pulsars], ["Galactic Center", "The Sun", "Other Pulsars", yourpulsar])
plt.xlim(-40, 40)
plt.ylim(-40,40)
plt.minorticks_on()
name = "%sxy.png" %j
plt.savefig(name)

# plots xy values
fig = plt.figure()
fig.suptitle('XZ Distance Plot')
plt.xlabel('kpc in the x direction')
plt.ylabel("kpc in the z direction")
other, = plt.plot(x_dist_plot2, z_dist_plot, '.', color = "blue", markersize =1) 
blackholes, = plt.plot(0,0, 'o',color = "black", markersize = 3)
suns, = plt.plot(0,0, "x", color = "yellow", markersize = 3)
pulsarrs, = plt.plot(dist_x_plot2, dist_z_plot, '*', color = "red", markersize = 3)
yourpulsar= "%s" %j
plt.legend([blackholes,suns,other,pulsarrs], ["Galactic Center", "The Sun", "Other Pulsars", yourpulsar])
name = "%sxz.png"%j
plt.savefig(name)


#plots values for pulsars within 10 kpc from earth
if  dist_z_plot < [10] and dist_z_plot > [-10]:
   fig = plt.figure()
   x1, x2, z1, z2 = -10, 10, -10, 10
   plt.xlim(x1, x2)
   plt.ylim(z1, z2)
   fig.suptitle('XZ Distance Plot for distances up to 10 kpc in the z direction')
   plt.xlabel('kpc in the x direction')
   plt.ylabel('kpc in the z direction')
   other, = plt.plot(x_dist_plot2, z_dist_plot, '.', color = "blue", markersize = 1)
   blackholes,= plt.plot(0,0, "o", color = "black", markersize = 5)
   sunss, = plt.plot(0,0, "x", color= "yellow", markersize = 3)
   pulsars, = plt.plot(dist_x_plot2, dist_z_plot, "*", color = "red", markersize = 3)
   yourpulsar = "%s"%j
   plt.legend([blackholes, sunss, other, pulsars], ["Galactic Center", "The Sun", "Other Pulsars", yourpulsar])
   name = "%sxzzoom.png" %j
   plt.savefig(name)

#plots values for pulsars within 3kpc from the sun 

if dist_z_plot < [3] and dist_z_plot > [-3]:
   fig = plt.figure()
   x1, x2, z1, z2 = -3, 3, -3, 3
   plt.xlim(x1, x2)
   plt.ylim(z1, z2)
   fig.suptitle('XZ Distance Plot for distances up to 3 kpc in the z direction')
   plt.xlabel('kpc in the x direction')
   plt.ylabel('kpc in the z direction')
   another, = plt.plot(x_dist_plot2, z_dist_plot, '.', color = "blue", markersize = 1)
   galcenter,= plt.plot(0,0, "o", color = 'Black', markersize = 4)
   thesun, = plt.plot(0,0, "x", color = "yellow", markersize = 2)
   allpulsars, = plt.plot(dist_x_plot2, dist_z_plot, '*', color = 'red', markersize =3 )
   yourpulsar = "%s"%j
   plt.legend([theholes, onesunnyboi, another, thatpulsar], ["Galactic Center", "The Sun", "Other Pulsars", yourpulsar])
   name = "%sxzzoom2.png"%j
   plt.savefig(name)
    

#gives distance from the sun to pulsar

x1 = (float(x))
y1 = (float(y))
z1 = (float(z))
y2 = y1 - 8.5

sun = np.sqrt(x1**2 + y2**2 + z1**2)
distance = 'The distance of pulsar %s is %s kpc in the x direction, %s kpc in the y direction and %s kpc in the z direction. This puts the source roughly %.3f kpc from the sun. ' %(j,x,y2,z, sun)
 
txt = "%sdistance.txt" %j
f = open(txt, 'w')
f.write(distance)
f.close()


