#Import Requirements
import numpy as np
import matplotlib.pyplot as plt

#Open Files
tfile = open('data/tropo.txt', 'r')
sfile = open('data/surftemp.txt', 'r')
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
tfile.seek(0)
i = 0
while i < len(lines): #Remove empty elements
    if lines[i] == '' or lines[i] == ' ':
        del lines[i]
    i = i + 1
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
for x in tdata:
    print(x)
for x in sdata:
    print(x)
for j in slines:
    j.split(' ')
    sdata.append(j[9:])
remove_empty(sdata)
sdata = [float(x) for x in sdata]

#Graph Data
#Plot surface temperatures against dates
chooseGraph = ""
while chooseGraph != "quit":
    chooseGraph = input("Please choose a graph or analysis to display (Surface Temperature against Months (smonth), Tropospheric Ozone against Months (tmonth), Surface Temperature against Tropospheric Ozone (surfozone), Analysis (analysis)) ")
    if chooseGraph == "smonth":
        plt.plot(sdata)
        plt.title("Surface Temperature at 35 N, 85 W")
        plt.xlabel("Months (JAN 1999 - JAN 2001)")
        plt.ylabel("Surface Temperature (C)")
        plt.xticks(np.arange((len(dates)) + 1), dates)
        plt.show()
    elif chooseGraph == "tmonth":
        plt.plot(tdata)
        plt.title("Tropospheric Ozone at 35 N, 85 W")
        plt.xlabel("Months (JAN 1999 - JAN 2001)")
        plt.ylabel("Tropospheric Ozone (Dobson Units)")
        plt.xticks(np.arange((len(dates)) + 1), dates)
        plt.show()
    elif chooseGraph == "surfozone":
        plt.scatter(sdata, tdata)
        plt.title("Comparison Between Surface Temperature and Tropospheric Ozone at 35 N, 85 W")
