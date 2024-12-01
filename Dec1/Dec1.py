

def loadData():
    f = open("input.txt", 'r')
    leftList = []
    rightList = []
    for line in f.readlines():
        split_values = line.split("   ")
        leftList.append(int(split_values[0]))
        rightList.append(int(split_values[1]))
    return leftList, rightList

def pOneSolve():
    subtractedValues = []
    leftlist, rightlist = loadData()
    leftlist.sort()
    rightlist.sort()
    for i in range(len(leftlist)):
        subtractedValues.append(abs(leftlist[i] - rightlist[i]))
    print(sum(subtractedValues))

def pTwoSolve():
    total = 0
    leftlist, rightlist = loadData()
    for num in leftlist:
        indices = [i for i, x in enumerate(rightlist) if x == num]
        if len(indices) > 0:
            total += (num * len(indices))
    print(total)
    

def main():
    print("===================PART ONE===========================")
    pOneSolve()
    print("===================PART TWO===========================")
    pTwoSolve()
    pass

if __name__ == "__main__":
    main()