import numpy as np
import random
import matplotlib.pyplot as plt
import cProfile, time
import pandas as pd
import sys
import csv
import os


totalTimeInsertion = 0
totalTimeSelection = 0
totalTimePython = 0
totalTimeQuick = 0

# Insersition Sort Function
def insertionSort(arr):
    global totalTimeInsertion
    start = time.time()
    theLength = len(arr)
      
    if theLength <= 1:
        return  #returns sorted sets
 
    for each in range(1, theLength):  # Iterate over from second index
        # Find the minimum 
        key = arr[each]  # Store the current element
        i = each-1
        while i >= 0 and key < arr[i]:  # move the greater items ahead
            arr[i+1] = arr[i]  # Shift elements right
            i -= 1
        arr[i+1] = key  # Insert key in correct position

    end = time.time()
    totalTimeInsertion = end - start
    totalTimeInsertion = round(totalTimeInsertion, 3)

#Selection Sort
def selectionSort(arr):
    global totalTimeSelection
    start = time.time()
    # Traverse through all array elements
    for each in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = each
        for j in range(each + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[each], arr[min_index] = arr[min_index], arr[each]

    end = time.time()
    totalTimeSelection = end - start
    totalTimeSelection = round(totalTimeSelection, 3)


#Python sort function

def pythonSort(arr):
    global totalTimePython
    start = time.time()
    arr.sort()
    end = time.time()
    totalTimePython = end - start
    totalTimePython = round(totalTimePython, 3)


#Quick Sort Function
def partition(array, low, high):

    # choose highest pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # compare each element
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # swapping
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot 
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the partition position
    return i + 1

def quickSort(array, low, high):
    global totalTimeQuick
    start = float(time.time())
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call left pivot
        quickSort(array, low, pi - 1)

        # Recursive call right pivot
        quickSort(array, pi + 1, high)

        sys.setrecursionlimit(999999999)
    
    end = float(time.time())
    totalTimeQuick = end - start
    totalTimeQuick = round(totalTimeQuick, 3)



for each in range(10):
    print("its working")
    theInput = random.randint(1,100000)
    theList = np.random.choice(1, 999999999,theInput)
    insertionList = theList.copy()
    selectionList = theList.copy()
    quickList = theList.copy()
    pythonList = theList.copy()

    totalTimeInsertion = 0
    totalTimeSelection = 0
    totalTimePython = 0
    totalTimeQuick = 0

    size = len(quickList)

    quickSort(quickList, 0, size - 1)

    insertionSort(insertionList)

    pythonSort(pythonList)

    selectionSort(selectionList)

    #writing to csv
    

    data = [{
        'Datasize': theInput,
        'Insertion Sort Time': totalTimeInsertion,
        'Selection Sort Time': totalTimeSelection,
        'Python Sort Time': totalTimePython,
        'Quick Sort Time': totalTimeQuick,
    }]
    with open('multithreadTesting.csv', 'a', newline='') as csvfile:
        fieldnames = ['Datasize', 'Insertion Sort Time', 'Selection Sort Time', 'Python Sort Time', 'Quick Sort Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        fileExists = os.path.isfile('multithreadTesting.csv')
        if not fileExists:
            writer.writeheader()
        writer.writerows(data)


# # Pull data from csv
mycsv = csv.reader(open('multithreadTesting.csv'))
next(mycsv)
insertionValuesList = []
selectionValuesList = []
pythonValuesList = []
quickValuesList = []
theDataList = []
for row in mycsv:
   text = float(row[1])
   text2 = float(row[2])
   text3 = float(row[3])
   text4 = float(row[4])
   theData = float(row[0])
   insertionValuesList.append(text)
   selectionValuesList.append(text2)
   pythonValuesList.append(text3)
   quickValuesList.append(text4)
   theDataList.append(theData)
   insertionValuesList = sorted(insertionValuesList)
   selectionValuesList = sorted(selectionValuesList)
   pythonValuesList = sorted(pythonValuesList)
   quickValuesList = sorted(quickValuesList)
   theDataList = sorted(theDataList)


xData = theDataList
yInsert = insertionValuesList
ySelection = selectionValuesList
yPython = pythonValuesList
yQuick = quickValuesList


# failed attempt to write to excel
# read_file_product = pd.read_csv (r'/Users/ajmanuel/Documents/Algorithm Assignment/sortTesting.csv')
# read_file_product.to_excel (r'/Users/ajmanuel/Documents/Algorithm Assignment/CSVDataImported.xlsx', index = None, header=True)

# new_dataFrame = pd.read_csv('sortTesting.csv')
# new_excel = pd.ExcelWriter('SampleFile.xlsx')
# new_dataFrame.to_excel(new_excel, index=False)
# new_excel.save()

# plot lines
plt.plot(xData, yInsert, label = "Insertion Sort", linestyle="-")
plt.plot(xData, ySelection, label = "Selection Sort", linestyle="-")
plt.plot(xData, yPython, label = "Python Sort", linestyle="-")
plt.plot(xData, yQuick, label = "Quick Sort", linestyle="-")
plt.legend()
plt.show()



