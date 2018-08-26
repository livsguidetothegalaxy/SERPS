#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
import subprocess as sb
import shlex 


# makes plot of period vs period dirv for all pulsars 

#with open("JName", "r") as myfile:
     #name = myfile.readlines()
     #names = [x.rstrip() for x in name]
     #for name in names:
           #j = name
           #print j

j =raw_input("Pulsar Name:")

periods_cmd = 'psrcat -nohead -nonumber -o short -c "P0"'
periods_cmd_list = shlex.split(periods_cmd)

p = sb.Popen(periods_cmd_list, stdout=sb.PIPE)
out, err = p.communicate()
periods = out.splitlines()

period_derivs_cmd = 'psrcat -nohead -nonumber -o short -c "P1"'
period_derivs_cmd_list = shlex.split(period_derivs_cmd)

p = sb.Popen(period_derivs_cmd_list, stdout=sb.PIPE)

out, err = p.communicate()
period_derivs = out.splitlines()

periods_plot = []
period_derivs_plot = []

for i in xrange(len(periods)):
    if periods[i].strip() != "*" and period_derivs[i].strip() != "*":
        p = float(periods[i])
        pdot = float(period_derivs[i])
        if p > 0 and pdot > 0:
            periods_plot.append(float(periods[i]))
            period_derivs_plot.append(float(period_derivs[i]))

pulsarperiod_cmd = 'psrcat -nohead -nonumber -o short -c "P0" %s' % j 
pulsarperiod_cmd_list = shlex.split(pulsarperiod_cmd)
pp = sb.Popen(pulsarperiod_cmd_list, stdout=sb.PIPE)
out, err = pp.communicate()
pulsar_period = out.splitlines()
    
pulsarperioddir_cmd = 'psrcat -nohead -nonumber -o short -c "P1" %s' %j
pulsarperioddir_cmd_list = shlex.split(pulsarperioddir_cmd)
ppd = sb.Popen(pulsarperioddir_cmd_list, stdout=sb.PIPE)
out, err = ppd.communicate()
pulsar_perioddir = out.splitlines()
    
pulsarperiod_plot = []
pulsarperioddir_plot = []

for i in xrange(len(pulsar_period)):
    if pulsar_period[i].strip() != "*" and pulsar_perioddir[i].strip() != "*":
        p = float(pulsar_period[i])
        plot = float(pulsar_perioddir[i])
if p > 0 and pdot > 0:
    pulsarperiod_plot.append(float(pulsar_period[i]))
    pulsarperioddir_plot.append(float(pulsar_perioddir[i]))
 
fig, ax = plt.subplots(1,1)
fig.suptitle('Pulsar Period vs Period Derivative(p vs pdot)')
plt.xlabel('period (s)', fontsize =16)
plt.ylabel('period derivative (s/s)', fontsize=16)
otherspulsars, = plt.plot(periods_plot , np.log10(period_derivs_plot), 'o', color = 'blue', markersize =1)
pulsar, = plt.plot(pulsarperiod_plot, np.log10(pulsarperioddir_plot), '*', color = 'red', markersize=8)
yourpulsar = "%s" %j
xscale = ax.set_xscale('log')

import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter
ax.get_xaxis().set_major_formatter(FormatStrFormatter("%.2f"))
ax.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())

plt.legend([pulsar, otherspulsars], [yourpulsar, "other pulsars"])
name = '%spp0.png'%j

plt.savefig(name)

plt.show()
   
