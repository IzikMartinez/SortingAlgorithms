import pandas as pd
import insert
import MergeSort
import random
import time
import matplotlib.pyplot as plt

startTime = time.time()


# This is a simple function that prints all the elements in a list
def display_list(array):
    for j in array:
        print(j)
    print("\n\n")


# Make Array
# Input: Size (int) the number of elements this array will contain
# Input: Width (int) the limit on how big a randomly generated number will be. E.G. if width is 100 then the
#       list will be populated with numbers between 1 and 100
# Output: Array (list): A list of 'size' elements, each of which is a random integer between 1 and 'width'
def make_array(size, width):
    array = [0] * size
    for i in range(0, size):
        array[i] = random.randrange(width)
    return array

#Declare arrays to hold the arrays to be sorted, their respective size, and the sort time
arrays = []
n = []
times = []

#Create 11 arrays of a random size from 10 to 100
for x in range(11):
   # print("Array ", x+1, ":")
    n.append(random.randrange(1000,100000,1))
    arrays.append(make_array(n[x], 100))
    #display_list(arrays[x])

#Sort all of the arrays and save the time taken to sort
print("Merge Sort")
for x in range(11):
    startTime = time.time()
    MergeSort.merge_sort(arrays[x])
    times.append(time.time() - startTime)
    #print("Array ", x + 1, ":")
    #display_list(arrays[x])

#Store the array size and sort times in a pandas data frame
df = pd.DataFrame(list(zip(n, times)), columns = ['Size', 'Sort Time'])
print(df)

#Plot the size vs sort time
df.plot(x = 'Size', y = 'Sort Time', kind = 'scatter')
plt.show()