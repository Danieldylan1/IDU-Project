#Import Requirements
import numpy as np
import matplotlib.pyplot as plt

#Open Files
tfile = open("data/tropo.txt", 'r')
sfile = open("data/surftemp.txt", 'r')

#Procedures
def remove_empty(l):
    """
    Removes empty elements from a list
    Precondition: l is a list
    """
    i = 0
    while i < len(l):
        if l[i] == '' or l[i] == ' ':
            del l[i]
        i = i + 1

#Get Dates
dates = []
lines = tfile.read().splitlines() #Get lines from file
i = 0
while i < len(lines): #Remove empty elements
    if lines[i] == '' or lines[i] == ' ':
        del lines[i]
    i = i + 1
lines[len(lines) - 2] = lines[len(lines) - 2] + lines[len(lines) - 1] #Concatenate last elements
del lines[-1] #Delete last element
for i in lines:
    i.split(' ')
    dates.append(i[0:3])

#Get Data Points
tdata = []
sdata = []
tlines = tfile.read().splitlines()
slines = sfile.read().splitlines()
for i in tlines:
    i.split(' ')
    tdata.append(i[9:])
remove_empty(tdata)
tdata = [float(x) for x in tdata]
for i in slines:
    i.split(' ')
    sdata.append(i[4:])
remove_empty(sdata)
sdata = [float(x) for x in sdata]

#Graph Data
#Plot surface temperatures against dates
plt.plot(sdata)
plt.title("Surface Temperature at ")
plt.xlabel("Months (JAN 1999 - JAN 2001)")
plt.xticks(np.arange(25), dates)
plt.ylabel("Surface Temperature (C)")
plt.show()
