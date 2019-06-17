Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1) - For every item added, because I'm keeping track of my position in the list, I need only to add the item to the appropriate index regardless of the length of the list.

2. What is the space complexity of your ring buffer's `append` function?

O(1) - Regardless of the input or the size of the list, the variables tracked are fixed: the input, the capacity, and the current position.

3. What is the runtime complexity of your ring buffer's `get` method?

O(1) - I'm simply returning the list (or some subsection of it), so the size of that list is irrelevant.

4. What is the space complexity of your ring buffer's `get` method?

O(n) - The space kept by the list is the only significant total space consideration.

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) - Two nested `for` loops always give a n^2 complexity.

6. What is the space complexity of the provided code in `names.py`?

O(1) - No significant increase in space is required. The input is the only space used.

7. What is the runtime complexity of your optimized code in `names.py`?

** I have two commits with answers for the `names.py` problem. This regards the first one, because the second path leads to madness.
O(n logn) - Building the BST with names from the first list is insignificant compared to looping through the second list of names. Inside that O(n) complexity is a binary search that is O(log n). The two together yield O(n logn).

8. What is the space complexity of your optimized code in `names.py`?

O(n) - There is a significant number of variables created, on the order of the number of input variables, when a BST is created.
