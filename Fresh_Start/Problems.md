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
Visit each cell once during intial iteration and potentially twice when exploring BFS in each direction `[4 -> up down left right no_diagonals]` and we do this for M * N vertices, O(4 * m * n) * O(M * N).\
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

        visitedPlace = set() # To avoid duplicate entries
        count = 0

        def bfs(r, c):
            que = deque()
            visitedPlace.add((r, c))
            que.append((r, c))

            while que: # Use this while loop is if conditions atlast to make is recersive [346, 347 line]
                x, y = que.popleft()

                for dirx, diry in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    cellx = x + dirx
                    celly = y + diry

                    if cellx >= 0 and celly >= 0 and (cellx, celly) not in visitedPlace and cellx < len(grid) and celly < len(grid[0]) and grid[cellx][celly] == '1':
                        que.append((cellx, celly))
                        visitedPlace.add((cellx, celly))

        

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

        def dfs(r, c):
            # Recursive Approach
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'): return

            grid[r][c] = '0' # Mark Visited or Sink Island

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c) # Mark Sink [Visited]
                    count += 1 # Increase Island Count

        return count
```


---
---
### **About DSF and BFS**

✅ **DFS (Depth-First Search)**

- For BFS Queue is used [Iterative version is Good and easy] [Level-Wise] [FIFO]
- For DFS Stack is used [Recursive version is Good and easy] [One-Sided] [LIFO]

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
| **BFS**   | ✅ Iterative only (queue-based)                             | Queue (`deque`) [Because will give all nodes at the same level]                           |


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

        # Sort to avoid duplications easily
        nums.sort()

        # If no negative numbers
        if nums[0] > 0: return []

        for i, val in enumerate(nums):
            # Avoid duplicate results [As same value is already evaluated]
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

                    # Avoid duplicate results [As same value is already evaluated]
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
###  11. How Many Numbers Are Smaller Than the Current Number [1365]
Given the array nums, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` and `nums[j] < nums[i]`.\
Return the answer in an array.

*Example 1:*\
Input: nums = [8,1,2,2,3]\
Output: [4,0,1,1,3]\
Explanation:\
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).\
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
        sortedList = sorted(nums) # Creates new list [nums.sort() modifies original list]
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
###  12. Longest Mountain in the Array [845]
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
Output: 11

**Solution:**
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
###  13. Contains Duplicate II [219]  {*Sliding-Window*}
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

**Solution:**
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
###  14. Minimum Absolute Difference [1200]
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
- The `minimum absolute difference` is a minimum difference between `two consecutive elements` in the `sorted array`.

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

- positive_infinity = **float('inf')**
- negative_infinity = **float('-inf')**


---
---
###  15. Minimum Size Subarray Sum [209]
Given an array of positive integers `nums` and a positive integer `target`, return the `minimal length` of a `subarray` whose sum is `greater than or equal to target`. If there is no such subarray, return 0 instead..

*Example 1:*\
Input: target = 7, nums = [2,3,1,2,4,3]\
Output: 2\
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

*Example 2:*\
Input: target = 4, nums = [1,4,4]\
Output: 1

*Example 3:*\
Input: target = 11, nums = [1,1,1,1,1,1,1,1]\
Output: 0

**Code Solution**
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        x = 0

        total = 0
        result = float('inf')

        for y in range(len(nums)):
            total += nums[y]

            while total >= target:
                result = min(result, y - x + 1)

                total -= nums[x]
                x += 1

        if (result == float('inf')): return 0
        return result
```


---
###  16. Contains Duplicate II [219]  {*Bit Manipulation*}
Given a `non-empty` array of integers `nums`, every element appears twice except for one. Find that single one.\
You must implement a solution with a linear runtime complexity and use only constant extra space.

*Example 1:*\
Input: [2,2,1]\
Output: 1
```
nums 2
xor 2
nums 2
xor 0
nums 1
xor 1
```

*Example 2:*\
Input: [4,1,2,1,2]\
Output: 4
```
nums 4
xor 4
nums 1
xor 5
nums 2
xor 7
nums 1
xor 6
nums 2
xor 4
```

*Example 3:*\
Input: [1]\
Output: 1
```
nums 1
xor 1
```

**Code Solution**
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for i in nums:
            print('nums', i)
            xor ^= i
            print('xor', xor)

        return xor
```

---
---
### 🧠 Bit Manipulation (Quick Reference)

| Operator | Name        | Meaning                  | Example  | Result |
| -------- | ----------- | ------------------------ | -------- | ------ |
| `&`      | AND         | 1 if **both bits** are 1 | `5 & 3`  | `1`    |
| `\|`     | OR          | 1 if **any bit** is 1    | `5 \| 3` | `7`    |
| `^`      | XOR         | 1 if **bits differ**     | `5 ^ 3`  | `6`    |
| `~`      | NOT         | Inverts all bits         | `~5`     | `-6`   |
| `<<`     | Left Shift  | Shifts bits left (×2)    | `5 << 1` | `10`   |
| `>>`     | Right Shift | Shifts bits right (÷2)   | `5 >> 1` | `2`    |


---
---
###  17. Coin Change [322]  {*Dynamic Programing [Reusing the calculated subprogramming `Memoization`]*}
You are given an integer array `coins` representing coins of different denominations and an integer amount representing a total `amount` of money.\
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.\
You may assume that you have an infinite number of each kind of coin.

*Example 1:*\
Input: coins = [1,2,5], amount = 11\
Output: 3\
Explanation: 11 = 5 + 5 + 1


*Example 2:*\
Input: coins = [2], amount = 3\
Output: -1


*Example 3:*\
Input: coins = [1], amount = 0\
Output: 0

**Explanation:**\
- dp[i] = minimum number of `coins` needed to make `amount i`.
- dp[i] = best solution of smaller problem + cost of current choice

#### 🎯 Real-Life Analogy 💰

You want to pay ₹10
You give a ₹5 note

You already used 1 note

Now you must find the minimum notes to pay the remaining ₹5

👉 Total notes = 1 + best way to pay ₹5 {1 + dp[i - c]}


**Code Solution**
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):

            for c in coins:
                if (i - c) >= 0:
                    
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount] if (dp[amount] != amount + 1) else -1 
        # amount + 1 acts like ∞ (infinity) Check, which means no combination exists
        # coins = [2], amount: 3
```

#### 💰 Coin Change — Visual Dry Run
Example
```
coins = [1, 3, 4]
amount = 6
```

##### 🧠 What dp[i] Means

- Minimum number of coins needed to make amount i

##### 🧱 Step 1: Initialize DP Table

We use ∞ = amount + 1 = 7

| Amount (i) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ---------- | - | - | - | - | - | - | - |
| dp[i]      | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |


##### 🔁 Step 2: Fill the DP Table

We go left → right (small → big)

🔹 i = 1

Try each coin:

coin 1 → 1 + dp[0] = 1

coin 3 → ❌ too big

coin 4 → ❌ too big

**| dp[1] = 1 |**

🔹 i = 2

coin 1 → 1 + dp[1] = 2

coin 3 → ❌

coin 4 → ❌

**| dp[2] = 2 |**

🔹 i = 3

coin 1 → 1 + dp[2] = 3

coin 3 → 1 + dp[0] = 1 ✅

coin 4 → ❌

**| dp[3] = 1 |**

🔹 i = 4

coin 1 → 1 + dp[3] = 2

coin 3 → 1 + dp[1] = 2

coin 4 → 1 + dp[0] = 1 ✅

**| dp[4] = 1 |**

🔹 i = 5

coin 1 → 1 + dp[4] = 2

coin 3 → 1 + dp[2] = 3

coin 4 → 1 + dp[1] = 2

**| dp[5] = 2 |**

🔹 i = 6

coin 1 → 1 + dp[5] = 3

coin 3 → 1 + dp[3] = 2 ✅

coin 4 → 1 + dp[2] = 3

**| dp[6] = 2 |**

##### ✅ Final DP Table

| Amount | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ------ | - | - | - | - | - | - | - |
| dp     | 0 | 1 | 2 | 1 | 1 | 2 | 2 |

- 🎯 Answer: `dp[6] = 2`

- (3 + 3)

---
---
### 🌳 BFS & DFS with DP — Quick Notes
🧠 Core Idea
- DFS / BFS → explore states
- DP (Memo / Visited) → avoid recomputing states
- Explore first, remember results later

## 1️⃣ DFS + DP (⭐ MOST COMMON & RECOMMENDED)
✅ Use this when:
- You are building combinations step by step
- Choices depend on previous choices
- You want all combinations or to check feasibility
- The state can repeat

Why DFS?
- Natural include / exclude structure
- Uses recursion stack instead of a queue
- Easy to memoize states

## 2️⃣ BFS + DP (Less common, but useful)
✅ Use this when:
- You want the shortest path
- Levels matter (step-by-step depth)
- Each step has equal cost

Why BFS?
- Explores level by level
- Guarantees minimum steps

## 🔑 Golden Summary
- 🔥 Combinations → DFS
- 🔥 Optimization → DP
- 🔥 Minimum steps → BFS


---
---
###  18. Climbing Stairs [70]
You are climbing a staircase. It takes `n` steps to reach the top.\
Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

*Example 1:*\
Input: n = 2\
Output: 2\
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


*Example 2:*\
Input: n = 3\
Output: 3\
Explanation: There are three ways to climb to the top.\
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


**Code Solution**
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
```


---
###  19. Maximum Subarray [53]
Given an integer array `nums`, find the `subarray` with the largest sum, and return its sum.

*Example 1:*\
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\
Output: 6\
Explanation: The subarray [4,-1,2,1] has the largest sum 6.


*Example 2:*\
Input: nums = [1]\
Output: 1\
Explanation: The subarray [1] has the largest sum 1.

*Example 3:*\
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


**Code Solution**
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = float('-inf')

        for n in nums:
            if currentSum < 0: currentSum = 0
            
            currentSum += n
            maxSum = max(currentSum, maxSum)

        return maxSum
```


---
###  20. Counting Bits [338]

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`'s in the binary representation of `i`.

**Explanation:**
- basically you have to find the number of `1`'s to create the `i`.

*Example 1:*\
Input: n = 2\
Output: [0,1,1]\
Explanation:\
0 --> 0\
1 --> 1\
2 --> 10


*Example 2:*\
Input: n = 5\
Output: [0,1,1,2,1,2]\
Explanation:\
0 --> 0\
1 --> 1\
2 --> 10\
3 --> 11\
4 --> 100\
5 --> 101

*Example 3:*\
Input: n = 3\
Output: [0,1,1,2]


**Solution:**
- basically you have to find the number of `1`'s to create the `i`.
- You can see the repeating pattern
- Taking the previous value and adding one to it gives the answer, as when the offset [power] changes the 1's reset and starts increasing again.

![alt text](image.png)


**Code Solution**
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp
```


---
### 21. Range Sum Query - Immutable [303]

Given an integer array nums, handle multiple queries of the following type:\
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.\
Implement the `NumArray` class:
- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` inclusive (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).


*Example 1:*\
Input:\
["NumArray", "sumRange", "sumRange", "sumRange"]\
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output:\
[null, 1, -1, -3]

Explanation:\
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);\
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1\
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1\
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3\


**Code Solution**
```python
class NumArray:
    num = []
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


# --- Or Using Prefix Sum -----
class NumArray:
    num = []
    def __init__(self, nums: List[int]):
        self.prefixSum = [0]
        for num in nums: self.prefixSum.append(self.prefixSum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]

# nums[-1] -> Last Element
# Why right + 1 -> First element is zero
```

---
---
### Back Tracking

BackTracking is a problem - solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end.

![alt text](image-1.png)

#### Permutations:
- The number of ways to arrange things
- order matters

#### Combinations:
- The number of ways to choose things
- order doesn't matter


---
---
### 22. Last Letter Permutation [784]  {*BackTracking*}
Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string.\
Return a list of all possible strings we could create. Return the output in `any order`.

*Example 1:*\
Input: s = "a1b2"\
Output: ["a1b2","a1B2","A1b2","A1B2"]


*Example 2:*\
Input: s = "3z4"\
Output: ["3z4","3Z4"]


**Code Solution**
```python
# Iterative Approach
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # As '' is present than it will iterate once and a in added to temp
        output = ['']

        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o + c.lower())
                    tmp.append(o + c.upper())
            else:
                for o in output:
                    tmp.append(o + c)

            output = tmp

        return output

# Recursion
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtracking(sub = '', i = 0):
            if (len(sub) == len(s)):
                res.append(sub)
                return

            if s[i].isalpha():
                backtracking(sub + s[i].swapcase(), i + 1)
            backtracking(sub + s[i], i + 1)

        backtacking()
        return res
   
```

**Dry Run Iterative**

*Input: a1b2*

*Output:*
```
['']
[[A], [a]] = o
[[A1], [a1]] = o
[[A1B], [a1b]] = o
...
```

---
### 23. Subsets [78]
Given an integer array `nums` of unique elements, return all possible `subsets` (the power set {all combinations including '[]'}).\
The solution set `must not` contain duplicate subsets. Return the solution in `any order`.

*Example 1:*\
Input: nums = [1,2,3]\
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

*Example 2:*\
Input: nums = [0]\
Output: [[],[0]]


**Code Solution**
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtracking(start, path):

            # path[:] creates a new list
            # Otherwise all references would change later
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path) # Continue to build subset from next element
                path.pop()

        result = []
        backtracking(0, [])
        return result
```

**Decision Tree**

*For*
```
nums = [1,2,3]
```

*Tree*
```
[]
├── [1]
│   ├── [1,2]
│   │   ├── [1,2,3]
│   │   └── backtrack
│   ├── [1,3]
│   └── backtrack
├── [2]
│   ├── [2,3]
│   └── backtrack
├── [3]
└── backtrack
```

*Call Stack*
```
backtracking(0, [])
 └── backtracking(1, [1])
      └── backtracking(2, [1,2])
           └── backtracking(3, [1,2,3])
      └── backtracking(3, [1,3])
 └── backtracking(2, [2])
      └── backtracking(3, [2,3])
 └── backtracking(3, [3])
```

*Time & Space Complexity*
```
Let n = len(nums)

Number of subsets:
2^n

Time:  O(2^n)
Space: O(n) recursion depth
```

**Core Backtracking Template {This Pattern appears everywhere}**
```python
def backtrack(start, path):
    save(path)

    for i in range(start, n):
        choose(i)
        backtrack(i+1, path)
        unchoose(i)

#
# You are walking a tree of decisions, and at every node you record the path so far, then try all possible next steps, and undo after returning.
```


---
### 24. Combinations [77]
Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.\
You may return the answer in any order.

*Example 1:*\
Input: n = 4, k = 2\
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]\
Explanation: There are 4 choose 2 = 6 total combinations.\
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

*Example 2:*\
Input: n = 1, k = 1\
Output: [[1]]\
Explanation: There is 1 choose 1 = 1 total combination.


**Code Solution**
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backTracking(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backTracking(i + 1, path)
                path.pop()

        result = []
        backTracking(1, []) # Because Range starts with zero
        return result
```


---
### 25. Permutations [46]
Given an array `nums` of distinct integers, return all the possible `permutations`. You can return the answer in `any order`.

*Example 1:*\
Input: nums = [1,2,3]\
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

*Example 2:*\
Input: nums = [0,1]\
Output: [[0,1],[1,0]]

*Example 3:*\
Input: nums = [1]\
Output: [[1]]

**Code Solution**
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTracking(start, end):
            if start == end:
                result.append(nums[:])
                return

            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backTracking(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start] # reversing the swap

        result = []
        backTracking(0, []) 
        return result
```

---
---
### Template (Combinations / Subsets)

```python
def backtrack(start, path):
    if condition:
        save(path)
        return

    for i in range(start, n):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

### Template (Permutations - visited array)
```python
def backtrack(path):
    if len(path) == n:
        save(path)
        return

    for i in range(n):
        if used[i]: continue
        used[i] = True
        path.append(nums[i])
        backtrack(path)
        path.pop()
        used[i] = False
```

### OR swap-based:
```python
def backtrack(start):
    if start == n:
        save(nums)
        return

    for i in range(start, n):
        swap(start, i)
        backtrack(start+1)
        swap back
```


---
---
### 26. Middle of the Linked List [876] {*Linked Lists*}
Given the `head` of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return `the second middle` node.

*Example 1:*\
Input: head = [1,2,3,4,5]\
Output: [3,4,5]\
Explanation: The middle node of the list is node 3.

*Example 2:*\
Input: head = [1,2,3,4,5,6]\
Output: [4,5,6]\
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.



**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

---
---
### Fast & Slow Pointer (Tortoise & Hare).

#### The Core Idea (in one line)
- One pointer moves 1 step, another moves 2 steps.
- When the fast one reaches the end, the slow one is at the middle.

How this works for even and uneven lists
- For Uneven the slow pointer points after middle iteration as the condition is false after second iteration

![alt text](image-2.png)


---
---
### 27. Linked List Cycle [141]
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.\
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.\
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.\
*Note: pos = -1 => No Cycle*

*Example 1:*\
![alt text](image-3.png)

Input: head = [3,2,0,-4], pos = 1\
Output: true\
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

*Example 2:*\
![alt text](image-4.png)

Input: head = [1,2], pos = 0\
Output: true\
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

*Example 3:*\
![alt text](image-5.png)

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


**Explanation:**\
As If their is cycle both will eventually will be same

**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False
```


### 27. Reverse Linked List [206]
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

*Example 1:*\
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

*Example 2:*\
Input: head = [1,2]
Output: [2,1]

*Example 3:*\
Input: head = []
Output: []


**Explanation:**\
- Changing the Current Node Previous and Next at a Time and repeating the Process
- prevNode => None <- CurrenNode <- nextNode <= PrevNode [Update the PrevNode]

**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode

            prevNode = currentNode
            currentNode = nextNode

        return prevNode

# ------ Or -------

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None

        while head:
            next = head.next
            head.next = prevNode
            prevNode = head
            head = next

        return prevNode
```


---
### 28. Remove Linked List Elements [206]
Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

*Example 1:*\
Input: head = [1,2,6,3,4,5,6], val = 6\
Output: [1,2,3,4,5]

*Example 2:*\
Input: head = [], val = 1\
Output: []

*Example 3:*\
Input: head = [7,7,7,7], val = 7\
Output: []

**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prevNode = None
        currentNode = head

        while currentNode:
            if currentNode.val == val:
                if prevNode == None:
                    head = head.next
                    currentNode = head
                    continue
                else:
                    prevNode.next = currentNode.next
                    currentNode = prevNode

            prevNode = currentNode
            currentNode = currentNode.next

        return head

# ---- OR ----

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None

        curr = head

        # Next is used as we are assuming that first element might be val
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        if head.val == val: return head.next

        return head
```


---
### 29. Reverse Linked List II [92]
Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

*Example 1:*\
Input: head = [1,2,3,4,5], left = 2, right = 4\
Output: [1,4,3,2,5]

*Example 2:*\
Input: head = [1,2]\
Output: false

*Example 3:*\
Input: head = [1,1,2,1]\
Output: false

**Explanation Image**
![alt text](image-6.png)


**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummyHead = ListNode(-1, head)

        # Stage 1 [Updating CurrentNode to Left]
        leftPrev, currentNode = dummyHead, head
        for i in range(left - 1):
            leftPrev, currentNode = currentNode, currentNode.next

        # Stage 2 [Reversing from Left to Right]
        prev = None
        for i in range(right - left + 1):
            nextPointer = currentNode.next
            currentNode.next = prev
            prev, currentNode = currentNode, nextPointer

        # Stage 3 [Arranging the Left Pointer and Right Pointer]
        leftPrev.next.next = currentNode
        leftPrev.next = prev
        
        return dummyHead.next
```


---
### 30. Palindrome Linked List [234]
Given the `head` of a singly linked list, return `true` if it is a `palindrome` or fals`e otherwise.

*Example 1:*\
Input: head = [1,2,2,1]\
Output: true

*Example 2:*\
Input: head = [5], left = 1, right = 1
Output: [5]

**Explanation Image**
![alt text](image-7.png)


**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Stage 1: [Find Middle]
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Stage 2: [Reverse the Right Side of List]
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev

            prev = slow
            slow = nextNode

        # Stage 3: [Check Palindrome with two pointers]
        left = head
        right = prev

        while right: # [As left is connect to the rightSide we haven't unlinked it]
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
```


---
### 31. Merge Two Sorted Lists [21]
You are given the heads of two sorted linked lists `list1` and `list2`.\
Merge the two lists into one `sorted` list. The list should be made by splicing together the nodes of the first two lists.\
Return the head of the merged linked list.

*Example 1:*\
Input: list1 = [1,2,4], list2 = [1,3,4]\
Output: [1,1,2,3,4,4]

*Example 2:*\
Input: list1 = [], list2 = []\
Output: []

*Example 3:*\
Input: list1 = [], list2 = [0]\
Output: [0]

**Code Solution**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        finalResult = currentNode = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                currentNode.next = list1
                list1 = list1.next
                
            else:
                currentNode.next = list2
                list2 = list2.next

            currentNode = currentNode.next

        if list1: currentNode.next = list1
        elif list2: currentNode.next = list2

        return finalResult.next
```


---
### 32. Min Stack [155]
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

*Example 1:*\
Input:\
["MinStack","push","push","push","getMin","pop","top","getMin"]\
[[],[-2],[0],[-3],[],[],[],[]]\

Output:\
[null,null,null,null,-3,null,0,-2]

Explanation:\
MinStack minStack = new MinStack();\
minStack.push(-2);\
minStack.push(0);\
minStack.push(-3);\
minStack.getMin(); # return -3\
minStack.pop();\
minStack.top();    # return 0\
minStack.getMin(); # return -2

**Code Solution**
```python
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# --- MyCode getMin is O(n) -----
class MinStack:
    def __init__(self):
        self.valueList = []
        self.currentMin = float('inf')

    def push(self, val: int) -> None:
        self.valueList.append(val)
        self.currentMin = min(val, self.currentMin)

    def pop(self) -> None:
        self.valueList.pop() 

    def top(self) -> int:
        return self.valueList[-1]

    def getMin(self) -> int:
        return self.currentMin

#
class MinStack:
    def __init__(self):
        self.stack = []
        # Min stack just for keep track of minimum so far
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # For minstack, if val is less than minimum, append to top, else 
        val = min(val, self.minStack[-1] if self.minStack else val) # if esist minStack or val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

#
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            currentMin = val
        else:
            currentMin = min(val, self.stack[-1][1])

        self.stack.append((val, currentMin)) #[(-2, -2), (-3, -3)]

    def pop(self) -> None:
        self.stack.pop() # [(-2, -2)]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1] # -2, As -3 is Popped
```


---
### 33. Valid Parentheses [20]
Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

*Example 1:*\
Input: s = "()"\
Output: true

*Example 2:*\
Input: s = "()[]{}"\
Output: true

*Example 3:*\
Input: s = "(]"\
Output: false

*Example 4:*\
Input: s = "([])"\
Output: true

*Example 5:*\
Input: s = "([)]"\
Output: false

**Code Solution**
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')':'(', '}':'{', ']':'['}

        for element in s:
            if stack and (element in hashMap and stack[-1] == hashMap[element]):
                stack.pop()
            else:
                stack.append(element)

        return not stack

# ----- Or ------
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stk = []
        
        for ch in s:
            if ch in '([{':
                stk.append(ch)
                continue
            
            if not stk:
                return False
            
            brk = stk[-1]
            if (brk == '(' and ch == ')') or \
               (brk == '[' and ch == ']') or \
               (brk == '{' and ch == '}'):
                stk.pop()
            else:
                return False
        
        return len(stk) == 0
```


---
### 34. Evaluate Reverse Polish Notation [150]
You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.\
Evaluate the expression. Return an integer that represents the value of the expression.\

**Note** that:
- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

*Example 1:*\
Input: tokens = ["2","1","+","3","*"]\
Output: 9\
Explanation: ((2 + 1) * 3) = 9

*Example 2:*\
Input: tokens = ["4","13","5","/","+"]\
Output: 6\
Explanation: (4 + (13 / 5)) = 6

*Example 3:*\
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\
Output: 22\
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5\
= ((10 * (6 / (12 * -11))) + 17) + 5\
= ((10 * (6 / -132)) + 17) + 5\
= ((10 * 0) + 17) + 5\
= (0 + 17) + 5\
= 17 + 5\
= 22

**Code Solution:**
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:
            if num not in '+-*/':
                stack.append(int(num))
            else:
                x, y = stack.pop(), stack.pop()

                if num == '+':
                    stack.append(y + x)
                elif num == '*':
                    stack.append(y * x)
                elif num == '-':
                    stack.append(y - x)
                elif num == '/':
                    stack.append(int(y / x))

        return stack.pop()
```


---
### 35. Given a Stack of Integers sort them in ascending or decending Order.

```python
# It's Decending Order Code
def sortStack(stack):
    tmpStack = []

    while stack:
        num = stack.pop()

        while tmpStack and tempStack[-1] < num:
            stack.append(tmpStack.pop())

        tmpStack.append(num)

    return tmpStack
```


---
### 34. Implement Stack using Queues [225]
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:
- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

Notes:
- You must use `only` standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

*Example 1:*\
Input: ["MyStack", "push", "push", "top", "pop", "empty"]\
[[], [1], [2], [], [], []]

Output:\
[null, null, null, 2, 2, false]

Explanation:\
MyStack myStack = new MyStack();\
myStack.push(1);\
myStack.push(2);\
myStack.top();   # return 2\
myStack.pop();   # return 2\
myStack.empty(); # return False\

**Code Solution:**
```python
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # Let to Last Element to Come Front 
        # => [3, 1, 2] <- 2 will be automatically last element after poping 3
        # That's the reason we used -1 other it will be same list again after rotating
        for num in range(len(self.stack) - 1):
            self.push(self.stack.popleft())

        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```


---
### 35. Time Needed to Buy Tickets [2073]
There are `n` people in a line queuing to buy tickets, where the `0th` person is at the front of the line and the `(n - 1)th` person is at the back of the line.

You are given a 0-indexed integer array `tickets` of length `n` where the number of tickets that the ith person would like to buy is `tickets[i]`.

Each person takes `exactly 1 second` to buy a ticket. A person can only buy `1 ticket at a time` and has to go back to `the end` of the line (which happens `instantaneously`) in order to buy more tickets. If a person does not have any tickets left to buy, the person will `leave` the line.

Return the `time taken` for the person `initially` at position `k` (0-indexed) to finish buying tickets.


*Example 1:*\
Input: tickets = [5,1,1,1], k = 0\
Output: 8

*Example 2:*\
Input: tickets = [2,3,2], k = 2\
Output: 6


**Code Solution:**
```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0

        for i in range(len(tickets)):
            if i <= k: # Before K
                # seconds needed is equal to k
                res += min(tickets[i], tickets[k])
            else: # After K
                # seconds needed is (k - 1)
                res += min(tickets[i], tickets[k] - 1)

        return res
```


---
### 36. Reserve the Queue using Stack

**Code Solution:**
```python
def reverse_first_k_using_stack_in_queue(k, q):
    stack = []

    # put first k elements in stack
    for i in range(k):
        stack.append(q.popleft())

    # push the contents of the stack to the back of the queue
    # will be added in reverse due to stack LIFO
    while stack:
        q.append(stack.pop())
    
    # pop and push elements in queue
    # that should come after first k elements in queue
    for i in range(len(q) - k):
        q.append(q.popleft())

    return q

reverse_first_k_using_stack_in_queue(3, deque([1, 2, 3, 4, 5]))
# Output: [3, 2, 1, 4, 5]
```


---
### 37. Average of Levels in Binary Tree [637] {*Binary Tree*}
Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within `10^-5` of the actual answer will be accepted.


*Example 1:*\
![alt text](image-8.png)\
Input: root = [3,9,20,null,null,15,7]\
Output: [3.00000,14.50000,11.00000]

*Example 2:*\
![alt text](image-9.png)\
Input: root = [3,9,20,15,7]\
Output: [3.00000,14.50000,11.00000]


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root]) # len(que) => 1
        result = []

        while que:
            level = []
            # Works on the initial len, after adding doesn't work here, so stops at len => 1
            for x in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

            result.append(sum(level) / len(level))

        return result
```


---
### 38. Minimum Depth of Binary Tree [111]
Given a binary tree, find its minimum depth.\
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.\
Note: A leaf is a node with no children.


*Example 1:*\
![alt text](image-10.png)\
Input: root = [3,9,20,null,null,15,7]\
Output: 2

*Example 2:*\
Input: root = [2,null,3,null,4,null,5,null,6]\
Output: 5


**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        que = deque([root])
        level = 1
        depth = float('inf')

        while que:
            for x in range(len(que)):
                node = que.popleft()

                if (not node.left) and (not node.right): return level

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

            level += 1

        return level


# --------- Using only While loop -------------
def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0

    que = deque([(root, 1)])

    while que:
        node, level = que.popleft()

        if (not node.left) and (not node.right): return level

        if node.left: que.append((node.left, level + 1))
        if node.right: que.append((node.right, level + 1))

    return 0


# -------- Recursive [DFS] [Recursive uses stack as nature, so DFS by default] --------
def minDepth(self, root):
    if not root: return 0

    # If one side is missing, You must go through the existing side.
    if not root.left: return self.minDepth(root.right) + 1

    if not root.right: return self.minDepth(root.left) + 1

    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

```


---
### 39. Maximum Depth of Binary Tree [104]
Given the `root` of a binary tree, return its maximum depth.\
A binary tree's `maximum depth` is the number of nodes along the longest path from the root node down to the farthest leaf node.


*Example 1:*\
Input: root = [3,9,20,null,null,15,7]\
Output: 3

*Example 2:*\
Input: root = [1,null,2]\
Output: 2


**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # DFS
        # Go full Deep, and pop by adding 1
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# ---- Iterative BFS -------
def maxDepth(self, root):
    if not root: return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    return depth
```


---
### 40. Find Maximum Node in the Tree

**Code Solution:**
```python
def findMax(root: Optional[TreeNode]) -> int:
    if not root: return float('-inf')  # very small value

    left_max = findMax(root.left)
    right_max = findMax(root.right)

    return max(root.val, left_max, right_max)


# ------ Iterative ----------
def findMax(root):
    if not root: return float('-inf')

    queue = deque([root])
    maximum = root.val

    while queue:
        node = queue.popleft()
        maximum = max(maximum, node.val)

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return maximum
```


---
### 41. Binary Tree Level Order Traversal [102]
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


*Example 1:*\
![alt text](image-11.png)\
Input: root = [3,9,20,null,null,15,7]\
Output: [[3],[9,20],[15,7]]

*Example 2:*\
Input: root = [1]\
Output: [[1]]

*Example 3:*\
Input: root = []\
Output: []

**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        que = deque([root])
        levels = []

        while que:
            level = []
            for x in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

            levels.append(level)

        return levels
```


---
### 42. Same Tree [100]
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.\
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


*Example 1:*\
![alt text](image-12.png)\
Input: p = [1,2,3], q = [1,2,3]\
Output: true

*Example 2:*\
![alt text](image-13.png)\
Input: p = [1,2], q = [1,null,2]\
Output: false

*Example 3:*\
![alt text](image-14.png)\
Input: p = [1,2,1], q = [1,1,2]\
Output: false

*Example 4:*\
![alt text](image-15.png)
Input: p = [10,5,15], q = [10,5,null,null,15]\
Output: false

**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # For recursive find Edge Cases
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        if not p or not q: return False

        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ----- Iterative DFS ------
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            nodep, nodeq = stack.pop()
            
            if not nodep and not nodeq: continue
            if not nodep or not nodeq: return False
            if nodep.val != nodeq.val: return False

            stack.append((nodep.left, nodeq.left))
            stack.append((nodep.right, nodeq.right))

        return True
```


---
### 43. Path Sum [100]
Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.\
A leaf is a node with no children.

*Example 1:*\
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22\
Output: true\
Explanation: The root-to-leaf path with the target sum is shown.

*Example 2:*\
Input: root = [1,2,3], targetSum = 5\
Output: false\
Explanation: There are two root-to-leaf paths in the tree:\
(1 --> 2): The sum is 3.\
(1 --> 3): The sum is 4.\
There is no root-to-leaf path with sum = 5.

*Example 3:*\
Input: root = [], targetSum = 0\
Output: false\
Explanation: Since the tree is empty, there are no root-to-leaf paths.


**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = [(root, root.val)]

        while stack:
            node, currentSum = stack.pop()
            if node is None: continue

            if not node.left and not node.right:
                if currentSum == targetSum: return True

            # CurrentSum is calculated till the node, from now its children will add its own value
            if node.left: stack.append((node.left, currentSum + node.left.val))
            if node.right: stack.append((node.right, currentSum + node.right.val))

        return False

# ---------- Recursion ------------
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def dfs(root, currentSum):
            if root is None: return False

            currentSum += root.val

            if not root.left and not root.right and currentSum == targetSum:
                return True

            return dfs(root.left, currentSum) or dfs(root.right, currentSum)

        return dfs(root, 0)

# ---- Recursion with Same Function ------
def hasPathSum(self, root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return targetSum == root.val
    
    return (self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val))
```


---
---
### 🧠 Recursion / Backtracking – Common Mistake Cheat Sheet

---

### 1️⃣ STATE MIXING MISTAKE
(Your hasPathSum mistake)

❌ Wrong:\
Using one global variable for all branches.

Example mistake:\
target += node.val   (shared across left & right)

✔ Rule:\
Each recursive call must have its OWN state.

If recursion has:\
dfs(node, current_sum)

Then each branch gets separate copy automatically.

👉 Never manually subtract to "undo" unless you are using backtracking pattern.

---

### 2️⃣ FORGETTING LEAF CONDITION

Problem says:\
"root to leaf"

❌ Wrong:\
Checking sum before confirming leaf.

✔ Rule:\
If problem says root-to-leaf,\
ALWAYS check:\
if not node.left and not node.right

Leaf check is mandatory.

---

### 3️⃣ WRONG AND / OR LOGIC

If question asks:\
"Does there exist a path?"

✔ Use OR

If question asks:\
"Are both trees same?"

✔ Use AND

Golden Rule:\
Existence → OR  \
Validation / Matching → AND

---

### 4️⃣ RETURN VALUE NOT USED

Common mistake:

dfs(node.left)\
dfs(node.right)\
return node.val == something

❌ You ignored returned results.

✔ Rule:\
Always combine recursive results:

left = dfs(node.left)\
right = dfs(node.right)

return left OR right\
return left AND right\
return max(left, right)

---

### 5️⃣ BASE CASE RETURN WRONG VALUE

Ask:\
What should NULL return?

Examples:

Max depth:\
if not node → return 0

Max value:\
if not node → return -inf

Boolean check:\
if not node → return True or False?\
(Depends on problem logic)

Null return value controls whole recursion.

---

### 6️⃣ MODIFYING SHARED LIST WITHOUT BACKTRACK

❌ Wrong:\
path.append(x)\
dfs(...)
### no pop()

✔ Rule:\
If you modify list → always undo.

append → pop\
add → remove\
mark → unmark

Backtracking = clean state restore.

---

### 7️⃣ CHECKING CONDITION BEFORE UPDATING STATE

Wrong order:

if sum == target:\
sum += node.val

✔ Correct order:\
Update state first\
Then check base condition

---

### 8️⃣ CONFUSING TREE PROBLEMS TYPES

There are only 3 categories:

1. Carry State Down\
   Example: Path Sum

2. Combine From Children\
   Example: Max Depth

3. Validate Structure\
   Example: Same Tree

First decide category.\
Then apply correct pattern.

---

### 🎯 Final Mental Model

Before coding recursion, ask:

1. What is my state?
2. Is it shared or separate per branch?
3. What should null return?
4. Do I need AND or OR?
5. Do I need to undo changes?

If you answer these 5,\
you will avoid 90% recursion bugs.


---
---
### 44. Diameter of Binary Tree [543]
Given the `root` of a binary tree, return the length of the `diameter` of the tree.\
The `diameter` of a binary tree is the `length` of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.\
The `length` of a path between two nodes is represented by the number of edges between them.

*Example 1:*\
Input: root = [1,2,3,4,5]\
Output: 3\
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

*Example 2:*\
Input: root = [1,2]\
Output: 1

**Explanation:**\
It's Basically MinDepth Problem with Maintaining the Count of Edges

**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # Returns Height
        def dfs(curr):
            if not curr: return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res

# --------- Iterative ---------------
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        maxheightDict = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))

            else:
                if node.left is None: leftHeight = 0
                else leftHeight = maxHeightDict.pop(node.left)

                if node.right is None: rightHeight = 0
                else rightHeight = maxHeightDict.pop(node.right)

                diameter = max(diameter, leftHeight + rightHeight)
                maxHeightDict[node] = max(leftHeight, rightHeight) + 1

        return diameter
```


---
### 45. Invert Binary Tree [226]
Given the `root` of a binary tree, invert the tree, and return its root.

*Example 1:*\
Input: root = [4,2,7,1,3,6,9]\
Output: [4,7,2,9,6,3,1]

*Example 2:*\
Input: root = [2,1,3]\
Output: [2,3,1]

*Example 2:*\
Input: root = []\
Output: []

**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque([root])

        while que:
            node = que.popleft()
            if not node: continue

            node.left, node.right = node.right, node.left
            que.extend([node.left, node.right])

        return root

# ------- Recursive ---------
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```


---
### 46. Lowest Common Ancestor of a Binary Tree [236]
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.\
According to the `definition of LCA on Wikipedia`: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow `a node to be a descendant of itself`).”

*Example 1:*\
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1\
Output: 3\
Explanation: The LCA of nodes 5 and 1 is 3.

*Example 2:*\
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4\
Output: 5\
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

*Example 3:*\
Input: root = [1,2], p = 1, q = 2\
Output: 1

**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': #DFS
        if root == None or root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None: return root
        return left or right

# ----------- Iterative ---------
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': #DFS
        que = deque([root])
        parent = {root: None}

        while que:
            node = que.popleft()

            if node.left:
                que.append(node.left)
                parent[node.left] = node

            if node.right:
                que.append(node.right)
                parent[node.right] = node

            if p in parent and q in parent: break

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q:
            if q in ancestors: return q
            q = parent[q]
```


---
### 47. Search in a Binary Search Tree [700] {*Binary Search Tree*}
You are given the root of a binary search tree (BST) and an integer val.\
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


*Example 1:*\
Input: root = [4,2,7,1,3], val = 2\
Output: [2,1,3]

*Example 2:*\
Input: root = [4,2,7,1,3], val = 5\
Output: []


**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        
        curr = root

        while curr:
            if curr.val == val: return curr

            if val < curr.val:
                curr = curr.left
                continue

            if val > curr.val:
                curr = curr.right
                continue

        return None

# --------- Recursive --------------
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        
        if not root: return None
        if root.val == val: return root

        if val < root.val: return self.searchBST(root.left, val)
        if val > root.val: return self.searchBST(root.right, val)
```


---
### 48. Search in a Binary Search Tree [701]
You are given the root of a binary search tree (BST) and an integer val.\
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


*Example 1:*\
Input: root = [4,2,7,1,3], val = 2\
Output: [2,1,3]

*Example 2:*\
Input: root = [4,2,7,1,3], val = 5\
Output: []


**Explanation:**\
The key misunderstanding is about what “insert into BST” actually means.
- 👉 In a `Binary Search Tree`, `you NEVER insert in the middle` by pushing nodes down manually.
- 👉 You `always insert at a leaf position` where a None exists.
- 👉 BST insertion = exactly same as BST search, but stop at None and insert.

**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: return TreeNode(val)

        # Because in BST insertion, you must stop before curr becomes None, not after.
        curr = root
        while True:
            if val < curr.val:
                if curr.left: curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break

            elif val > curr.val:
                if curr.right: curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break

        return root
```


---
### 49. Convert Sorted Array to Binary Search Tree [108]
Given an integer array nums where the elements are `sorted in ascending order`, convert it to a `height-balanced` binary search tree.

*Example 1:*\
Input: nums = [-10,-3,0,5,9]\
Output: [0,-3,9,-10,null,5]\
Explanation: [0,-10,5,null,-3,null,9] is also accepted

*Example 2:*\
Input: nums = [1,3]\
Output: [3,1]\
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


**Code Solution:**
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ----------- Iterative BFS ------------
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        que = deque()
        que.append((root, 0, mid - 1))
        que.append((root, mid + 1, len(nums) - 1))

        while que:
            parent, left, right = que.popleft()

            if left <= right:
                midIndex = (left + right) // 2
                child = TreeNode(nums[midIndex])

                if nums[midIndex] < parent.val:
                    parent.left = child
                elif nums[midIndex] > parent.val:
                    parent.right = child

                que.append((child, left, midIndex - 1))
                que.append((child, midIndex + 1, right))
        
        return root

# ------- Recursive DFS --------
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(left, right):
            if left > right: return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)

            return node
        
        return convert(0, len(nums) - 1)
```