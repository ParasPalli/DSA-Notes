import sys
 
# Divide and conquer solution to find the minimum and maximum number in a list
def findMinAndMax(nums, left, right, min=sys.maxsize, max=-sys.maxsize):
 
    # if the list contains only one element
 
    if left == right:               
 
        if min > nums[left]:          
            min = nums[left]
 
        if max < nums[left]:          
            max = nums[left]
 
        return min, max
 
    # if the list contains only two elements
 
    if right - left == 1:           
 
        if nums[left] < nums[right]:   

            if min > nums[left]:     
                min = nums[left]
 
            if max < nums[right]:    
                max = nums[right]
 
        else:
            
            if min > nums[right]:     
                min = nums[right]
 
            if max < nums[left]:      
                max = nums[left]
 
        return min, max
 
    # find the middle element
    mid = (left + right) // 2
 
    # recur for the left sublist
    min, max = findMinAndMax(nums, left, mid, min, max)
 
    # recur for the right sublist
    min, max = findMinAndMax(nums, mid + 1, right, min, max)
 
    return min, max
 
 # First Left Side Sorting is Done and then Right Side.... and as the min and max are same for over all function so once left side is done...
 # Then right side is done..... And as the min and Max are static their values will be changed according to it.....
 
 
nums = [7, 2, 9, 3, 24, 6, 10, 1, 75, 8, 4, 10]

min, max = findMinAndMax(nums, 0, len(nums) - 1)

print("The minimum element in the list is", min)
print("The maximum element in the list is", max)


# Time Complexity is O(n)