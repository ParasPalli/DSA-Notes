# Binary Search Requires Sorted Array....


def binarySearch(arr, low, high, x):
 
	if high >= low:
		
		mid = (low + high) // 2

		if arr[mid] == x:
			return mid
		
		if arr[mid] > x:
			return binarySearch(arr, low, mid - 1, x)
		
		else:
			return binarySearch(arr, mid + 1, high, x)

	else:
		return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

x = 8

result = binarySearch(arr, 0, len(arr)-1, x)

print(result)


# Time Complexity = O(log n)
# Best Time Complexity = O(1)

