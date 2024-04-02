# Project 0x01: Caching Back-end

In this project,I will delve into the world of caching systems and explore different caching algorithms. 
We will explore various cache replacement policies such as FIFO, LIFO, LRU, MRU, and LFU to understanding 
their concepts and implementations.

## Background Context

Caching is a fundamental concept in computer science and software engineering, involving the temporary 
storage of frequently accessed data to improve system performance. This project provides an opportunity 
to deepen understanding of caching systems and algorithms.

## Resources

Before diving into the project tasks, you may find the following resources helpful:

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_(LFU))

## Learning Objectives

By completing this project, you should be able to explain to anyone, without the help of Google:

- The concept of a caching system
- Various caching algorithms such as FIFO, LIFO, LRU, MRU, and LFU
- The purpose and limitations of caching systems


## Tasks

### 0. Basic Dictionary

#### Description

Create a class `BasicCache` that inherits from `BaseCaching` and represents a basic caching system. 
This caching system doesn’t have a limit on the number of items it can store.

#### Details

- Use `self.cache_data`, a dictionary from the parent class `BaseCaching`.
- Implement `put(self, key, item)` method:
  - Assign the item value for the key `key` in the `self.cache_data` dictionary.
  - If `key` or `item` is `None`, this method should not do anything.
- Implement `get(self, key)` method:
  - Return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### 1. FIFO Caching

#### Description

Implement a class `FIFOCache` that represents a caching system based on the FIFO (First In, First Out) algorithm.

#### Details

- Use `self.cache_data`, a dictionary from the parent class `BaseCaching`.
- Implement `put(self, key, item)` method:
  - Assign the item value for the key `key` in the `self.cache_data` dictionary.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the first item put in cache (FIFO algorithm).
    - Print `DISCARD:` with the key discarded and followed by a new line.
- Implement `get(self, key)` method:
  - Return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### 2. LIFO Caching

#### Description

Implement a class `LIFOCache` that represents a caching system based on the LIFO (Last In, First Out) algorithm.

#### Details

- Use `self.cache_data`, a dictionary from the parent class `BaseCaching`.
- Implement `put(self, key, item)` method:
  - Assign the item value for the key `key` in the `self.cache_data` dictionary.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the last item put in cache (LIFO algorithm).
    - Print `DISCARD:` with the key discarded and followed by a new line.
- Implement `get(self, key)` method:
  - Return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### 3. LRU Caching

#### Description

Implement a class `LRUCache` that represents a caching system based on the LRU (Least Recently Used) algorithm.

#### Details

- Use `self.cache_data`, a dictionary from the parent class `BaseCaching`.
- Implement `put(self, key, item)` method:
  - Assign the item value for the key `key` in the `self.cache_data` dictionary.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least recently used item (LRU algorithm).
    - Print `DISCARD:` with the key discarded and followed by a new line.
- Implement `get(self, key)` method:
  - Return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### 4. MRU Caching

#### Description

Implement a class `MRUCache` that represents a caching system based on the MRU (Most Recently Used) algorithm.

#### Details

- Use `self.cache_data`, a dictionary from the parent class `BaseCaching`.
- Implement `put(self, key, item)` method:
  - Assign the item value for the key `key` in the `self.cache_data` dictionary.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the most recently used item (MRU algorithm).
    - Print `DISCARD:` with the key discarded and followed by a new line.
- Implement `get(self, key)` method:
  - Return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### 5. LFU Caching

#### Description

Implement a class `LFUCache` that represents a caching system based on the LFU (Least Frequently Used) algorithm.

#### Details

- Use `self.cache_data`, a dictionary from the parent class `BaseCaching`.
- Implement `put(self, key, item)` method:
  - Assign the item value for the key `key` in the `self.cache_data` dictionary.
  - If `key` or `item` is `None`, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least frequency used item (LFU algorithm).
    - If you find more than 1 item to discard, use the LRU algorithm to discard only the least recently used.
    - Print `DISCARD:` with the key discarded and followed by a new line.
- Implement `get(self, key)` method:
  - Return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.


