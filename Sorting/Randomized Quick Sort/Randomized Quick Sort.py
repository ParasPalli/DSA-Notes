

# Randomized_quick_sort using Hoare Partitioning

import random
  

def partition(arr, low, high):

    pivot = arr[low]

    i = low - 1
    j = high + 1

    while(True):

        while(True):

            i += 1

            if arr[i] >= pivot:
                break

        while(True):
            
            j -= 1

            if arr[j] <= pivot:
                break
        
        if i >= j:
            return j
        
        # Swap.....
        arr[i], arr[j] = arr[j], arr[i]




def random_partition(arr, low, high):

    random_number = random.randint(low, high)

    arr[low], arr[random_number] = arr[random_number], arr[low]

    return partition(arr, low, high)




def quick_sort(arr, low, high):

    if low < high:
        
        p = random_partition(arr, low, high)

        quick_sort(arr, low, p)
        quick_sort(arr, p+1, high)

        

array = [1, 3, 4, 7, 10, 13, 2, 5, 9, 6]

quick_sort(array, 0, len(array)-1)

print(array)



# Average Time Complexity = O(nlogn)
# Worst Time Complexity = O(n^2)