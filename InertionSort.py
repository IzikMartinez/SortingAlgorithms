Unsorted = [1, 3, 7, 2, 4, 10, 9]


def insertion_sort(array):
    # check if i ls less than i-1
    # if it is, then swap i with i-1
    # repeat this process for i-2 .. i-n
    for i in range(1, len(array)):
        # Key will hold the current element of the array.
        key = array[i]
        # We need to compare key to every element before it in the array, so we initialize it to i-1
        j = i-1

        # We are going to be decrementing, so we need to set a loop condition as "J is at least 0" so that we don't
        # decrement j into the negatives
        # The second condition is that key (the current element of the array we are checking) is smaller than
        # the element at index j. This has the effect of comparing key to every element before it, and whenever
        # it locates an element smaller then itself it swaps with that element.
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1


print("Hello moto")
