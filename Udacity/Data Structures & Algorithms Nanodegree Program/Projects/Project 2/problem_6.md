# Problem 6 - Union and Intersection of Two Linked Lists

## Overview

Taking into account that hash sets have optimal performance with "union" and "intersection" operations, I choose to convert the linked list values into sets, perform the operation and, finally, convert the result set into a linked list.

## Complexity Analyses

Given that "n" is the amount of values in both linked lists.

- Time: O(n)
    +  In order to create a union or an intersection, the algorithm has to traverse through the values of both sets.
- Space: O(n)
    + Given that it has to convert the LinkedList to the HashSet, this algorithm also has a O(n) space complexity.