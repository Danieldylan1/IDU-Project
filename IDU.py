#Import Requirements
import numpy as np
import matplotlib.pyplot as plt
import time as t
import sys

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
def typewriter(s):
    """
    Prints text in typewriter format
    Precondition: s is a string
    """
    for c in s:
        sys.stdout.write(c)
        t.sleep(0.003)

#Credits
credits = "This project was created by Robert Bao and Jason Liu, \nFeatures of this include: Different Graphs, Hypothesis and Data Analysis, \nLocation of the Area Surveyed, and the variables\n"
typewriter(credits)

#Open Files
tfile = open('tropo.txt', 'r')
sfile = open('surftemp.txt', 'r')

#Get Dates
dates = []
lines = tfile.read().splitlines() #Get lines from file
tfile.seek(0)
i = 0
while i < len(lines) : #Remove empty elements
    if lines[i] == '' or lines[i] == ' ':
        del lines[i]
    i = i + 1
del lines[-1] #Delete last element
for i in lines:
    i.split(' ')
    dates.append(i[0:3])
dates.append('JAN')

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
for j in slines:
    j.split(' ')
    sdata.append(j[9:])
remove_empty(sdata)
sdata = [float(x) for x in sdata]

#Graph Data
#Plot surface temperatures against dates
chooseGraph = ""
chooseAnalysis = ""
graphText = "Please choose a graph or analysis to display: \n       Surface Temperature against Months (smonth) \n       Tropospheric Ozone against Months (tmonth) \n       Surface Temperature against Tropospheric Ozone (surfozone) \n       Our analysis of the data (analysis) "
analysisText = "What would you like to see? (hypothesis, variables, location, data, climatechange, predictions) "
while chooseGraph.upper() != "QUIT":
    chooseGraph = input(graphtext)
    if chooseGraph.upper() == "SMONTH":
        plt.plot(sdata, 'b--')
        plt.title("Surface Temperature at 35 N, 85 W")
        plt.xlabel("Months (JAN 1999 - JAN 2001)")
        plt.ylabel("Surface Temperature (C)")
        plt.xticks(np.arange((len(dates)) + 1), dates)
        plt.legend('Surface Temperatures')
        plt.show()
    elif chooseGraph.upper() == "TMONTH":
        plt.plot(tdata, 'r--')
        plt.title("Tropospheric Ozone at 35 N, 85 W")
        plt.xlabel("Months (JAN 1999 - JAN 2001)")
        plt.ylabel("Tropospheric Ozone (Dobson Units)")
        plt.xticks(np.arange(len(dates)), dates)
        plt.legend(['Tropospheric Ozone'])
        plt.show()
    elif chooseGraph.upper() == "SURFOZONE":
        plt.scatter(sdata, tdata)
        plt.title("Comparison Between Surface Temperature and Tropospheric Ozone at 35 N, 85 W")
        plt.xlabel("Surface Temperature (C)")
        plt.ylabel("Tropospheric Ozone (Dobson Units)")
        plt.plot(sdata, np.poly1d(np.polyfit(sdata, tdata, 1))(sdata), 'g:')
        plt.show()
    elif chooseGraph.upper() == "ANALYSIS":
        chooseAnalysis = input(analysisText)
        while chooseAnalysis.upper() != "QUIT":
            if chooseAnalysis.upper() == "HYPOTHESIS":
                print(">>> HYPOTHESIS <<<")
                t.sleep(0.5)
                print()
    elif chooseGraph.upper() == "QUIT":
        print("Quitting...")
    else:
        print("Invalid Input!")