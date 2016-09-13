import csv
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image

def getList(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        listofnum = list(next(reader))
    return listofnum

def findLocalMax(listofNumb):
    localmax = []
    localmax.append(listofNumb[0])
    i = 1
    while i < len(listofNumb) - 1:
        if((listofNumb[i] > listofNumb[i-1] and listofNumb[i] > listofNumb[i+1])
         or (listofNumb[i] > listofNumb[i-1] and listofNumb[i] == listofNumb[i+1])
         or (listofNumb[i] == listofNumb[i-1] and listofNumb[i] > listofNumb[i+1])):
            localmax.append(listofNumb[i])
            i+= 1
        else:
            i+= 1

    if(listofNumb[-1] > localmax[-1]):
        localmax.append(listofNumb[-1])

    return localmax

def findLocalMin(listofNumb):
    localmin = []
    localmin.append(listofNumb[0])
    i = 1
    while i < len(listofNumb):
        if(listofNumb[i] < listofNumb[i-1] and listofNumb[i] < listofNumb[i+1]):
            localmin.append(listofNumb[i])
            i+= 1
        else:
            i+= 1
    return localmin

def fibRet(listofNumb, globalmax, globalmin):
    fiblines = []
    globaldiff = globalmax - globalmin
    fiblines.append(globalmin)
    fiblines.append(globalmin + (.382*globaldiff))
    fiblines.append(globalmin + (.5*globaldiff))
    fiblines.append(globalmin + (.618*globaldiff))
    fiblines.append(globalmax)

    currenttrend = detTrend(listofNumb)
    if((currenttrend == "decreasing trend.")):
        fiblines = fiblines[::-1]

    return fiblines

def getGlobalMaxIndex(listofNumb):
    globalmax = max(listofNumb)
    globalmaxindex = len(listofNumb)-1-listofNumb[::-1].index(globalmax)
    return globalmaxindex

def getGlobalMinIndex(listofNumb):
    globalmin = min(listofNumb)
    globalminindex = len(listofNumb)-1-listofNumb[::-1].index(globalmin)
    return globalminindex

def getAvg(listofNumb):
    simpAvg = sum(listofNumb)/len(listofNumb)
    return simpAvg

def whichLater(listofNumb):
    dex1 = getGlobalMinIndex(listofNumb)
    dex2 = getGlobalMaxIndex(listofNumb)

    if (dex1 > dex2):
        thisOne = dex1
    else:
        thisOne = dex2

    return thisOne

def plotGraph(listofNumb, fiblines):

    dex = whichLater(listofNumb)
    simpAvg = getAvg(listofNumb[dex:])
    newPointX = [len(listofNumb) - 1, len(listofNumb)]
    newPointY = [listofNumb[len(listofNumb)-1], simpAvg]

    plt.figure(figsize=(20,10))

    plt.plot(listofNumb)
    plt.plot(len(listofNumb), simpAvg, 'ro')
    plt.plot(newPointX, newPointY, 'ro-')
    for i in range(0,len(fiblines)):
        plt.axhline(y = fiblines[i], color = 'y')

    plt.ylabel('Price')
    plt.savefig('first.jpg')
    Image.open('first.jpg').show()

    #plt.draw()

def detTrend(listofNumb):
    relList = []
    trendlist = []
    dex = whichLater(listofNumb)
    relList = listofNumb[dex:]

    localmax = findLocalMax(relList)

    if(len(localmax) == 0):
        trend = "Stable."
    else:
        i = 1
        while (i < len(localmax)):
            if(localmax[i] > localmax[i-1]):
                trendlist.append("increasing trend ")
                i += 1
            elif(localmax[i] < localmax[i-1]):
                trendlist.append("decreasing trend ")
                i+= 1
            else:
                #trendlist.append("stable trend.")
                i += 1

            counts = Counter(trendlist)
            trend = max(counts, key = counts.get)

    return trend

def rangefiblines(fiblist, dire):
    UB = []
    LB = []
    const = 0.30

    if(dire == "+"):
        UB.append(fiblist[0] + (const*abs(fiblist[0] - fiblist[1])))
        UB.append(fiblist[1] + (const*abs(fiblist[1] - fiblist[2])))
        UB.append(fiblist[2] + (const*abs(fiblist[2] - fiblist[3])))
        UB.append(fiblist[3] + (const*abs(fiblist[3] - fiblist[4])))
        UB.append(fiblist[4] + (const*abs(fiblist[3] - fiblist[4])))

        LB.append(fiblist[0] - (const*abs(fiblist[0] - fiblist[1])))
        LB.append(fiblist[1] - (const*abs(fiblist[0] - fiblist[1])))
        LB.append(fiblist[2] - (const*abs(fiblist[1] - fiblist[2])))
        LB.append(fiblist[3] - (const*abs(fiblist[2] - fiblist[3])))
        LB.append(fiblist[4] - (const*abs(fiblist[3] - fiblist[4])))
    else:
        UB.append(fiblist[0] + (const*abs(fiblist[0] - fiblist[1])))
        UB.append(fiblist[1] + (const*abs(fiblist[0] - fiblist[1])))
        UB.append(fiblist[2] + (const*abs(fiblist[2] - fiblist[1])))
        UB.append(fiblist[3] + (const*abs(fiblist[3] - fiblist[2])))
        UB.append(fiblist[4] + (const*abs(fiblist[3] - fiblist[4])))

        LB.append(fiblist[0] - (const*abs(fiblist[0] - fiblist[1])))
        LB.append(fiblist[1] - (const*abs(fiblist[2] - fiblist[1])))
        LB.append(fiblist[2] - (const*abs(fiblist[3] - fiblist[2])))
        LB.append(fiblist[3] - (const*abs(fiblist[4] - fiblist[3])))
        LB.append(fiblist[4] - (const*abs(fiblist[3] - fiblist[4])))

    return {'UB': UB, 'LB': LB}

def ovrTrend(listofNumb):
    ovrTrend = ""

    if(listofNumb[-1] > listofNumb[0]):
        ovrTrend = "increasing"
    elif(listofNumb[-1] < listofNumb[0]):
        ovrTrend = "decreasing"
    else:
        ovrTrend = "undetermined"

    return ovrTrend

def intro():
    print("\nWelcome to Forex Trading Assistant V1! You are currently viewing the USD/CAD rate.\n\nHere are the following list of commands: \n")

def commands():
    print("--------------------------------------------------------------------------------\nPress 'c' to view the current chart.\nPress 'a' to seek current trading advice.\nPress 's' to view another currency pair.\nPress 'q' to quit the program.\n")

def runAnalyses(listofNumb):
    fibrat = ["0","38.2%","50%","61.8%","100%"]
    globalmaxindex = getGlobalMaxIndex(listofNumb)
    globalminindex = getGlobalMinIndex(listofNumb)
    boolindex = globalmaxindex > globalminindex
    currenttrend = detTrend(listofNumb)
    overTrend = ovrTrend(listofNumb)
    if(overTrend == "undetermined" or currenttrend == "stable trend."):
        print("\nNo immediate trend detected, please wait until a trend becomes apparent.\n")
        return

    if((currenttrend == "increasing trend.")):
        dire = "+"
    else:
        dire = "-"

    fiblines = fibRet(listofNumb, listofNumb[globalmaxindex], listofNumb[globalminindex])
    rangeUB = rangefiblines(fiblines, dire)['UB']
    rangeLB = rangefiblines(fiblines, dire)['LB']

    for index, x in enumerate(fiblines):

        #Trading advice is given here based on 
        print("Please contact ashton.sidhu1994@gmail.com for questions and inquiries about the program's logic!")

def main():
    cont = True
    intro()
    commands()
    while(cont):
        pricelist = [float(i) for i in getList('test.csv')]
        inp = input("Please enter a command(c, a, s, q): ")
        if(inp == "c"):
            globalmaxindex = getGlobalMaxIndex(pricelist)
            globalminindex = getGlobalMinIndex(pricelist)
            fiblines = fibRet(pricelist, pricelist[globalmaxindex], pricelist[globalminindex])
            plotGraph(pricelist,fiblines)
            print("\nGraph Displayed!\n")
            commands()

        elif(inp == "a"):
            runAnalyses(pricelist)
            commands()

        elif(inp == "s"):
            print("\nSorry this feature is unavailable at this time.\n")
            commands()

        elif(inp == "q"):
            print("\nThank you for using Forex Trading Assistant V1.\n\n\n\n\nShutting down!")
            cont = False

        else:
            print("Invalid Command, please try again!")
            commands()

if __name__ == '__main__':
    main()
