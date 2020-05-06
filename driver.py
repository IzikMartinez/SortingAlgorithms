import pandas as pd
import InertionSort
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
unsorted_arrays = []
n = []
merge_times = []
insertion_times = []

#Create 11 arrays of a random size from 1000 to 100000
for x in range(11):
    n.append(random.randrange(1000,100000,1))
    unsorted_arrays.append(make_array(n[x], 100))

sorted_arraysM = unsorted_arrays.copy()

#Sort all of the arrays using merge sort and save the time taken to sort
print("Merge Sort")
for x in range(11):
    startTime = time.time()
    MergeSort.merge_sort(sorted_arraysM[x])
    merge_times.append(time.time() - startTime)

#Sort all of the arrays using insertion sort and save the time taken to sort
print("Insertion Sort")
for x in range(11):
    startTime = time.time()
    InertionSort.insertion_sort(unsorted_arrays[x])
    insertion_times.append(time.time() - startTime)


#Store the array size and merge sort times in a pandas data frame
merge_df = pd.DataFrame(list(zip(n, merge_times)), columns = ['Size', 'Merge Sort Time'])
print(merge_df)

#Store the array size and insertion sort times in a pandas data frame
insertion_df = pd.DataFrame(list(zip(n, insertion_times)), columns = ['Size', 'Insertion Sort Time'])
print(insertion_df)

#Plot the size vs merge sort time
merge_df.plot(x = 'Size', y = 'Merge Sort Time', kind = 'scatter')
plt.title('Merge Sort Analysis')
plt.show()

#Plot the size vs insertion sort time
insertion_df.plot(x = 'Size', y = 'Insertion Sort Time', kind = 'scatter')
plt.title('Insertion Sort Analysis')
plt.show()