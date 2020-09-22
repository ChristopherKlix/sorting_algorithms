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

We now have **two halves**. For example: [8, 4, 3, 1] and [5, 2, 9, 6]

After that, we start with sorting the left half.
```python
sorted_left_half = sort(left_half)
```
Yeah... seems weird, and it is, but in fact this is super powerful.
Basically, what happens is the we now start the function again, but with a list of size 4, assuming we started with an initial list of size 8.
And this first thing the function does, again, check if the list is greater than 1, which it is, split it into two halves ([8, 4] and [3 ,1])
and sort the left half.
This calls the function again, but this time with a list of size 2. Split into [8] and [4] and sort the left half.

**Now the function gets called with a list of size 1**

That means that the first if statement no longer is `True` and the function executes the **base case** and returns the list as it is.

We can now store the result of `sort(left_half)` in `sorted_left_half = [8]` and proceed with the former function.
The function next calls
```python
sorted_right_half = sort(right_half)
```
And again, this function call returns a list of size 1 `[4]`.

That means that we can now proceed to step 4.

### Merge
Again, we don't really care how Python merges the two halves, but if you are curious, see further below for a detail explanation.

Summarized, it step by step compares index 0 of both halves and append the smaller one to a new list.

This repeats until all elements from both halves are appended to the new list and this list is then returned and stored in `sorted_list`.
```python
sorted_list = merge(sorted_left_half, sorted_right_half)
```

### Return
Now that we have a sorted list of [4, 8], the function returns this `sorted_list` to its caller function.

And if you remember, this call came from `sorted_left_half = sort(left_half)`, where left_half was [8, 4].
Wich now was returned as [4, 8] and stored in `sorted_left_half`.

The same process now continues to
```python
sorted_right_half = sort(right_half)
```

After that, both sorted halves `[4, 8]` and `[1, 3]` are merge to `[1, 3, 4, 8]` and returned to its caller function,
which, again, was the previous `sorted_left_half = sort(left_half)`.

This function then proceeds to
```python
sorted_right_half = sort(right_half)
```
where the entire process that we just went through is repeated again for the right half of the original list of size 8.

This will return `[2, 5, 6, 9]`, which then gets merged with `[1, 3, 4, 8]`.

### Done
Now, we just have to merge both and we're done!
