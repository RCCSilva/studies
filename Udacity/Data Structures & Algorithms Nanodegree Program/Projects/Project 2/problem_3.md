# Problem 3 - Huffman Coding

## Overview

The encode algorithm follows the steps provided in the course: 1) create a count table; 2) creates the Huffman Tree recursively; 3) creates the Huffman Code; finally 4) it replaces each character by its binary representation. In order to create the Huffman Tree, the function recursively calls itself with the resulting list of nodes, sorting this list every time so it can get the two nodes with the least amount of count. 

## Complexity Analyses

Given "n" as the input sentence,

- `huffman_encoding()`:
    + Time: O(n logn)
        + As implemented, we have some O(n) steps as, for example, the creation of a count table and creation of Huffman Codes. Nevertheless, in order to create the Huffman Tree the algorithm sorts the node list each time the function `create_huffman_tree()` is called recursively. Since O(n logn) time complexity, in the long run, surpasses the linear complexity, encoding takes O(n logn).
    + Space: O(n)
        + In order to create the tree, we first start with a list of nodes which grows linear following the size of the input sentence.

Given "n" as the size of the encoded data (binary representation),

- `huffman_decoding()`
    + Time: O(n)
        + Decoding has to go through the encoded data, following the correspondent binary values in the `tree`.
    + Space: O(n)
        + The space grows following the decoding of each character in the encoded data.