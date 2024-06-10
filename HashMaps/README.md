# Hash Maps

A hash map is a data structure that maps keys to values. It uses a hash function to determine the index where the corresponding value is stored in an array. This allows for fast lookups, insertion, and deletion operations

## How does a hashmap work?
1. Hash Function:
The hash function converts a given key into an index in an array.
Ideally, the function distributes the keys uniformly across the array to minimize collisions.

2. Array (Buckets):
The hash map uses an array where each position(bucket) can store a value.
If the hash function maps multiple keys to the same index, this is known as a `collision`.

3. Handling collisions
- Separate Chaining: Each bucket points to a linked list of entries that have the same index.

- Open Addressing: If a collision occurs, the hash map searches for the next available bucket using methods like linear probing, quadratic probing, or double hashing.


## Uses of Hash Maps
- Database Indexing: Hash maps are used to index large amounts of data, allowing for fast retrieval and storage.
- Caching: Storing frequently accessed data to reduce repeated computation
- Routers and DNS Resolution: Used to route internet traffic and resolve domain names to IP addresses
- Language Interpretation: Used in compilers and interpreters to store variables and functions in a symbol table.

