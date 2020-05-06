

# Merge Sort
def merge_sort(array):
    if len(array) > 1:
        # Save the size of the halfway point
        halfway = int(len(array)/2)
        # copy the first half of the array into a new variable
        first_half = array[:halfway]
        # copy the second half of the array into a new variable
        second_half = array[halfway:]

        # Counters
        i = 0
        j = 0
        k = 0

        # Recursively split the first half of the array in to two arrays
        merge_sort(first_half)
        # Recursively split the second half of the array into two arrays
        merge_sort(second_half)

        # loop as long as I is not as big as our first half (IE for every element in first_half) and J is not as big as
        #       len(second_half) IE for every element in the second_half
        while i < len(first_half) and j < len(second_half):
            # Compare the current element from both halves of the array and store the smallest one in the current
            # position of the main array. Then increment the choosen half.
            # This has the effect of comparing each element of the two sub-arrays against one another, always choosing
            # the smaller of the two elements to build a new, fully sorted array
            if first_half[i] < second_half[j]:
                array[k] = first_half[i]
                i += 1
            else:
                array[k] = second_half[j]
                j += 1
            k += 1
        while i < len(first_half):
            array[k] = first_half[i]
            i += 1
            k += 1
        while j < len(second_half):
            array[k] = second_half[j]
            j += 1
            k += 1



