# Problem 5 - Blockchain

## Overview

The Blockchain works almost as a linked list, where each Block has a reference to the next Block. The only difference is that each Block has a property called "previous_hash" that stores the hash of the Block before it. This is a fundamental feature of a blockchain as it permits anyone to verify the validity of the chain.

## Complexity Analyses

Given "n" as the length of the list holding the data we'd like to add to the blockchain,

- Time: O(1)
  - Creating the hash for the Block's data takes constant time.
  - It also takes constant time to add a new node to the blockchain, since we have the references of where it should be placed. It is not needed, for example, to run through the entire chain to add a new one.
- Space: O(n)
  - Adding a new value in the chain just creates a new instance of Block. Since the Block's data does not grow as we increase the chain size, it has a linear space complexity. For example, the "hash" or "previous_hash" will have the same size, regardless of the blockchain size.
