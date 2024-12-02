def loadData():
    f = open("input.txt", 'r')
    intputlist = []
    for line in f.readlines():
        split_values = line.split(" ")
        intputlist.append(split_values)
    return intputlist

def solOne():
    inputList = loadData()
    totSafe = 0
    for report in inputList:
        if checkIfSafe(report):
            totSafe += 1
    print(totSafe)
    
def checkIfSafe(report):
    increasing = True
    stillSafe = True
    if int(report[0]) > int(report[1]):
        increasing = False
    lastVal = int(report[0])
    for i in range(1,len(report)):
        if increasing:
            if int(report[i]) > lastVal:
                #Good
                if 1<= abs(int(report[i]) - lastVal) <=3:
                    #Good
                    lastVal = int(report[i])
                    pass
                else:
                    stillSafe = False
                    break
            else:
                stillSafe = False
                break
                   
            
        else:
            if int(report[i]) < lastVal:
                #Good
                if 1<= abs(int(report[i]) - lastVal) <=3:
                    #Good
                    lastVal = int(report[i])
                    pass
                else:
                    stillSafe = False
                    break
            else:
                stillSafe = False
                break
    return stillSafe
            
        
    
def solTwo():
    inputList = loadData()
    totSafe = 0
    unsafeList = []
    
    for report in inputList:
        if checkIfSafe(report):
            totSafe += 1
        else:
            unsafeList.append(report)
    for report in unsafeList:
        dampenedReports = []
        for val in report:
            reportCopy = report.copy()
            reportCopy.remove(val)
            dampenedReports.append(reportCopy)
        for report in dampenedReports:
            if checkIfSafe(report):
                totSafe += 1
                break
    print(totSafe)
        
        
        
    
    

def main():
    print("============================SOL ONE================================")
    solOne()
    print("============================SOL TWO=============================== ")
    solTwo()
    pass

if __name__ == "__main__":
    main()