#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
import subprocess as sb
import shlex 

#makes plot for pulsar proper motions 

#the following lines will run through the code for all pulsars 
#with open("JName", "r") as myfile:
      #name = myfile.readlines()
      #names = [x.rstrip() for x in name]
      #for name in names:
           #j = name
           #print j



j = raw_input( "Please enter J name of your pulsar.")

allpl = "psrcat -nohead -nonumber -o short -c 'PML'"
p_l = shlex.split(allpl)
pl = sb.Popen(p_l, stdout=sb.PIPE)
out, err = pl.communicate()
alll = out.splitlines()

allpb = "psrcat -nohead -nonumber -o short -c 'PMB'" 
p_b = shlex.split(allpb)
pb = sb.Popen(p_b, stdout=sb.PIPE)
out, err = pb.communicate()    
allb = out.splitlines()

pmb = []
pml = []

for i in xrange(len(allb)):
    if allb[i].strip()!='*' and alll[i].strip()!='*':
       pmb.append(float(allb[0]))
       pml.append(float(alll[0]))

yourpl = "psrcat -nohead -nonumber -o short -c 'PML' %s" %j
yp_l = shlex.split(yourpl)
ypl = sb.Popen(yp_l, stdout=sb.PIPE)
out, err = ypl.communicate()
yourpml = out.splitlines()


yourpb = "psrcat -nohead -nonumber -o short -c 'PMB' %s" %j
yp_b = shlex.split(yourpb)
ypb = sb.Popen(yp_b, stdout=sb.PIPE)
out, err = ypb.communicate()
yourpmb = out.splitlines()


properb = []
properl = []

for i in xrange(len(yourpmb)):
    if yourpmb[i].strip()!='*' and yourpml[i].strip()!='*':
       properb.append(float(yourpmb[i]))
       properl.append(float(yourpml[i]))
from  matplotlib.patches import Arrow
fig = plt.figure()
proper, = plt.plot(properb, properl,'^', markersize = 5, color = "blue")
totproper, = plt.plot(pmb, pml, '.',markersize = 2, color = "orange" )



fig.suptitle("Proper motion of pulsar in l and b")
plt.xlabel("Proper motion in b (mas/year)")
plt.ylabel("Proper motion in l (mas/year)")
pulsar = "%s coord: (%s, %s)"%(j, properb, properl)
plt.legend([ totproper, proper], ["other pulsars", pulsar])
name = "%spropermotion.png" %j
plt.savefig(name)

