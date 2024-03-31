# Project 0x00: Pagination Back-end


This project focuses on implementing pagination functionalities in the back-end of a web application.
Pagination is crucial for efficiently handling large datasets by breaking them into manageable chunks.
In this project, you will write functions and methods to paginate datasets, retrieve specific pages of data,
and provide hypermedia pagination for improved navigation.

## Resources

Before starting the project, you may find the following resources helpful:

- [REST API Design: Pagination](https://www.baeldung.com/rest-api-pagination): 
                   Learn about the principles and best practices of pagination in RESTful APIs.
- [HATEOAS](https://restfulapi.net/hateoas/): Understand the concept of Hypermedia as the 
                   Engine of Application State (HATEOAS) and its relevance in web development.

## Tasks

### 0. Simple helper function (mandatory)

#### Description

Write a function named `index_range` that takes two integer arguments `page` and `page_size`. 
The function should return a tuple of size two containing a start index and an end index corresponding 
to the range of indexes to return in a list for those particular pagination parameters.

#### Details

Page numbers are 1-indexed, i.e., the first page is page 1.

### 1. Simple pagination

#### Description

Implement a method named `get_page` that takes two integer arguments `page` with a default value of 1 and
 `page_size` with a default value of 10. You have to use a CSV file (same as the one presented at the top of the project). 
Use `assert` to verify that both arguments are integers greater than 0. Use the `index_range` function to find the correct
 indexes to paginate the dataset correctly and return the appropriate page of the dataset.

#### Details

If the input arguments are out of range for the dataset, an empty list should be returned.

### 2. Hypermedia pagination

#### Description

Implement a method named `get_hyper` that takes the same arguments (and defaults) as `get_page` and returns 
a dictionary containing hypermedia pagination information.

#### Details

The dictionary contain the following key-value pairs:
- `page_size`: the length of the returned dataset page.
- `page`: the current page number.
- `data`: the dataset page.
- `next_page`: number of the next page, None if no next page.
- `prev_page`: number of the previous page, None if no previous page.
- `total_pages`: the total number of pages in the dataset as an integer.

### 3. Deletion-resilient hypermedia pagination

#### Description

Implement a method named `get_hyper_index` with two integer arguments: `index` with a default value of None 
and `page_size` with a default value of 10.

#### Details

The method returns a dictionary with the following key-value pairs:
- `index`: the current start index of the return page.
- `next_index`: the next index to query with.
- `page_size`: the current page size.
- `data`: the actual page of the dataset.

Requirements/Behavior:
- Use `assert` to verify that `index` is in a valid range.
- If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with page_size 10, but rows 3, 6, and 7 were deleted, the user should 
  still receive rows indexed 10 to 19 included.

