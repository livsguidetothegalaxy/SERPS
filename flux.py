#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
import subprocess as sb
import shlex 

#to run through code for all pulsars
#with open("JName", "r") as myfile:
    #name = myfile.readlines()
    #names = [x.rstrip() for x in name]
    #for name in names:
         #j = name
         #print j 

j = raw_input( "Please enter J name of your pulsar.") 


#creates flux vs frequency plot for your pulsar

fig = plt.figure() 
flux30 = 'psrcat -nohead -nonumber -o short -c "S30" %s' %j
flux30_list = shlex.split(flux30)
f = sb.Popen(flux30_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_30 = out.splitlines()

flux_30_plot = []
freq30 = []

for i in xrange(len(flux_30)):
    if flux_30[i].strip()!='*':
       f = float(flux_30[i])
       if f > 0:
         flux_30_plot.append(float(flux_30[i]))
         freq30 = 30 
         Thirty = plt.plot(np.log10(flux_30_plot), np.log10(freq30), "^", color = "purple", markersize = 5)   

flux40 = 'psrcat -nohead -nonumber -o short -c "S40" %s' %j
flux40_list = shlex.split(flux40)
f = sb.Popen(flux40_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_40 = out.splitlines()

flux_40_plot = []
freq40 = []
for i in xrange(len(flux_40)):
    if flux_40[i].strip()!='*':
       f = float(flux_40[i])
       if f > 0:
          flux_40_plot.append(float(flux_40[i]))
          freq40 = 40 
          Fourty = plt.plot(np.log10(flux_40_plot), np.log10(freq40), "^", color = "purple", makersize = 5)

flux50 = 'psrcat -nohead -nonumber -o short -c "S50" %s' %j
flux50_list = shlex.split(flux50)
f = sb.Popen(flux50_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_50 = out.splitlines()

flux_50_plot = []
freq50 = []
for i in xrange(len(flux_50)):
    if flux_50[i].strip()!='*':
       f = float(flux_50[i])
       if f > 0:
          flux_50_plot.append(float(flux_50[i]))
          freq50 = 50
          Fifty = plt.plot(np.log10(flux_50_plot), np.log10(freq50), "^", color = "purple", markersize = 5)

flux60 = 'psrcat -nohead -nonumber -o short -c "S60" %s' % j
flux60_list = shlex.split(flux60)
f = sb.Popen(flux60_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_60 = out.splitlines()
flux_60_plot = []
freq60 = []
for i in xrange(len(flux_60)):
    if flux_60[i].strip()!='*':
       f = float(flux_60[i])
       if f > 0:
          flux_60_plot.append(float(flux_60[i]))
          freq60 = 60
          Sixty = plt.plot(np.log10(flux_60_plot), np.log(freq60), "^", color = "purple", markersize = 5)

flux80 = 'psrcat -nohead -nonumber -o short -c "S80" %s' %j
flux80_list = shlex.split(flux80)
f = sb.Popen(flux80_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_80 = out.splitlines()

flux_80_plot = []
freq80 = []
for i in xrange(len(flux_80)):
    if flux_80[i].strip()!='*':
       f = float(flux_80[i])
       if f > 0:
          flux_80_plot.append(float(flux_80[i]))
          freq80 = 80
          Eighty = plt.plot(np.log10(flux_80_plot), np.log10(freq80), "^", color = "purple", markersize = 5)
flux100 = 'psrcat -nohead -nonumber -o short -c "S100" %s' %j
flux100_list = shlex.split(flux100)
f = sb.Popen(flux100_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_100 = out.splitlines()

flux_100_plot = []
freq100 = []
for i in xrange(len(flux_100)):
    if flux_100[i].strip()!='*':
       f = float(flux_100[i])
       if f > 0:
          flux_100_plot.append(float(flux_100[i]))
          freq100 = 100
          hundred = plt.plot(np.log10(flux_100_plot), np.log10(freq100), "^", color = "purple", markersize = 5)

flux150 = 'psrcat -nohead -nonumber -o short -c "S150" %s' %j
flux150_list = shlex.split(flux150)
f = sb.Popen(flux150_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_150 = out.splitlines()

flux_150_plot = []
freq150 = []
for i in xrange(len(flux_150)):
    if flux_150[i].strip()!='*':
       f = float(flux_150[i])
       if f > 0:
          flux_150_plot.append(float(flux_150[i]))
          freq150 = 150
          hundredfifty = plt.plot(np.log10(flux_150_plot), np.log10(freq150), "^", color = "purple", markersize = 5)

flux200 = 'psrcat -nohead -nonumber -o short -c "S200" %s' %j
flux200_list = shlex.split(flux200)
f = sb.Popen(flux200_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_200 = out.splitlines()

flux_200_plot = []
freq200 = []

for i in xrange(len(flux_200)):
    if flux_200[i].strip()!='*':
       f = float(flux_200[i])
       if f > 0:
          flux_200_plot.append(float(flux_200[i]))
          freq200 = 200
          twohundred = plt.plot(np.log10(flux_200_plot), np.log10(freq200), "^", color = "purple", markersize = 5)

flux300 = 'psrcat -nohead -nonumber -o short -c "S300" %s' %j
flux300_list = shlex.split(flux300)
f = sb.Popen(flux300_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_300 = out.splitlines()

flux_300_plot = []
freq300 = []
for i in xrange(len(flux_300)):
    if flux_300[i].strip()!='*':
       f = float(flux_300[i])
       if f > 0:
          flux_300_plot.append(float(flux_300[i]))
          freq300 = 300
          threehundred = plt.plot(np.log10(flux_300_plot), np.log10(freq300), "^", color = "purple", markersize = 5)

flux400 = 'psrcat -nohead -nonumber -o short -c "S400" %s' %j
flux400_list = shlex.split(flux400)
f = sb.Popen(flux400_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_400 = out.splitlines()

flux_400_plot = []
freq400 = []
for i in xrange(len(flux_400)):
    if flux_400[i].strip()!='*':
       f = float(flux_400[i])
       if f > 0:
          flux_400_plot.append(float(flux_400[i]))
          freq400 = 400
          fourhundred = plt.plot(np.log10(flux_400_plot), np.log10(freq400), "^", color = "purple", markersize = 5)

flux600 = 'psrcat -nohead -nonumber -o short -c "S600" %s' %j
flux600_list = shlex.split(flux600)
f = sb.Popen(flux600_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_600 = out.splitlines()

flux_600_plot = []
freq600 = []
for i in xrange(len(flux_600)):
    if flux_600[i].strip()!='*':
       f = float(flux_600[i])
       if f > 0:
          flux_600_plot.append(float(flux_600[i]))
          freq600 = 600
          sixhundred = plt.plot(np.log10(flux_600_plot), np.log10(freq600), "^", color = "purple", markersize = 5)

flux700 = 'psrcat -nohead -nonumber -o short -c "S700" %s' %j
flux700_list = shlex.split(flux700)
f = sb.Popen(flux700_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_700 = out.splitlines()

flux_700_plot = []
freq700 = []
for i in xrange(len(flux_700)):
    if flux_700[i].strip()!='*':
       f = float(flux_700[i])
       if f > 0:
          flux_700_plot.append(float(flux_700[i]))
          freq700 = 700
          sevenhundred = plt.plot(np.log10(flux_700_plot), np.log10(freq700), "^", color = "purple", markersize = 5)

flux800 = 'psrcat -nohead -nonumber -o short -c "S800" %s' %j  
flux800_list = shlex.split(flux800)
f = sb.Popen(flux800_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_800 = out.splitlines()

flux_800_plot = []
freq800 = []
for i in xrange(len(flux_800)):
    if flux_800[i].strip()!='*':
       f = float(flux_800[i])
       if f > 0:
          flux_800_plot.append(float(flux_800[i]))
          freq800 = 800
          eighthundred = plt.plot(np.log10(flux_800_plot), np.log10(freq800), "^", color = "purple", markersize = 5)

flux900 = 'psrcat -nohead -nonumber -o short -c "S900" %s' %j
flux900_list = shlex.split(flux900)
f = sb.Popen(flux900_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_900 = out.splitlines()

freq900 = 900
flux_900_plot = []

for i in xrange(len(flux_900)):
    if flux_900[i].strip()!='*':
       f = float(flux_900[i])
       if f > 0: 
          flux_900_plot.append(float(flux_900[i]))
          freq900 = 900
          ninehundred = plt.plot(np.log10(flux_900_plot), np.log10(freq900), "^" , color = "purple", markersize = 5)

flux1400 = 'psrcat -nohead -nonumber -o short -c "S1400" %s' %j
flux1400_list = shlex.split(flux1400)
f = sb.Popen(flux1400_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_1400 = out.splitlines()

flux_1400_plot = []
freq1400 = []
for i in xrange(len(flux_1400)):
    if flux_1400[i].strip()!='*':
       f = float(flux_1400[i])
       if f > 0:
          flux_1400_plot.append(float(flux_1400[i]))
          freq1400 = 1400
          fourteen = plt.plot(np.log10(flux_1400_plot), np.log10(freq1400), "^", color =  "purple", markersize = 5)

flux1600 = 'psrcat -nohead -nonumber -o short -c "S1600" %s' %j
flux1600_list = shlex.split(flux1600)
f = sb.Popen(flux1600_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_1600 = out.splitlines()

flux_1600_plot = []
freq1600 = []
for i in xrange(len(flux_1600)):
    if flux_1600[i].strip()!='*':
       f = float(flux_1600[i])
       if f > 0:
          flux_1600_plot.append(float(flux_1600[i]))
          freq1600 = 1600
          sixteen = plt.plot(np.log10(flux_1600_plot), np.log10(freq1600), "^", color = "purple", markersize = 5)

flux2000 = 'psrcat -nohead -nonumber -o short -c "S2000" %s' %j
flux2000_list = shlex.split(flux2000)
f = sb.Popen(flux2000_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_2000 = out.splitlines()

flux_2000_plot = []
freq2000 = []
for i in xrange(len(flux_2000)):
    if flux_2000[i].strip()!='*':
       f = float(flux_2000[i])
       if f > 0:
          flux_2000_plot.append(float(flux_2000[i]))
          freq2000 = 2000
          twothousand = plt.plot(np.log10(flux_2000_plot), np.log10(freq2000), "^", color = "purple", markersize = 5)

flux3000 = 'psrcat -nohead -nonumber -o short -c "S3000" %s' %j
flux3000_list = shlex.split(flux3000)
f = sb.Popen(flux3000_list,stdout=sb.PIPE)
out, err = f.communicate()
flux_3000 = out.splitlines()

flux_3000_plot = []
freq3000 = 3000
for i in xrange(len(flux_3000)):
    if flux_3000[i].strip()!='*':
       f = float(flux_3000[i])
       if f > 0:
          flux_3000_plot.append(float(flux_3000[i]))
          freq3000 = 3000
          threethousand = plt.plot(np.log10(flux_3000_plot), np.log10(freq3000),"^", color = "purple", markersize = 5)

flux4000 = 'psrcat -nohead -nonumber -o short -c "S4000" %s' %j
flux4000_list = shlex.split(flux4000)
f = sb.Popen(flux4000_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_4000 = out.splitlines()

flux_4000_plot = []
freq4000 = []
for i in xrange(len(flux_4000)):
    if flux_4000[i].strip()!='*':
       f = float(flux_4000[i])
       if f > 0: 
          flux_4000_plot.append(float(flux_4000[i]))
          freq4000 = 4000
          fourthousand = plt.plot(np.log10(flux_4000_plot), np.log10(freq4000), "^", color = "purple", markersize = 5)
flux5000 = 'psrcat -nohead -nonumber -o short -c "S5000" %s' %j
flux5000_list = shlex.split(flux5000)
f = sb.Popen(flux5000_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_5000 = out.splitlines()

flux_5000_plot = []
freq5000 = 5000
for i in xrange(len(flux_5000)):
    if flux_5000[i].strip()!='*':
       f = float(flux_5000[i])
       if f > 0:
          flux_5000_plot.append(float(flux_5000[i]))
          freq5000 = 5000
          fivethousand = plt.plot(np.log10(flux_5000_plot), np.log10(freq5000), "^", color = "purple", markersize = 5)

flux6000 = 'psrcat -nohead -nonumber -o short -c "S6000" %s' %j
flux6000_list = shlex.split(flux6000)
f = sb.Popen(flux6000_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_6000= out.splitlines()

flux_6000_plot = []
fre6000 = []
for i in xrange(len(flux_6000)):
    if flux_6000[i].strip()!='*':
       f = float(flux_6000)
       if f > 0:
          flux_6000_plot.append(float(flux_6000[i]))
          freq6000 = 6000
          sixthousand = plt.plot(np.log10(flux_6000_plot), np.log10(freq6000), "^", color = "purple", markersize = 5)

flux8000 = 'psrcat -nohead -nonumber -o short -c "S8000" %s' %j
flux8000_list = shlex.split(flux8000)
f = sb.Popen(flux8000_list, stdout=sb.PIPE)
out, err = f.communicate()
flux_8000 = out.splitlines()

flux_8000_plot = []
freq8000 = []
for i in xrange(len(flux_8000)):
    if flux_8000[i].strip()!='*':
       f = float(flux_8000)
       if f > 0:
          flux_8000_plot.append(float(flux_8000[i]))
          freq8000 = 8000
          eightthousand = plt.plot(np.log10(flux_8000_plot), np.log10(freq8000), "^", color = "purple", markersize = 5)
#this section ensures that plots are only made for pulsars that have values for flux  
if thirty == 0:
    if fourty == 0:
        if fifty == 0:
            if sixty == 0:
                if eighty == 0:
                    if hundred == 0:
                        if hundredfifty == 0:
                            if twohundred == 0:
                                if threehundred == 0:
                                    if fourhundred == 0:
                                        if sixhundred == 0:
                                            if sevenhundred == 0:
                                                if eighthundred == 0:
                                                    if ninehundred == 0:
                                                        if fourteen == 0:
                                                            if sixteen == 0:
                                                                if twothousand ==0:
                                                                    if threethousand == 0:
                                                                        if fourthousand == 0:
                                                                            if fivethousand == 0:
                                                                                if sixthousand == 0:
                                                                                    if eightthousand == 0:
                                                                                        print " "
else:
    title = 'Frequency vs Flux for %s' %j
    fig.suptitle(title)
    plt.xlabel('log(frequency) (MHz)')
    plt.ylabel('log(flux) (mJy)')
    name = '%sflux.png'%j
    plt.savefig(name)


