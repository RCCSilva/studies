# Problem 2 - File Recursion

## Overview

The algorithm uses recursion and lists. For each subfolder of the root folder, it aggregates the results and returns them. The results are lists of files that had the specified suffix inside the given folder.

## Complexity Analyses

Given that "n" is the amount of files and directories in the root folder,

- Time: O(n)
    + The algorithm has to run through every single file and directory of the specified root folder.
- Space: O(n)
    + While running, it may hold all files and directories inside its internal list variables, because of two main reasons: either all the files were placed in the root folder, or all the files match the supplied suffix. Thus, in the worst case scenario, it may have a list as big as "n" files.