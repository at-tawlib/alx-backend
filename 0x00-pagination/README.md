# 0x00. Pagination

### 0. Simple helper function
 [0-simple_helper_function.py](0-simple_helper_function.py) , [0-main.py](0-main.py)
function  that takes two integer arguments  `page`  and  `page_size`.
function return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

```
bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```

### 1. Simple pagination
[1-simple_pagination.py](1-simple_pagination.py) , [1-main.py](1-main.py)
has a `Server` class which gets data from [Popular_Baby_Names.csv](Popular_Baby_Names.csv) 
Implement a method named  `get_page`  that takes two integer arguments  `page`  with default value 1 and  `page_size`  with default value 10.
-   Use  `assert`  to verify that both arguments are integers greater than 0.
-   Use  `index_range`  to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
-   If the input arguments are out of range for the dataset, an empty list should be returned.

```
bob@dylan:~$  wc -l Popular_Baby_Names.csv 
19419 Popular_Baby_Names.csv
bob@dylan:~$  
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$  
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$ 
```

### 2. Hypermedia pagination
[2-hypermedia_pagination.py](2-hypermedia_pagination.py), [2-main.py](2-main.py)
Based on above
Implement a  `get_hyper`  method that takes the same arguments (and defaults) as  `get_page`  and returns a dictionary containing the following key-value pairs:
-   `page_size`: the length of the returned dataset page
-   `page`: the current page number
-   `data`: the dataset page (equivalent to return from previous task)
-   `next_page`: number of the next page,  `None`  if no next page
-   `prev_page`: number of the previous page,  `None`  if no previous page
-   `total_pages`: the total number of pages in the dataset as an integer

```
bob@dylan:~$ 
bob@dylan:~$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
bob@dylan:~$ 
```

### 3. Deletion-resilient hypermedia pagination
[3-hypermedia_del_pagination.py](3-hypermedia_del_pagination.py), [3-main.py](3-main.py)

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
Implement a  `get_hyper_index`  method with two integer arguments:  `index`  with a  `None`  default value and  `page_size`  with default value of 10.
-   The method should return a dictionary with the following key-value pairs:
    -   `index`: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with  `page_size`  20, and no data was removed from the dataset, the current index should be 60.
    -   `next_index`: the next index to query with. That should be the index of the first item after the last item on the current page.
    -   `page_size`: the current page size
    -   `data`: the actual page of the dataset

**Requirements/Behavior**:

-   Use  `assert`  to verify that  `index`  is in a valid range.
-   If the user queries index 0,  `page_size`  10, they will get rows indexed 0 to 9 included.
-   If they request the next index (10) with  `page_size`  10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.

```
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']], 'page_size': 2, 'next_index': 5}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
Nb items: 19417
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']], 'page_size': 2, 'next_index': 6}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
bob@dylan:~$ 
```

> Written with [StackEdit](https://stackedit.io/).
