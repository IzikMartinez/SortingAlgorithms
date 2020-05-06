import pandas
import insert
import MergeSort
import random
import time

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


list1 = make_array(10, 50)
display_list(list1)

print("Merge Sort")
MergeSort.merge_sort(list1)

display_list(list1)

endTime = time.time() - startTime

print(endTime)

