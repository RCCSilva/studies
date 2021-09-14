# Problem 1 - LRU Cache

## Overview

To hold the key and value pair, this implementation of LRU Cache uses a hash map. Given that we need to store the usage of each "key" in order to drop the least used when needed, I choose to use a doubly linked list, where the head node holds the keys with smaller count of use. For example, we may have a head node with the keys which were used once, followed by another node holding the keys used twice. If we need to make room for more data, the algorithm goes in the head node, pops one key from it and removes it from the hash map. Thus, we use three data structures: 1) hash map, 2) doubly linked list and 3) hash set.

- HashMap:
    + Key: Equal to the input "key".
    + Value: Holds both the input "value" and a reference to the current usage node of this key, which allows me to update the usage node in constant time.

- Doubly Linked List:
    + Ordered: The first node is the least recently used.
    + Node Data: The data of each node is a hash set, which stores the keys that were used "x" amount of times. For example, we may have a node that has the keys which were used two times. The hash set of this node will only contain keys used two times.

## Complexity Analyses

Given "n" as the amount of key and value pairs,

- `LRU_Cache.set(key, value)`: 
    + Time: O(1)
        + It takes constant time to add the key and value inside the hash map. It also takes constant time to update the Node or create the linked list node which holds the usage information
    + Space: O(n)
        + For `set()` operations, the hash map that has the values for each key will grow linear. Also, the input key will be saved in the node which contains keys used once. Thus, the hash set will as well grow linear following the amount of data to be cached.

- `LRU_Cache.get(key)`:
    + Time: O(1)
        + In order to get a value to a given pair, it takes constant time to extract it from the hash map. Even through we need to update the doubly linked list, holding the usage data, it also takes constant time, since we store a reference to the key's usage node in the hash map.
    + Space: O(1)
        + The lookup in a hash map is constant in terms of space. Since we're just moving data in the doubly linked list, it also uses constant space.
