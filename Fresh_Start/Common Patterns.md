# Common Patterns

1. Sliding Window:

  * Need to process the series of Data like list or String
  * Looking smaller part of the list
  * liner data structure
  * When to Use:
    *  If a problem has to find the sub-set of the elements that satisfies given condition
  * Eg: Find the longest substring with k unique characters in a given string

2. SubSet Pattern:
  * Used to find all the possible combination of the elements from a given set [repation may Or may not be allowed]
  * Eg: Permutations

3. Modified Binary Search:
  * Core idea is same but need to adjust the logic little bit to solve the problem
  * To understand binary search in dept [when duplicates, or does not contain the target, etc], code the bisect_right and left function in python.
  * Eg: Search in Rotated Sorted Array

4. Top K Elements:
  * Used to select k element from a larger dataset with given condition
  * linear data structure
  * You have to keep tark of k most important number to seen so far
  * These numbers are stored using DataStructure like Heap [For finding and removing the number efficiently]
  * Eg: Given an integer array nums and an inter k, return the kth largest element in the array.

5. Binary Tree Depth First Search [DFS]:
  * Generally used recurrsion to do this
  * Goes inDept at side side of the node at a time and after the dead end goes for the other side
  * Eg: Maximum Depth of Binary Tree

6. Topological Sort:
  * Used to arrange elements in specific order when their is dependency on other
  * Particularly useful for Directed Acyclic Graphs
    * One Way Connection
    * No Cycle / Loop
  * Use whenever you have pre-requiste chain
    * When their is dependency on other module
    * When other modules complete then next module should execute
  * Eg: Course Schedule

7. Binary Tree Breath First Search [BFS]:
  * It explores all the nodes in different branchs at the same level first
  * Then go to next level
  * We use Queue for that
  * Generally used recurrsion for this algorithm
  * Eg: Binary Tree Level Order Traversal

8. Two Pointer Pattern:
  * Used to solve a problem when you iterate through a *sorted array*
  * Used to solve problem in single pass
  * Linear Data Struture
  * Eg: Two Sum, 3 Sum