# Merge Sort
Beautiful and the definition of confusing.
Merge sorting allows for super fast sorting by calling itself (so-called **recursion**).

As it is quite difficult for beginners in CS to understand this algorithm,
I created it manually in Python.

**For CS50 students:** I chose Python over C as it simplifies things A LOT and is so much easier to read.
To the general concept it the same, no matter what language. If you want to try to implement this algorithm
in C, go ahead! But keep in mind that you have to be aware of pointers.

**If you want to look like a hacker:**

To enable debug printing, run `merge_sort_debug.py` instead of `merge_sort.py`.

## Understanding the general idea
It can be quite difficult to keep an overview over what is actually happening when you run your code.
Simply because recursion seems to be non-sensical. When you try to understand how the algorithm works, you get
to the line where it calls itself and to understand that you have to understand the algorithm in the first place.

**So, don't be intimidated if you have absolutely no idea what is going on!**

## 1. Starting the algorithm
When you run `$ python3 merge_sort.py`, the first thing that happens is Python calling `main()`.

`main()` simply prints some nice ASCII art and instructions but doesn't actually calculate anything.
Well, it generates a random list and also stops the time, but nothing that would be relevant for sorting.

**On line 113:**
```python
sorted_list = sort(unsorted_list)
```
calls the actual sorting algorithm.

The result is a list that now is sorted and stored into `sorted_list`.

## 2. Running the sorting algorithm
As you can see, `sort(unsorted_list)` isn't acutally that complicated.
```python
def sort(unsorted_list):

    # if list is large than 1
    if len(unsorted_list) > 1:

        # split list in halves
        left_half, right_half = split(unsorted_list)

        # sort left half
        sorted_left_half = sort(left_half)

        # sort right half
        sorted_right_half = sort(right_half)
    
        # merge halves
        sorted_list = merge(sorted_left_half, sorted_right_half)
        
        # return sorted list
        return sorted_list
    
    # if list is only one number
    else:
        # unsorted_list is sorted_list
        sorted_list = unsorted_list
        return sorted_list
```
Let's go through it step by step.

`sort(unsorted_list)` takes as argument an unsorted list, which we call `unsorted_list`.
### Base case
The first thing the function does, is to check if the unsorted list has more than only one element.
```python
if len(unsorted_list) > 1:
```
If not, `else:` simply returns the unsorted list, because, ...well a list of 1 is by definition sorted.

**This is important!**

If we wouldn't include this option, then recursion would cause the function to call itself infinite times.

This is our **base case**.

### Recursion
Now, if the list has more than 1 element, the next thing the function does is to split this list into two halves.
```python
left_half, right_half = split(unsorted_list)
```
For now, we don't care how Python does that, but if you are curious, you can find a detailed explanation further down.

We now have **two halves**. For example: [4, 8, 3, 1] and [5, 2, 9, 6]

After that, we start with sorting the left half.
```python
sorted_left_half = sort(left_half)
```
