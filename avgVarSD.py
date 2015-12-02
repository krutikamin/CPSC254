total = 0
num = 0
numEntered = 0
intArray = []

def CalculateAverage(total, numInts):
    return (total / numInts)

def CalculateVariance(myArray, avg):
    numInts = len(myArray)
    temp = 0
    difference = 0
    while (numInts > 0):
        temp = myArray[numInts -1] - avg
        temp *= temp
        difference += temp
        numInts -= 1
    return (difference / numEntered)
    
def CalculateSD(var):
    return ((var)**0.5)
 
while(num >= 0):
    global total
    global numEntered
    global intArray
    num = int(input("Enter a positive integer, negative to quit: "))
    if (num < 0):
        average = CalculateAverage(total, numEntered)
        print ("Average is %s." %(average))
        variance = CalculateVariance(intArray, average)
        print ("Variance is %s." %(variance))
        SD = CalculateSD(variance)
        print('Standard Deviation is %s' %(SD))
        break
    else:
        intArray.append(num)
        total += num
        numEntered += 1
