# 0x01. Caching
### 0. Basic dictionary
[0-basic_cache.py](0-basic_cache.py) , [0-main.py](0-main.py)
`BasicCache`  that inherits from  `BaseCaching`  and is a caching system:

-   This caching system doesn’t have limit
-   `def put(self, key, item):`
    -   Must assign to the dictionary  `self.cache_data`  the  `item`  value for the key  `key`.
    -   If  `key`  or  `item`  is  `None`, this method should not do anything.
-   `def get(self, key):`
    -   Must return the value in  `self.cache_data`  linked to  `key`.
    -   If  `key`  is  `None`  or if the  `key`  doesn’t exist in  `self.cache_data`, return  `None`.

```
guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
```

### 1. FIFO caching
[1-fifo_cache.py](1-fifo_cache.py) , [1-main.py](1-main.py)

has a class  `FIFOCache`  that inherits from  `BaseCaching`  and is a caching system:
-   `def put(self, key, item):`
    -   Must assign to the dictionary  `self.cache_data`  the  `item`  value for the key  `key`.
    -   If  `key`  or  `item`  is  `None`, this method should not do anything.
    -   If the number of items in  `self.cache_data`  is higher that  `BaseCaching.MAX_ITEMS`:
        -   you must discard the first item put in cache (FIFO algorithm)
        -   you must print  `DISCARD:`  with the  `key`  discarded and following by a new line

```
guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
```

### 2. LIFO Caching
[2-lifo_cache.py](2-lifo_cache.py) , [2-main.py](2-main.py)

has a class  `LIFOCache`  that inherits from  `BaseCaching`  and is a caching system:

-   `def put(self, key, item):`
    -   Must assign to the dictionary  `self.cache_data`  the  `item`  value for the key  `key`.
    -   If  `key`  or  `item`  is  `None`, this method should not do anything.
    -   If the number of items in  `self.cache_data`  is higher that  `BaseCaching.MAX_ITEMS`:
        -   you must discard the last item put in cache (LIFO algorithm)
        -   you must print  `DISCARD:`  with the  `key`  discarded and following by a new line
```
guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$ 
```

### 3. LRU Caching
[3-lru_cache.py](3-lru_cache.py), [3-main.py](3-main.py)

has a class  `LRUCache`  that inherits from  `BaseCaching`  and is a caching system:
-   `def put(self, key, item):`
    -   Must assign to the dictionary  `self.cache_data`  the  `item`  value for the key  `key`.
    -   If  `key`  or  `item`  is  `None`, this method should not do anything.
    -   If the number of items in  `self.cache_data`  is higher that  `BaseCaching.MAX_ITEMS`:
        -   you must discard the least recently used item (LRU algorithm)
        -   you must print  `DISCARD:`  with the  `key`  discarded and following by a new line
```
guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Fracisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$ 
```

### 4. MRU Caching
[4-mru_cache.py](4-mru_cache.py) , [4-main.py](4-main.py)
has a class  `MRUCache`  that inherits from  `BaseCaching`  and is a caching system:

-   `def put(self, key, item):`
    -   Must assign to the dictionary  `self.cache_data`  the  `item`  value for the key  `key`.
    -   If  `key`  or  `item`  is  `None`, this method should not do anything.
    -   If the number of items in  `self.cache_data`  is higher that  `BaseCaching.MAX_ITEMS`:
        -   you must discard the most recently used item (MRU algorithm)
        -   you must print  `DISCARD:`  with the  `key`  discarded and following by a new line

```
guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/0x01$ 
```


### 5. LFU Caching
[100-lfu_cache.py](100-lfu_cache.py) , [100-main.py](100-main.py)
has a class  `LFUCache`  that inherits from  `BaseCaching`  and is a caching system:
-   `def put(self, key, item):`
    -   Must assign to the dictionary  `self.cache_data`  the  `item`  value for the key  `key`.
    -   If  `key`  or  `item`  is  `None`, this method should not do anything.
    -   If the number of items in  `self.cache_data`  is higher that  `BaseCaching.MAX_ITEMS`:
        -   you must discard the least frequency used item (LFU algorithm)
        -   if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
        -   you must print  `DISCARD:`  with the  `key`  discarded and following by a new line
```
guillaume@ubuntu:~/0x01$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
guillaume@ubuntu:~/0x01$ 
```

> Written with [StackEdit](https://stackedit.io/).
