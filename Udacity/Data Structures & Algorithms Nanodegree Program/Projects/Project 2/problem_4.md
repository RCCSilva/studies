# Problem 4 - Active Directory

## Overview

The algorithm takes a recursive approach, verifying for each subgroup if it has the input user.

## Complexity Analyses

Given "n" as the amount of groups (nested or not)

- Time: O(n)
    + We may have to run through every single subgroup in order to verify if the user is in the group. It also takes O(n) time to verify if the user is in the group list.
- Space: O(n)
    + The algorithm itself does not create variables, but it creates a new stack each time it calls itself. Thus, the stack space will grow, in the worst case, "n" times, taking into account that we may have to visit all groups.