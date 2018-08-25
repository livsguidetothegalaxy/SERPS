#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
import subprocess as sb
import shlex 

#This section will plot binary periods vs. minmass

#Following lines take the enteries for the binary periods and minimum companion mass from the PSRCat, split the lines into a list, and then strips any blank space away so each componant can be used as a varible in the plot.
bperiod_cmd = 'psrcat -nohead -nonumber -o short -c "PB"'
bperiod_cmd_list = shlex.split(bperiod_cmd)
bp = sb.Popen(bperiod_cmd_list, stdout=sb.PIPE)
out, err = bp.communicate()
bperiod = out.splitlines()

mas_cmd = 'psrcat -nohead -nonumber -o short -c "MINMASS"'

mas_cmd_list = shlex.split(mas_cmd)
mas = sb.Popen(mas_cmd_list, stdout=sb.PIPE)
out, err = mas.communicate()
massofsystem = out.splitlines()

bperiod_plot = []
mass_of_system_plot = []

for i in xrange(len(bperiod)):
    if bperiod[i].strip()!="*" and massofsystem[i].strip()!="*":
       bp = float(bperiod[i])
       mas = float(massofsystem[i])
       if bp > 0 and mas > 0: 
          bperiod_plot.append(float(bperiod[i])) 
          mass_of_system_plot.append(float(massofsystem[i]))
#Following lines use the J name input by user to create piont on plot for that pulsar.
j = raw_input( "Please enter J name of your pulsar.") 
pulsarbperiod_cmd = 'psrcat -nohead -nonumber -o short -c "PB" %s' %j 
pulsarbperiod_cmd_list = shlex.split(pulsarbperiod_cmd)
pbp = sb.Popen(pulsarbperiod_cmd_list, stdout=sb.PIPE)
out, err = pbp.communicate()
pulsar_bperiod = out.splitlines() 

pulsarmassofsystem_cmd = 'psrcat -nohead -nonumber -o short -c "MINMASS" %s' %j
pulsarmassofsystem_cmd_list = shlex.split(pulsarmassofsystem_cmd)
pmos = sb.Popen(pulsarmassofsystem_cmd_list, stdout=sb.PIPE)
out, err = pmos.communicate()
pulsar_massofsystem = out.splitlines()

pulsarbperiod_plot = []
pulsarmassofsystem_plot = []

for i in xrange(len(pulsar_bperiod)):
    if pulsar_bperiod[i].strip()!="*" and pulsar_massofsystem[i].strip()!="*":
       pbp = float(pulsar_bperiod[i])
       ppmos = float(pulsar_massofsystem[i])
       if pbp > 0 and ppmos > 0:
          pulsarbperiod_plot.append(float(pulsar_bperiod[i]))
          pulsarmassofsystem_plot.append(float(pulsar_massofsystem[i]))          

#plots and lables information 
fig = plt.figure()
fig.suptitle('Binary period vs MinMass')
plt.xlabel('log(Pb)- binary period(Days)')
plt.ylabel('log(MinMass)-MinMass (solar masses)')
plt.ticklabel_format(style='sci', axis ='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis= 'y', scilimits=(0,0))
others, = plt.plot(np.log10(bperiod_plot), np.log10(mass_of_system_plot), 'o', color = 'blue', markersize = 3)
pulsar, = plt.plot(np.log10(pulsarbperiod_plot), np.log10(pulsarmassofsystem_plot), '*', color = 'red', markersize = 5)
yourpulsar= "%s" %j 
plt.legend([others, pulsar],["Other binary pulsars", yourpulsar])
plt.minorticks_on()

name = '%sbinary.png' %j
plt.savefig(name)


    


