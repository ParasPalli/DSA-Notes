
# Merge Sort....
def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        Merge(arr, L, R)


def Merge(arr, L, R):

    i = j = k = 0

    # Merging and Sorting the Left and Right arrays...
    # Until we reach either end of either L or M, pick larger among
    while i < len(L) and j < len(R):

        if L[i] < R[j]:

            arr[k] = L[i]
            i += 1

        else:

            arr[k] = R[j]
            j += 1
        
        k += 1

    # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
    
    # Adding remaining elements of Left Array....
    while i < len(L):

        arr[k] = L[i]
        i += 1
        k += 1

    # Adding remaining elements of Left Array....
    while j < len(R):

        arr[k] = R[j]
        j += 1
        k += 1


    
# Unsorted Array....
        
array = [3, 1, 5, 2, 4, 8, 6, 9, 7, 12, 10]

mergeSort(array)

print(array)



# Times Complexity = O(nlogn)