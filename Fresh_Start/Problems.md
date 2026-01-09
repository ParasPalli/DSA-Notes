# Arrays

### 1. Two Sum [1]

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\
You may assume that each input would have exactly one solution, and you may not use the same element twice.\
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9\
Output: [0,1]\
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6\
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6\
Output: [0,1]

**Solution:**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNumberMap = {}

        for index, value in enumerate(nums):
            diff = target - value

            if (previousNumberMap.get(diff) is not None): 
                return [index, previousNumberMap.get(diff)]
            
            previousNumberMap[value] = index
```

**Explanation:**

target - current_number => left_over_number

Check LeftOverNumber present previously in the list or in this case map

9 - 7 = 2

So, 2 + 7 => 9
And 2 is present in the Map


---
### 2. Find All Numbers Disappeared in an Array [448]

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]\
Output: [5,6]

Example 2:

Input: nums = [1,1]\
Output: [2]

**Solution**
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNums = set(nums)
        result = []

        for x in range(1, len(nums) + 1):
            if x not in setNums:
                result.append(x)

        return result
```


---
### 3. Contains Duplicate [217]

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]\
Output: true\
Explanation:\
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]\
Output: false\
Explanation:\
All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]\
Output: true

**Solution**
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```


---
### 4. Minimum time visiting all the points [1266]

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

- In 1 second, you can either:
    - move vertically by one unit,
    - move horizontally by one unit, or
    - move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).

- You have to visit the points in the same order as they appear in the array.
- You are allowed to pass through points that appear later in the order, but these do not count as visits.

*Example 1:*\
Input: points = [[1,1],[3,4],[-1,0]]\
Output: 7\
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]\
Time from [1,1] to [3,4] = 3 seconds\
Time from [3,4] to [-1,0] = 4 seconds\
Total time = 7 seconds

*Example 2:*\
Input: points = [[3,2],[-2,2]]\
Output: 5


**Problem:**

From the list of Points, calculate minimum distance between First and Last Points (X1, Y1).

**Solution:**

If the first node is `10x` and `-5y` away. It's going to take exactly 10 steps from `0x` and `0y`, because you can only move `1x` at a time and the difference in `y` is made up by diagonal moves during the process of overcoming the difference `x`.

*[Trick]* So, Distance Between the two Co-ordinates *is maximum difference* of one Co-ordinate [Point]

**min_difference = max(abs(X2 - X1), abs(Y2 - Y1))**

Time O(n) : Space O(1)


**✅ Scenarios Where This Trick Works:**

This works **under a specific set of movement rules**, often seen in grid-based problems — like in chessboard-like movement.

You're allowed to move:
1. **One unit in the X direction** (left or right)
2. **One unit in the Y direction** (up or down)
3. **Or both at the same time**, i.e., a diagonal move (which changes X and Y both by ±1)

This is called **Chebyshev distance**, and it's common in pathfinding problems where diagonal movement costs the same as straight movement.


**Explanation:**

**🔍 Why It Works: Intuition**

Let's say you're at point (X1, Y1) and you want to go to (X2, Y2). The absolute differences are:


**dx = |X2 - X1|, dy = |Y2 - Y1|**

Now, imagine walking:

- You can reduce both **dx and dy** by doing **diagonal moves**.

- Once either dx or dy becomes 0, you do **straight moves** in the remaining direction.

So, in **one diagonal move**, you fix **1 unit in both X and Y directions**.

Hence:

- You can do **min(dx, dy)** diagonal moves.

- You then need **|dx - dy|** more moves in the dominant direction (X or Y).

So total moves =

- **min(dx,dy) (diagonal) + |dx-dy| (straight) = max(dx, dy)**

That's why:

- **Minimum distance= max(|X2-X1|, |Y2-Y1|)**

**🧠 Example:**

From (0, 0) to (4, 2):

**dx = 4**, **dy = 2**

You do 2 diagonal moves -> now at (2, 2)\
Still need 2 more moves in X -> now at (4, 2)\
Total = 4 moves = max(4, 2)

**✅ This Trick Works For:**
- Grid-based movement
- Diagonal movement allowed and costs same as orthogonal
- Chess King moves, for example


**Code Solution**
```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minDistance = 0
        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()
            minDistance += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2
        
        return minDistance
```


---
### 5. Spiral Matrix [54]

Given an m x n matrix, return all elements of the matrix in spiral order.

*Example 1:*\
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]\
Output: [1,2,3,6,9,8,7,4,5]

*Example 2:*\
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

**Code Solution**
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:

            # Step 1: Add the Top Row
            result += matrix.pop(0)

            # Step 2: Go Down / Add last elements
            if matrix and matrix[0]: # matrix[0] is to check wheather the x is not empty
                for x in matrix:
                    result.append(x.pop()) # you can do {if (row): result.append(x.pop())}; instead of matrix[0]
            
            # Step 3: Add the Last Row
            if matrix:
                result += matrix.pop()[::-1]

            # Step 4: Climb Up and Add first elements
            if matrix and matrix[0]:
                for x in matrix[::-1]:
                    result.append(x.pop(0))

        return result

        result = []
```


---
### 6. Number of Islands [200] {*BFS*}

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.\
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

*Example 1:*\
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

*Example 2:*\
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

**Problem:**

Given a 2D m * n grid, where 1 is land and 0 is water, return the number of islands

**Solution:**

It's Breath-First-Search Problem
- Traverse Level by Level
- Left Side Smaller Number, Right Side Larger Number

Iterate through problem and perform dfs or bfs search finding a '1' to mark neighbour as visited, and complete the island.\
Visit each cell once during intial iteration and potentially twice when exploring BFS in each direction `[4 - up down left right no_diagonals]` and we do this for M * N vertices, O(4 * m * n) * O(M * N).\
It might help to think of worst case senerio - matrix is all '1', so we have to visit every cell and explore every adjecent cell.\
For Space it could be stack/queue the entire grid if it is all 1s.

*Time & Space -> O(m * n)*

**✅ Scenarios Where This Trick Works**

| ✅ Works Well When...                         | ❌ Doesn't Work When...                          |
| -------------------------------------------- | ----------------------------------------------- |
| Finding connected regions (grids/graphs)     | Graph is weighted (use Dijkstra instead)        |
| Grid traversal / flood fill / clustering     | Diagonal connections needed (not included)      |
| Counting islands, lakes, provinces, clusters | You need optimal or shortest paths with weights |
| Any scenario with 4-directional connectivity | Problem requires topological sort or cycles     |


- A *deque (pronounced "deck")* is a data structure that allows elements to be added or removed from both the front and the rear, similar to a queue but with more flexibility, Act as [FIFO (queue)]/[LIFO (Stack)].

**Code Solution**
- Iterative Approach [BFS]
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0

        def bfs(r, c):
            que = deque()
            visitedPlace.add((r, c))
            que.append((r, c))

            while que:
                x, y = que.popleft()

                for dirx, diry in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    cellx = x + dirx
                    celly = y + diry

                    if cellx >= 0 and celly >= 0 and (cellx, celly) not in visitedPlace and cellx < len(grid) and celly < len(grid[0]) and grid[cellx][celly] == '1':
                        que.append((cellx, celly))
                        visitedPlace.add((cellx, celly))

        

        visitedPlace = set() # To avoid duplicate entries
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visitedPlace and grid[r][c] == '1':
                    bfs(r, c) # Mark Visited
                    count += 1 # Increase Island Count

        return count
```

- Recursive Approach [Faster] [DFS]
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0

        def bfs(r, c):
            # Recursive Approach
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'): return

            grid[r][c] = '0' # Mark Visited or Sink Island

            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c) # Mark Sink [Visited]
                    count += 1 # Increase Island Count

        return count
```


---
---
### **About DSF and BFS**

✅ **DFS (Depth-First Search)**

- For BFS Queue is used [Iterative version is Good and easy] [Level-Wise]
- For DFS Stack is user [Recursive version is Good and easy] [One-Sided]

| Style         | Mechanism                   | Why it's used                                                      |
| ------------- | --------------------------- | ------------------------------------------------------------------ |
| **Recursive** | Function call stack         | Natural, clean, and easy to write (especially in Python)           |
| **Iterative** | Manual stack (`stack = []`) | Needed when recursion depth is too large (e.g., huge grids/graphs) |

➡️ **Recursive DFS is usually simpler and faster** in Python unless stack depth becomes a problem.

---

✅ **BFS (Breadth-First Search)**

| Style              | Mechanism                   | Why it's used                                              |
| ------------------ | --------------------------- | ---------------------------------------------------------- |
| **Iterative only** | Queue (`collections.deque`) | Required to explore nodes **level-by-level** in FIFO order |

➡️ **BFS doesn't make sense recursively** because **recursion is naturally LIFO**, but BFS requires FIFO order.

---

🔁 **Summary of Your Insight**

| Algorithm | Preferred Method                                           | Data Structure                             |
| --------- | ---------------------------------------------------------- | ------------------------------------------ |
| **DFS**   | ✅ Recursive (easy), 🟡 Iterative (safe for deep recursion) | Stack (explicit or implicit via recursion) |
| **BFS**   | ✅ Iterative only (queue-based)                             | Queue (`deque`)                            |


🎯 **Bonus Tip:**

If you're doing:

* **Pathfinding / Shortest Path (unweighted graphs)** → Use **BFS**
* **Exploring all connected components / Islands (clustering)** → Use **DFS** or **BFS**
* **Maze solving (all paths)** → DFS is usually cleaner


---
---
### 7. Best Time to Buy and Sell Stock [121] {*Two-Pointer*}

You are given an array prices where prices[i] is the price of a given stock on the ith day.\
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

*Example 1:*\
Input: prices = [7,1,5,3,6,4]\
Output: 5

*Example 2:*\
Input: prices = [7,6,4,3,1]\
Output: 0

**Explanation:**

Its called `Greedy Method` operates on `accepting best option now`
- The problem can be solved by making `locally optimal choices` that lead to `global optimality`.
- You can prove (or guess) that choosing the best now will always work.

Move to next `Lower Price compared to current` as you have already calculated `All the previous maxProfits`\
And you are `comparing that previous maxProfits with latest one` to get new `maxProfit`

**Code Solution**
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        maxPrice = 0
        x, y = 0, 1

        # [6, 20, 5, 1, 1, 9]
        while y < len(prices):
            if prices[x] < prices[y]:
                maxPrice = max(maxPrice, prices[y] - prices[x])

            else:
                x = y # update buy day to new lower price

            y += 1

        return maxPrice

# BrutForce
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        maxProfit = max(maxProfit, prices[j] - prices[i])
```


---
---

### 🧠 Final Rule of Thumb:

| Goal / Pattern                  | Strategy         |
| ------------------------------- | ---------------- |
| Make best decision now          | Greedy           |
| Work with sorted or linear data | Two Pointers     |
| Work with substrings/subarrays  | Sliding Window   |
| Need to explore all choices     | DFS/Backtracking |
| Need to reuse solutions         | DP               |


---
---
### 8. Square Of Sorted Arrays [977]

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

*Example 1:*\
Input: nums = [-4,-1,0,3,10]\
Output: [0,1,9,16,100]

*Example 2:*\
Input: nums = [-7,-3,2,3,11]\
Output: [4,9,9,49,121]

**Explanation:**
Square Root of  negative number == to square root of positive number\
`-4^2` == `4^2` -> 16

**Code Solution**
```python
# BrutForce
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num ** 2 for num in nums]
        nums.sort() # O(n log n)

        return nums

# O(n) Solution with Higher Space Complexity
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Used Merge Sort Algo

        # Check if num exist
        if not nums: return nums

        # Check if no-negative number [No Sorting Needed]
        if nums[0] > 0: return [num ** 2 for num in nums]

        # Split after negative number
        m = len(nums) - 1
        for i in range(len(nums)):
            if (nums[i] >= 0):
                m = i
                break

        # Creating negative number list with square
        nL = [num ** 2 for num in nums[:m][::-1]]
        pL = [num ** 2 for num in nums[m:]]
        result = []

        # Merge the lists
        x = 0
        y = 0

        while x < len(nL) and y < len(pL):
            if (nL[x] > pL[y]):
                result.append(pL[y])
                y += 1

            else:
                result.append(nL[x])
                x += 1
        
        if (x < len(nL)): result += nL[x:]
        if (y < len(pL)): result += pL[y:]

        return result

# O(n) Solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n) Solution
        x = 0
        y = len(nums) - 1
        result = []

        while x <= y:
            sqr = 0
            if (abs(nums[x]) > abs(nums[y])):
                sqr = nums[x]
                x += 1
            else:
                sqr = nums[y]
                y -= 1

            result.insert(0, sqr ** 2)
        
        return result
```


---
### 9. 3Sum [15]

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

*Example 1:*\
Input: nums = [-1,0,1,2,-1,-4]\
Output: [[-1,-1,2],[-1,0,1]]

*Example 2:*\
Input: nums = [0,1,1]\
Output: []

**Problem:**\
Given an array of ints, return the list of triplets which add to 0, can only use same int twice if in list is twice.

**Solution:**\
Two Pointer, Sort and iterate through list for first value in triplet. Use two pointers, moving left and right to find 0

`Sorting the array first`
- This allows us to use two-pointers efficiently for the inner part of the problem.
- Also helps to easily skip duplicates, which is key to avoiding repeated triplets in the result.
- Why sort the array?
    - To use two-pointer efficiently and handle duplicates easily.
- Why do we skip duplicate nums[i]?
    - To avoid generating the same triplets again.
- How can one nums[i] produce multiple triplets?
    - Because the two-pointer search finds all pairs that sum with nums[i] to make zero -> including cases with duplicate values.

**Code Solution**
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Sort to find duplications easily
        nums.sort()

        # If no negative numbers
        if nums[0] > 0: return []

        for i, val in enumerate(nums):
            # Avoid duplicate results [As previous value is already evaluated]
            if i > 0 and val == nums[i - 1]: continue

            # Pointer to find remaining 2 sums
            x = i + 1
            y = len(nums) - 1

            while x < y:
                sum = val + nums[x] + nums[y]

                if sum > 0: y -= 1
                elif sum < 0: x += 1
                else:
                    result.append([val, nums[x], nums[y]])
                    x += 1

                    # remove duplicate values to avoid duplicate triplets
                    while x < y and nums[x] == nums[x - 1]: x += 1

        return result
```


---
---
### ⚠️ When to Sort in a Problem
Use sorting when:
- You need to compare elements in a certain order (e.g., Two-Sum variants, Intervals, Greedy decisions).
- You want to apply two-pointer or sliding window approaches.
- You want to remove duplicates or group similar elements.

Don't sort:
- When the original order of elements matters (e.g., for subsequences, permutations).
- Or if the cost of sorting is too high and not justified.

### 🧠 Key Benefits of Sorting:

| Purpose                   | Why it helps                                                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Two-pointer technique** | Only works efficiently on sorted data                                                                                       |
| **Skip duplicates**       | Consecutive duplicates are easy to spot                                                                                     |
| **Early pruning**         | Once the current number is > 0, we can break early (because nums\[x] + nums\[y] + nums\[z] > 0 will always hold after that) (So the smallest possible sum = 1 + 1 + 1 = 3 > 0) |


---
---
###  10. Missing Number [268]
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

Notice that the solution set must not contain duplicate triplets.

*Example 1:*\
Input: nums = [3,0,1]\
Output: 2

*Example 2:*\
Input: nums = [0,1]\
Output: 2

**Solution:**\
The Sum of first `n` Natural Numbers - Sum of array elements => Missing number.\

$$
Sum = \frac{n(n + 1)}{2}
$$


**Code Solution**
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
```


---
###  11. Find All Numbers Disappeared in an Array [448]
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.


*Example 1:*\
Input: nums = [4,3,2,7,8,2,3,1]\
Output: [5,6]

*Example 2:*\
Input: nums = [1,1]\
Output: [2]


**Code Solution**
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = set(nums)

        result = []
        for num in range(1, len(nums) + 1):
            if num not in temp: result.append(num)
        

        return result
```


---
###  12. How Many Numbers Are Smaller Than the Current Number [1365]
Given the array nums, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` and `nums[j] < nums[i]`.\
Return the answer in an array.

*Example 1:*\
Input: nums = [8,1,2,2,3]\
Output: [4,0,1,1,3]\
Explanation:\
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). \
For nums[1]=1 does not exist any smaller number than it.\
For nums[2]=2 there exist one smaller number than it (1).\ 
For nums[3]=2 there exist one smaller number than it (1). \
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

*Example 2:*\
Input: nums = [6,5,4,8]\
Output: [2,1,0,3]

*Example 3:*\
Input: nums = [7,7,7,7]\
Output: [0,0,0,0]

**Solution:**\
- Sort the array, so index of the element will be count of the lower elements as well
- create dictionary and also add not in check to avoid value overriding
- finally returning the list

**Code Solution**
```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedList = sorted(nums)
        numberMapping = {}

        for index, value in enumerate(sortedList):
            if value not in numberMapping:
                numberMapping[value] = index
        
        result = []
        for value in nums:
            result.append(numberMapping[value])

        return result
```


---
###  13. Longest Mountain in the Array [845]
You may recall that an array arr is a mountain array if and only if:
- `arr.length >= 3`
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
    - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
    - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

*Example 1:*\
Input: arr = [2,1,4,7,3,2,5]\
Output: 5\
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

*Example 2:*\
Input: arr = [2,2,2]\
Output: 0\
Explanation: There is no mountain.

*Example 3:*\
Input: arr = [0,1,2,3,4,5,4,3,2,1,0]\
Output: 11\

**Solution:**\
- Find the Peak and Than Slide from both slides

**Code Solution**
```python
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # No Mountain Array
        if len(arr) < 3: return 0

        result = 0

        # Find the Peak and Slide on both sides from peak
        for i in range(1, len(arr) - 1):

            # It's the Peak [Highest Value]
            if arr[i - 1] < arr[i] > arr[i + 1]:

                # Slide Left:
                x = i
                while x > 0:
                    if arr[x] > arr[x - 1]: x -= 1
                    else: break

                # Slide Right:   
                y = i
                while y < len(arr) - 1:
                    if arr[y] > arr[y + 1]: y += 1
                    else: break

                result = max(result, y - x + 1)

        return result
```


---
###  14. Contains Duplicate II [219]  {*Sliding-Window*}
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

*Example 1:*\
Input: nums = [1,2,3,1], k = 3\
Output: true

*Example 2:*\
Input: nums = [1,0,1,1], k = 1\
Output: true

*Example 3:*\
Input: nums = [1,2,3,1,2,3], k = 2\
Output: false

**Solution:**\
- Maintain the Window of `k` as `abs(i - j) <= k`, if we maintain the window of `k` then `|i - j|, |(i + 1) - (j + 1)|` ....

**Code Solution**
```python
# Using Set
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for index, value in enumerate(nums):
            if value in seen: return True

            seen.add(value)
            # Maintain Window Size [K is Window Size]
            if len(seen) > k:
                # [index[4] - k[4] => 0[Remove]]
                seen.remove(nums[index - k])
        
        return False

# Using Distionary
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dist = {}

        for index, value in enumerate(nums):
            if value in dist and (index - dist[value] <= k): return True
            dist[value] = index
            
        return False
```

---
###  15. Minimum Absolute Difference [1200]
Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows
- `a, b` are from `arr`
- `a < b`
- `b - a` equals to the minimum absolute difference of any two elements in `arr`

*Example 1:*\
Input: arr = [4,2,1,3]\
Output: [[1,2],[2,3],[3,4]]\
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

*Example 2:*\
Input: arr = [1,3,6,10,15]\
Output: [[1,3]]

*Example 3:*\
Input: arr = [3,8,-10,23,19,-4,-14,27]\
Output: [[-14,-10],[19,23],[23,27]]

**Explanation:**\
- The `minimum absolute difference` is a minimum difference between two consecutive elements in the sorted array.

**Code Solution**
```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort first to find minimum absolute difference
        arr.sort()

        # Find minimum absolute difference
        minDiff = float('inf')
        for i in range(1, len(arr)):
            minDiff = min(minDiff, arr[i] - arr[i - 1])

        # Finding Pairs using window of pair
        result = []
        for i in range(1, len(arr)):
            if (arr[i] - arr[i - 1]) <= minDiff:
                result.append([arr[i - 1], arr[i]])

        return result
```

---
---
### 🧠 Python Negative and Positive Infinities
`float('inf') > 1000000000000` evaluates to `True`

- positive_infinity = float('inf')
- negative_infinity = float('-inf')
---
---