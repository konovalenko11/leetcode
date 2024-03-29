<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Google Sans">

<style>
   summary {
      font-family: "Google Sans";
   }
   .easy {
      background-color: green;
   }
</style>

# Problem Descriptions

<!-----------------------------------------------------------------------------
-- 14. Longest Common Prefix
------------------------------------------------------------------------------>
<details>
<summary><b class = "easy">14. Longest Common Prefix</b>
   <a href="python/14-longest-common-prefix/solution.py">[python]</a>
   <a href="python/14-longest-common-prefix/solution_v2.py">[python v2]</a>
</summary>
<br />

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

<pre>**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"
</pre>

**Example 2:**

<pre>**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.
</pre>

**Constraints:**

*   `1 <= strs.length <= 200`
*   `0 <= strs[i].length <= 200`
*   `strs[i]` consists of only lower-case English letters.

### Solution 1 (word by word)
1. Taking the `strs[0]` (first element) as an initial `prefix`
2. Iterating through all words starting from `strs[1]`
3. Iterating through `prefix` letters and comparing with letters in `strs[1]` (example)
4. If we find the letter that differs, shrinking our `prefix = prefix[:i]`
   and continuing to the next element in `strs`.
5. If after some iteration we find that `prefix` is empty, breaking the outer 
   loop and returning empty string.

### Solution 2 (column by column)
1. Taking the `strs[0]` (first element) as starting string
2. Iterating through all letters in `strs[0]`
3. Iterating through all strings in `strs[1:]` and checking if current letter 
   from `strs[0]` is NOT equal to the same letter in other words or we find 
   shorter word.
   If we haven't found issues, adding to letter to `prefix`.
4. Otherwise, returning `prefix`

</details>

<!-----------------------------------------------------------------------------
-- 26. Remove Duplicates from Sorted Array
------------------------------------------------------------------------------>
<details>
<summary><b>26. Remove Duplicates from Sorted Array</b>
   <a href="problems/python/26-remove-duplicates/solution_queue.py">[python (queue)]</a>
</summary>
<br />

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` _after placing the final result in the first_ `k` _slots of_ `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**

<pre>**Input:** nums = [1,1,2]
**Output:** 2, nums = [1,2,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

**Example 2:**

<pre>**Input:** nums = [0,0,1,1,1,2,2,3,3,4]
**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

**Constraints:**

*   `0 <= nums.length <= 3 * 10<sup>4</sup>`
*   `-100 <= nums[i] <= 100`
*   `nums` is sorted in **non-decreasing** order.

### Solution 1 (queue)
1. Iterating through elements and registering **last unique number**.
2. If `num[i] == last_unique_num` then we need to replace element value with 
   "gap" ("_") and add the index of gap to queue.
3. Otherwise, if `num[i] != last_unique_num`, updating `last_unique_num` and 
   moving to the place where is a gap (if there are gaps). And adding current 
   index to the queue.
   ```python
   if gaps:
      gap_idx = gaps.popleft()
      nums[gap_idx], nums[i] = nums[i], nums[gap_idx]
      gaps.append(i)
   ```
   In parallel, incrementing the `unique_numbers` counter.
4. Returning `unique_numbers` counter.

### Solution 2 (list)
1. Iterating through elements and registering **last unique number idx**.
2. If `nums[i] != nums[last_num_idx]`, then incrementing `last_num_idx` and 
   assigning the current number to the new `last_num_idx` (the next position).
3. Returning `last_num_idx + 1`

Note: It doesn't matter what goes after the list of unique numbers. The main 
point to have first `n` elements be filled with requested unique numbers.

</details>

<!-----------------------------------------------------------------------------
-- 27. Remove Element
------------------------------------------------------------------------------>
<details>
<summary><b>27. Remove Element</b>
   <a href="python/27-remove-element/solution_list.py">[python]</a>
   <a href="python/27-remove-element/solution_list_2.py">[python (optimized)]</a>
</summary>
<br />

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` _after placing the final result in the first_ `k` _slots of_ `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**

<pre>**Input:** nums = [3,2,2,3], val = 3
**Output:** 2, nums = [2,2,_,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

**Example 2:**

<pre>**Input:** nums = [0,1,2,2,3,0,4,2], val = 2
**Output:** 5, nums = [0,1,4,0,3,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

**Constraints:**

*   `0 <= nums.length <= 100`
*   `0 <= nums[i] <= 50`
*   `0 <= val <= 100`

### [Solution 1 (moving correct nums)](python/27-remove-element/solution_list.py)
1. Setting up pointer to the last correct number.
2. Iterating through the elements in `nums`.
3. If we find correct number, assigning and incrementing the value of 
   `last_correct_number`:
   ```python
   nums[last_correct_number] = nums[i]
   last_correct_number += 1
   ```
4. Returning `last_correct_number`.

### [Solution 2 (moving invalid nums)](python/27-remove-element/solution_list_2.py)
This algorithm might be more efficient if invalid number is rare.

1. Setting up forward and back pointers:
   ```python
   forward = 0
   back = len(nums)
   ```
2. Iterating through the elements while `forward < back`.
3. If we find invalid number, we're assigning `nums[forward] = nums[back - 1]`
   and decrementing `back` pointer.
4. Otherwise, incrementing `forward` pointer.
5. Returning `back` pointer.

</details>

<!-----------------------------------------------------------------------------
-- 28. Implement strStr()
------------------------------------------------------------------------------>
<details>
<summary><b>28. Implement strStr()</b>
   <a href="python/28-implement-strstr/solution.py">[python]</a>
   <a href="python/28-implement-strstr/solution_simple.py">[python (simple)]</a>
</summary>
<br />

Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Return the index of the first occurrence of needle in haystack, or `-1` if `needle` is not part of `haystack`.

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

**Example 1:**

<pre>**Input:** haystack = "hello", needle = "ll"
**Output:** 2
</pre>

**Example 2:**

<pre>**Input:** haystack = "aaaaa", needle = "bba"
**Output:** -1
</pre>

**Example 3:**

<pre>**Input:** haystack = "", needle = ""
**Output:** 0
</pre>

**Constraints:**

*   `0 <= haystack.length, needle.length <= 5 * 10<sup>4</sup>`
*   `haystack` and `needle` consist of only lower-case English characters.

**Note:** In general this problem should be solved by using the 
[Boyer–Moore–Horspool algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm).

### Solution 1 (custom algorithm)
1. Returning `0` if `needle` is empty.
2. Iterating through `haystack`.
3. For each symbol in `haystack` we're looping through `needle`.
4. If `needle` loop finished successfully (using additional flag `search_broken`
   ), returning index of `haystack` symbol.
5. Otherwise, if we find that relative `haystack` symbol differs from `needle` 
   symbol, then:
    - if before that moment we had only the same repeating symbols, then we 
      don't need to loop throught the whole `needle` again. It will be enough 
      just to restart search from current `needle index`.
    - if before that moment we had different symbols in `haystack`, then we need 
      to start the search in `needle` from the beginning (`0`).
6. Returning `-1` if haven't found anything.

### Solution 2 (simple reusing of built-in function)
```python
return haystack.find(needle) if needle else 0
```

</details>

<!-----------------------------------------------------------------------------
-- 54. Spiral Matrix
------------------------------------------------------------------------------>
<details>
<summary><b>54. Spiral Matrix</b>
<a href="python/54-spiral-matrix/main.py">[python]</a>
<a href="python/54-spiral-matrix/main_v2_visited.py">[python 2]</a>
</summary>
<br />

Given an `m x n` `matrix`, return _all elements of the_ `matrix` _in spiral order_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

<pre>**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]
</pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

<pre>**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

**Constraints:**

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= m, n <= 10`
*   `-100 <= matrix[i][j] <= 100`

### Solution 1
1. Starting from the (0,0) and going further until we reach the limit of steps 
   for row/column.
2. If we reached the limit of steps, it means that we went through all elementsd on the side and we need to turn vector clockwise.
   ```python
   x, y = y, -x
   ```
3. On each second side (side num 2, 4, ...) we decrease the side steps counter.
4. Proceeding until we looped through all elements.

### Solution 2 (recording visited)
1. Starting from the (0,0) and going further until we reach the edge of row/column or new element was already visited.
2. If so, it means that we went through all elements on the side and we need to turn vector clockwise.
   ```python
   x, y = y, -x
   ```
3. Otherwise: `x, y = xnew, ynew`
4. Proceeding until we looped through all elements.
</details>

<!-----------------------------------------------------------------------------
-- 66. Plus One
------------------------------------------------------------------------------>
<details>
<summary><b>66. Plus One</b>
<a href="python/66-plus-one/main.py">[python]</a>
</summary>
<br />

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i<sup>th</sup>` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return _the resulting array of digits_.

**Example 1:**

<pre>**Input:** digits = [1,2,3]
**Output:** [1,2,4]
**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

**Example 2:**

<pre>**Input:** digits = [4,3,2,1]
**Output:** [4,3,2,2]
**Explanation:** The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

**Example 3:**

<pre>**Input:** digits = [0]
**Output:** [1]
**Explanation:** The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].
</pre>

**Example 4:**

<pre>**Input:** digits = [9]
**Output:** [1,0]
**Explanation:** The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

**Constraints:**

*   `1 <= digits.length <= 100`
*   `0 <= digits[i] <= 9`
*   `digits` does not contain any leading `0`'s.

### Solution
1. Loop throught the digits in reverse order
2. If `digits[idx] == 9` then `digits[idx] = 0`
3. Else `digits[idx] += 1` and `return digits`
4. If you went throug sll elements, it means that the the most significant 
   element was 9, lso we need to add "1" at the beginning of an array:
   `[1] + digits`

</details>

<!-----------------------------------------------------------------------------
-- 67. Add Binary
------------------------------------------------------------------------------>
<details>
<summary>
   <b>67. Add Binary</b>
   <a href="python/67-add-binary/main.py">[python]</a>
</summary>
<br />

Given two binary strings `a` and `b`, return _their sum as a binary string_.

**Example 1:**

<pre>**Input:** a = "11", b = "1"
**Output:** "100"
</pre>

**Example 2:**

<pre>**Input:** a = "1010", b = "1011"
**Output:** "10101"
</pre>

**Constraints:**

*   `1 <= a.length, b.length <= 10<sup>4</sup>`
*   `a` and `b` consist only of `'0'` or `'1'` characters.
*   Each string does not contain leading zeros except for the zero itself.

### Solution 1 (array manipulation)
1. Add missing `0s` if the lengths of strings are different.
2. Loop through each element (from any of strings as they have the same length)
3. Find int sum of: `a[i] + b[i] + carry`. Where `carry` is carry bit from previous iteration.
4. Final bit value would be `sum % 2`, carry value would be `sum // 2`
5. Add final bit to result array
6. After loop is finished and `carry == 1`, add one more bit to result array.
7. Reverse array and print all elements.

### Solution 2 (int sum)
1. Convert `a` and `b` to int from binary string.
2. Find int sum: `a + b`
3. Print result as binary: 
   ```python
   return f'{result:b}'
   ```

### Solution 3 (bit manipulation)
1. Convert `a` and `b` to int from binary string.
2. Iterate while `carry > 0` 
3. Each time perform [binary addition](https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/).
4. Print result as binary: 
   ```python
   return f'{result:b}'
   ```
</details>

<!-----------------------------------------------------------------------------
-- 118. Pascal's Triangle
------------------------------------------------------------------------------>
<details>
<summary><b>118. Pascal's Triangle</b>
<a href="python/118-pascals-triangle/main.py">[python]</a>
</summary>
<br />

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example 1:**

<pre>**Input:** numRows = 5
**Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre>

**Example 2:**

<pre>**Input:** numRows = 1
**Output:** [[1]]
</pre>

**Constraints:**

*   `1 <= numRows <= 30`

### Solution
1. Create empty result list
2. Loop each row and element
3. First and last elements are `1`
4. Middle elements are sum of elements on previous row:
   ```python
   list[row][idx] = list[row - 1][idx - 1] + list[row - 1][idx]
   ```

</details>

<!-----------------------------------------------------------------------------
-- 119. Pascal's Triangle
------------------------------------------------------------------------------>
<details>
<summary><b>119. Pascal's Triangle II</b>
<a href="python/119-pascals-triangle-ii/main.py">[python]</a>
</summary>
<br />

[Leetcode Link](https://leetcode.com/problems/pascals-triangle-ii/)

Given an integer `rowIndex`, return the `rowIndex<sup>th</sup>` (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example 1:**

<pre>**Input:** rowIndex = 3
**Output:** [1,3,3,1]
</pre>

**Example 2:**

<pre>**Input:** rowIndex = 0
**Output:** [1]
</pre>

**Example 3:**

<pre>**Input:** rowIndex = 1
**Output:** [1,1]
</pre>

**Constraints:**

*   `0 <= rowIndex <= 33`

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?

### Solution 1 (Brute Force).
1. Generating all rows up to the row we are looking for.
2. Returning the last row.

### Solution 2 (Math)
There is a formula that can be used to calculate any element in the Pascal's 
triangle (except first and last, they are `1`).

```
n! / (k! * (n - k)!)
```

If to take this formula into consideration, we can find the coefficient of 
dependency between previous and current element. This can simplify the formula 
and avoid calculations of factorials.

```
n! / (k! * (n - k)!)
--- divide to ----------------------  => (n - k + 1) / k
n! / ((k-1)! * (n - (k-1))!)
```

Using this formula we can derive the current n-row value (k) using the previous 
value (k-1).

```
n(k) = n(k-1) * ((n - k + 1) / k)
```

Or something like that, where `i`
is the index of element in row, and `rowIndex` indicates row:

```python
result[i-1] * (rowIndex - i + 1) // i
```

</details>

<!-----------------------------------------------------------------------------
-- 121. Best Time to Buy and Sell Stock
------------------------------------------------------------------------------>
<details>
<summary><b class = "easy">121.</b> Best Time to Buy and Sell Stock</b>
   <a href="python/121-best-time-to-buy-and-sell-stock/solution.py">[python]</a>
</summary>
<br />

[LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i<sup>th</sup>` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

**Example 1:**

<pre>**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

**Example 2:**

<pre>**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.
</pre>

**Constraints:**

*   `1 <= prices.length <= 10<sup>5</sup>`
*   `0 <= prices[i] <= 10<sup>4</sup>`

### Solution [[python](python/121-best-time-to-buy-and-sell-stock/solution.py)]
1. Create pointers for `min_price` and `profit`. Assigning first element to `min_price`.
2. Loop through each element
   1. If the `price` of current element is lower than `min_price` - updating `min_price`.
   2. If difference between current `price` and `min_price` is more than previously registered `profit` - updating `profit`.
3. Returning `profit`.

</details>

<!-----------------------------------------------------------------------------
-- 167. Two Sum II - Input array is sorted
------------------------------------------------------------------------------>
<details>
<summary><b>167. Two Sum II - Input array is sorted</b>
<a href="python/167-two-sum-ii-input-array-is-sorted/solution.py">[python]</a>
</summary>
<br />

Given a **1-indexed** array of integers `numbers` that is already **_sorted in non-decreasing order_**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index<sub>1</sub>]` and `numbers[index<sub>2</sub>]` where `1 <= index<sub>1</sub> < index<sub>2</sub> <= numbers.length`.

Return _the indices of the two numbers,_ `index<sub>1</sub>` _and_ `index<sub>2</sub>`_, **added by one** as an integer array_ `[index<sub>1</sub>, index<sub>2</sub>]` _of length 2._

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

**Example 1:**

<pre>**Input:** numbers = [<u>2</u>,<u>7</u>,11,15], target = 9
**Output:** [1,2]
**Explanation:** The sum of 2 and 7 is 9\. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2\. We return [1, 2].
</pre>

**Example 2:**

<pre>**Input:** numbers = [<u>2</u>,3,<u>4</u>], target = 6
**Output:** [1,3]
**Explanation:** The sum of 2 and 4 is 6\. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3\. We return [1, 3].
</pre>

**Example 3:**

<pre>**Input:** numbers = [<u>-1</u>,<u>0</u>], target = -1
**Output:** [1,2]
**Explanation:** The sum of -1 and 0 is -1\. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2\. We return [1, 2].
</pre>

**Constraints:**

*   `2 <= numbers.length <= 3 * 10<sup>4</sup>`
*   `-1000 <= numbers[i] <= 1000`
*   `numbers` is sorted in **non-decreasing order**.
*   `-1000 <= target <= 1000`
*   The tests are generated such that there is **exactly one solution**.

### Solution (two pointers)
1. Creating two pointers: one refers to the beginning of list, other one to the 
   end: `i = 0`, `j = len(numbers) - 1`
2. Loop through each element
3. If sum of `numbers[i]` and `numbers[j]` equals to target, then returning 
   indexes (with +1).
4. If more than `target`, moving right side to the left: `j -= 1`
5. Otherwise, moving left side to the right: 'i += 1' until we find the answer.

### Solution (binary search)
1. Creating two pointers: one refers to the beginning of list, other one to the 
   end: `i = 0`, `j = len(numbers) - 1`

</details>

<!-----------------------------------------------------------------------------
-- 189. Rotate Array
------------------------------------------------------------------------------>
<details>
<summary><b>189. Rotate Array - [Medium]</b>
   <a href="python/189-rotate-array/solution_move.py">[python]</a>
</summary>
<br />

[Leetcode Link](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

<pre>**Input:** nums = [1,2,3,4,5,6,7], k = 3
**Output:** [5,6,7,1,2,3,4]
**Explanation:**
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

**Example 2:**

<pre>**Input:** nums = [-1,-100,3,99], k = 2
**Output:** [3,99,-1,-100]
**Explanation:** 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

**Constraints:**

*   `1 <= nums.length <= 10<sup>5</sup>`
*   `-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1`
*   `0 <= k <= 10<sup>5</sup>`

**Follow up:**

*   Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
*   Could you do it in-place with `O(1)` extra space?

### Solution (moving to positions) [[python](python/189-rotate-array/solution_move.py)]
Idea is to move each element one by one into their new positions right away. For 
doing it we need to use one of the cells as a placeholder for the data.

1. Creating following variables:
    - `anchor`: index of the cell that we use as a placeholder for swapped data
    - `content`: index of the cell that we swap with `anchor`
2. Iterating through elements. Overall we need `n - 1` swaps.
3. Calculating new `content` index that we want to swap with `anchor`:
   ```python
   content = (content + k + len(nums)) % len(nums)
   ```
4. If `anchor != content` then we need to swap `content` and `anchor` data.
5. Otherwise, we need to increment `anchor` and assign `content` to the anchor.
   
</details>

<!-----------------------------------------------------------------------------
-- 209. Minimum Size Subarray Sum
------------------------------------------------------------------------------>
<details>
<summary><b>209. Minimum Size Subarray Sum</b>
   <a href="python/209-minimum-size-subarray-sum/solution.py">[python]</a>
</summary>
<br />

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a **contiguous subarray** `[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

**Example 1:**

<pre>**Input:** target = 7, nums = [2,3,1,2,4,3]
**Output:** 2
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.
</pre>

**Example 2:**

<pre>**Input:** target = 4, nums = [1,4,4]
**Output:** 1
</pre>

**Example 3:**

<pre>**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Output:** 0
</pre>

**Constraints:**

*   `1 <= target <= 10<sup>9</sup>`
*   `1 <= nums.length <= 10<sup>5</sup>`
*   `1 <= nums[i] <= 10<sup>5</sup>`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

### [Solution (two pointers)](python/209-minimum-size-subarray-sum/solution.py)
Idea is to create two pointers that will track the beginning and the end of the 
window for which we calculate the sum of elements. If `sum < target` it means 
that we need to increase window (expand `end`). Otherwise, if we reached the 
target, we need to log the current window length, compare with current min 
window length, and shrink the window (move `start` to the left.)

Iterating till the moment when we reach the end: `end == len(nums)`.

</details>

<!-----------------------------------------------------------------------------
-- 344. Reverse String
------------------------------------------------------------------------------>
<details>
<summary><b>344. Reverse String</b>
   <a href="python/344-reverse-string/solution.py">[python]</a>
</summary>
<br />

Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

**Example 1:**

<pre>**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]
</pre>

**Example 2:**

<pre>**Input:** s = ["H","a","n","n","a","h"]
**Output:** ["h","a","n","n","a","H"]
</pre>

**Constraints:**

*   `1 <= s.length <= 10<sup>5</sup>`
*   `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

### Solution
1. Creating two pointers (`i = 0`, `j = len(s) - 1`) that guide us to the 
   beginning and to the end of the array.
2. Iterating while `i < j` (they will meet in the middle).
3. Swappoing the values:
   ```python
   s[i], s[j] = s[j], s[i]
   ```

</details>

<!-----------------------------------------------------------------------------
-- 359. Logger Rate Limiter
------------------------------------------------------------------------------>
<details>
<summary><b class = "easy">359.</b> Logger Rate Limiter</b>
   <a href="python/359-logger-rate-limiter/solution_dict.py">[python]</a>
</summary>
<br />

[LeetCode Link](https://leetcode.com/problems/logger-rate-limiter/)

Design a logger system that receives a stream of messages along with their timestamps. Each **unique** message should only be printed **at most every 10 seconds** (i.e. a message printed at timestamp `t` will prevent other identical messages from being printed until timestamp `t + 10`).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the `Logger` class:

*   `Logger()` Initializes the `logger` object.
*   `bool shouldPrintMessage(int timestamp, string message)` Returns `true` if the `message` should be printed in the given `timestamp`, otherwise returns `false`.

**Example 1:**

```java
**Input**
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
**Output**
[null, true, true, false, false, false, true]

**Explanation**
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
```

**Constraints:**

*   `0 <= timestamp <= 10<sup>9</sup>`
*   Every `timestamp` will be passed in non-decreasing order (chronological order).
*   `1 <= message.length <= 30`
*   At most `10<sup>4</sup>` calls will be made to `shouldPrintMessage`.

### Solution (Queue + Set) [[python](python/359-logger-rate-limiter/solution_queue_set.py)]
1. Creating class attributes:
    - `messages` (Set) for logging unique messages.
    - `queue` (Queue) for logging message queue in chronological order. The last 
      element of `queue` will contain the "oldest" message.
2. Removing old messages from `messages` and `queue` by taking the last message 
   timestamp until we find the message with age that is less than threshold.
3. If input `message` exists in `messages`, returning `False`.
4. Adding `message` and `timestamp` to `queue` and `messages`.
5. Returning `True`
   
### Solution (Dict) [[python](python/359-logger-rate-limiter/solution_dict.py)]
1. Creating class attributes:
    - `messages` (Dict) for logging unique messages and tyhe latest timestamp.
2. If `message` is in `messages` and entry is not too old, then returning `False`.
3. Otherwise, 
   1. Adding `messages[message] = timestamp`
   2. Returning `True`

</details>

<!-----------------------------------------------------------------------------
-- 394. Decode String
------------------------------------------------------------------------------>
<details>
<summary><b>394. Decode String (M)</b>
   <a href="python/394-decode-string/solution_recursive.py">[python]</a>
</summary>
<br />

[LeetCode Link](https://leetcode.com/problems/decode-string/)

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

**Example 1:**

<pre>**Input:** s = "3[a]2[bc]"
**Output:** "aaabcbc"
</pre>

**Example 2:**

<pre>**Input:** s = "3[a2[c]]"
**Output:** "accaccacc"
</pre>

**Example 3:**

<pre>**Input:** s = "2[abc]3[cd]ef"
**Output:** "abcabccdcdcdef"
</pre>

**Constraints:**

*   `1 <= s.length <= 30`
*   `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
*   `s` is guaranteed to be **a valid** input.
*   All the integers in `s` are in the range `[1, 300]`.

### [Solution (recursive)](python/394-decode-string/solution_recursive.py)
We will have main function `decodeString(self, s: str) -> str` and recursive 
`_parseExpression(s: str, cursor: int) -> Tuple`. The former will call the 
latter to initiate recursive processing from the beginning.

```python
  def decodeString(self, s: str) -> str:
    return _parseExpression(s, 0)[0]
```

1. Iterating through the input string `s` in scope of `_parseExpression`:
   0. Initializing the list of substrings `characters`.
   1. If symbol is digit, then building the number of repetiotions by adding to 
      the `s[i]` into the `repeat_digits` or by calculating `repeat` number 
      right away as: 
      ```python
      repeat = repeat * 10 + int(s[i])
      ```
   2. If `s[i] == '['`, it means we're entering the inner substring, ao we need 
      to repeat the inner substring `repeat` times. To identify inner substring, 
      we need to call recursive function `_parseExpression` with index `i + 1`.
      After it, appending the result to `characters`.
   3. If `s[i] == ']'`, it means that we already had processed the inner string, 
      so we need just combine all of the sunstrings.
   4. Else (if we found just string character), we're adding it to our 
      `characters` list.
2. Returning `(''.join(characters), i+1)`.

### [Solution (stack)](python/394-decode-string/solution_stack.py)
1. Defining:
   ```python
   result_string = [] # will contain final string.
   repeat = 0 # number of repeats for the substring.
   stack = [] # stack of the entries.
   ```
2. Iterating through characters `c` in `s`:
   1. `c.isdigit()`: calculating number of repeats. If there are few consequtive 
       digits in `s` we can do: `repeat = repeat * 10 + int(c)`
   2. `c == '['`: it means we will have one more level, so need to add into a 
      stack number of repeats + current `result_string` for this new entry and 
      resetting the `repeat` and `result_string`.
   3. `c == ']'`: closing entry. We need to take from the stack the number of 
      repetiotions and previous string. Concatenating it with current 
      `result_string`: 
      ```python
      result_string = [last_value + repetitions * ''.join(result_string)]
      ```
   4. Else (when `c` is char). Appending to `result_string`.
3. Returning `result_string` as `''.join(result_string)`.

<!-----------------------------------------------------------------------------
-- 485. Max Consecutive Ones
------------------------------------------------------------------------------>
<details>
<summary><b>485. Max Consecutive Ones</b>
   <a href="python/485-max-consecutive-ones/solution.py">[python]</a>
</summary>
<br />

Given a binary array `nums`, return _the maximum number of consecutive_ `1`_'s in the array_.

**Example 1:**

<pre>**Input:** nums = [1,1,0,1,1,1]
**Output:** 3
**Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

**Example 2:**

<pre>**Input:** nums = [1,0,1,1,0,1]
**Output:** 2
</pre>

**Constraints:**

*   `1 <= nums.length <= 10<sup>5</sup>`
*   `nums[i]` is either `0` or `1`.

### [Solution](python/485-max-consecutive-ones/solution.py)
1. Creating two counters `max_reps`, `curr_reps`.
2. Iterating through elements.
3. Incrementing `curr_reps` if we encounter `1`, otherwise, assigning to 
   `max_reps` max of valiues `max(max_reps, curr_reps)`
4. Returning `max(max_reps, curr_reps)`

</details>

<!-----------------------------------------------------------------------------
-- 498. Diagonal Traverse
------------------------------------------------------------------------------>
<details>
<summary><b>498. Diagonal Traverse</b>
<a href="python/66-plus-one/main.py">[python]</a>
</summary>
<br/>

Given an `m x n` matrix `mat`, return _an array of all the elements of the array in a diagonal order_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)

<pre>**Input:** mat = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,4,7,5,3,6,8,9]
</pre>

**Example 2:**

<pre>**Input:** mat = [[1,2],[3,4]]
**Output:** [1,2,3,4]
</pre>

**Constraints:**

*   `m == mat.length`
*   `n == mat[i].length`
*   `1 <= m, n <= 10<sup>4</sup>`
*   `1 <= m * n <= 10<sup>4</sup>`
*   `-10<sup>5</sup> <= mat[i][j] <= 10<sup>5</sup>`

### Solution
1. If input array is empty, return as-is;
2. If input array has less than 2 columns or 2 rows, then just returning values as-is (combining them into one array).
3. Defining possible moves (vectors) from point ot point. There are only 4 of 
   them:
    - main directions: up-right (`[-1, 1]`), down-left (`[1, -1]`);
    - alternative 1: right (`[0, 1]`);
    - alternative 2: down (`[1, 0]`).
4. First (`0, 0`), second (`0, 1`) and last (`nrows-1`, `ncols-1`) elements are 
   known, so we can include first and second value into result array right away.
	 Last value will be included at the end.
5. Due to that we're starting from the 2nd element, our initial direction will 
   be down-left. Alternative vectors down and right (in exact order).
	 Adding these possble moves to the array that will be modified later when we 
	 change direction. `vectors = [[1, -1], [1, 0], [0, 1]]`
6. Iterating through the elements. Total number of iterations is `#elements - 3` 
   as we do not need to identify first, second and last elements. Our initial 
	 point will be the second element (`0, 1`).
7. For each vector from #5 we need to check if it will be a valid move. If yes, 
   then we apply new x and y, breaking the vector loop.
8. If not, then we need to note that direction should change, and continuing to 
   the next vector.
9. Eventually, one of three vectors should work, so appending value to result 
   array: `result_list.append(mat[x][y])`.
10. If `change_direction` flag is `True`, then we need to update the direction in
   vectors array:

	 ```python
	 vectors[0][0] *= -1
	 vectors[0][1] *= -1
	 ``` 

	 Example: if we move down-left, then starting from the next 
	 iteration we need to mobe up-right. 

	 Also, we need to swap order of alternative moves. 
	 Example, if we go down-left and come to the matrix edge, then we need to 
	 check alternative options counter-clockwise: down and then right. If we go up-right, then we need to check alternative options clockwise: right and then down.

	 ```python
	 vectors[1], vectors[2] = vectors[2], vectors[1]
	 ```

	  Final thing is to update the direction flag itself to `False`:

	  ```python
	  change_direction = False
	  ```
11. After iterating of all elements, adding the final one as described in #4 and
    returning result:

    ```python
    result_list.append(mat[-1][-1])
    ```

[Alternative solution](https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING)

</details>

<!-----------------------------------------------------------------------------
-- 561. Array Partition I 
------------------------------------------------------------------------------>
<details>
<summary><b>561. Array Partition I</b>
<a href="python/561-array-partition-i/solution.py">[python]</a>
</summary>
<br />

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a<sub>1</sub>, b<sub>1</sub>), (a<sub>2</sub>, b<sub>2</sub>), ..., (a<sub>n</sub>, b<sub>n</sub>)` such that the sum of `min(a<sub>i</sub>, b<sub>i</sub>)` for all `i` is **maximized**. Return _the maximized sum_.

**Example 1:**

<pre>**Input:** nums = [1,4,3,2]
**Output:** 4
**Explanation:** All possible pairings (ignoring the ordering of elements) are:
1\. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2\. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3\. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.</pre>

**Example 2:**

<pre>**Input:** nums = [6,2,6,5,1,2]
**Output:** 9
**Explanation:** The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
</pre>

**Constraints:**

*   `1 <= n <= 10<sup>4</sup>`
*   `nums.length == 2 * n`
*   `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`

### Solution
To get the biggest sum of pairs, we need to group elements in ascending order by 
their value. It means that the least valuable elements should be in pair with 
the least valuable elements. And the most valuable elements with the most 
valuable: `[1, 4, 6, 2, 3, 5] -> (1, 2), (3, 4), (5, 6)`.

1. Sort input array in ascending order.
2. Due to that array is sorted, min value will always be the first number in a 
   pair. So we can just iterate through all elements with even indexes and count 
   them into sum.

</details>
     
<!-----------------------------------------------------------------------------
-- 724. Find Pivot Index 
------------------------------------------------------------------------------>
<details>
<summary><b>724. Find Pivot Index</b>
<a href="python/724-find-pivot-index/main.py">[python]</a>
</summary>
<br />

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return _the **leftmost pivot index**_. If no such index exists, return -1.

**Example 1:**

<pre>**Input:** nums = [1,7,3,6,5,6]
**Output:** 3
**Explanation:**
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

**Example 2:**

<pre>**Input:** nums = [1,2,3]
**Output:** -1
**Explanation:**
There is no index that satisfies the conditions in the problem statement.</pre>

**Example 3:**

<pre>**Input:** nums = [2,1,-1]
**Output:** 0
**Explanation:**
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

**Constraints:**

*   `1 <= nums.length <= 10<sup>4</sup>`
*   `-1000 <= nums[i] <= 1000`

**Note:** This question is the same as 1991: [https://leetcode.com/problems/find-the-middle-index-in-array/](https://leetcode.com/problems/find-the-middle-index-in-array/)

### Solution
1. Find sum of all elements
2. Loop through the list of elements and:
    - compare the sum of elements to the left of current element with (total sum - current element - left sum)
    - if equal -> return index
    - otherwise, increment left sum += element  

</details>  

<!-----------------------------------------------------------------------------
-- 747. Largest Number At Least Twice of Others
------------------------------------------------------------------------------>
<details>
<summary><b>747. Largest Number At Least Twice of Others</b>
<a href="python/747-largest-number-at-least-twice-of-others/main.py">[python]</a>
</summary>
<br />

You are given an integer array `nums` where the largest integer is **unique**.

Determine whether the largest element in the array is **at least twice** as much as every other number in the array. If it is, return _the **index** of the largest element, or return_ `-1` _otherwise_.

**Example 1:**

<pre>**Input:** nums = [3,6,1,0]
**Output:** 1
**Explanation:** 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
</pre>

**Example 2:**

<pre>**Input:** nums = [1,2,3,4]
**Output:** -1
**Explanation:** 4 is less than twice the value of 3, so we return -1.</pre>

**Example 3:**

<pre>**Input:** nums = [1]
**Output:** 0
**Explanation:** 1 is trivially at least twice the value as any other number because there are no other numbers.
</pre>

**Constraints:**

*   `1 <= nums.length <= 50`
*   `0 <= nums[i] <= 100`
*   The largest element in `nums` is unique.

### Solution
1. Loop through the elements
2. If length == 0, return -1
3. If length == 1, return 0
4. If index == 0, setting max
5. If element > max: setting second_max with max value and resetting max
6. If index == 1 or element > second_max: setting second max
7. If second_max == 0 or max / second_max >= 2 -> return max_index
8. return -1

</details>  

<!-----------------------------------------------------------------------------
-- 977. Squares of a Sorted Array
------------------------------------------------------------------------------>
<details>
<summary><b class = "easy">977.</b> Squares of a Sorted Array</b>
   <a href="python/977-squares-of-a-sorted-array/solution_two_pointers.py">[python]</a>
</summary>
<br />

[LeetCode Link](https://leetcode.com/problems/squares-of-a-sorted-array/)

Given an integer array `nums` sorted in **non-decreasing** order, return _an array of **the squares of each number** sorted in non-decreasing order_.

**Example 1:**

<pre>**Input:** nums = [-4,-1,0,3,10]
**Output:** [0,1,9,16,100]
**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

**Example 2:**

<pre>**Input:** nums = [-7,-3,2,3,11]
**Output:** [4,9,9,49,121]
</pre>

**Constraints:**

*   `<span>1 <= nums.length <=</span> 10<sup>4</sup>`
*   `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`
*   `nums` is sorted in **non-decreasing** order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

### Solution (Brute Force) [[python](python/977-squares-of-a-sorted-array/solution_brute_force.py)]
Idea is that we're moving from the beginning of the array and adding all negative numbers into array.
During processing of the positive numbers we are checking if current positive 
number is greater than the last added negative (if tehre are any negative numbers).
If there are, then firstly adding to result array quads from negative list and 
then adding quad of positive.

At the end, if we still have negative numbers in array, we're adding them to the 
end of result array.

### Solution (Two Pointers) [[python](python/977-squares-of-a-sorted-array/solution_two_pointers.py)]
1. Creating few variables:
    - `squares` (Queue) for keeping result squares and having the possibility to add values to the beginng of the array.
    - `left` and `right` pointers to the `0` and last element respectively.
2. While `left < right` iterating through the elements:
   1. If `abs(nums[right]) > abs(nums[left])` then adding `nums[right]**2` to 
      `squares` and shifting `right` to the left.
   2. Otherwise, adding `nums[left]**2` to `squares` and shifting `left` to the 
      right.
3. At the end, if we have one element left (`left == right`), adding it as well: 
   `squares.appendleft(nums[left]**2)`
4. Returning result array: `list(squares)`

</details>


<!-----------------------------------------------------------------------------
-- 1991. Find the Middle Index in Array
------------------------------------------------------------------------------>
<details>
<summary><b>1991. Find the Middle Index in Array</b>
   <a href="python/1991-find-the-middle-index-in-array/main.py">[python]</a>
</summary>
<br />

Given a **0-indexed** integer array `nums`, find the **leftmost** `middleIndex` (i.e., the smallest amongst all the possible ones).

A `middleIndex` is an index where `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]`.

If `middleIndex == 0`, the left side sum is considered to be `0`. Similarly, if `middleIndex == nums.length - 1`, the right side sum is considered to be `0`.

Return _the **leftmost**_ `middleIndex` _that satisfies the condition, or_ `-1` _if there is no such index_.

**Example 1:**

<pre>**Input:** nums = [2,3,-1,<u>8</u>,4]
**Output:** 3
**Explanation:**
The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
</pre>

**Example 2:**

<pre>**Input:** nums = [1,-1,<u>4</u>]
**Output:** 2
**Explanation:**
The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
</pre>

**Example 3:**

<pre>**Input:** nums = [2,5]
**Output:** -1
**Explanation:**
There is no valid middleIndex.
</pre>

**Example 4:**

<pre>**Input:** nums = [<u>1</u>]
**Output:** 0
**Explantion:**
The sum of the numbers before index 0 is: 0
The sum of the numbers after index 0 is: 0
</pre>

**Constraints:**

*   `1 <= nums.length <= 100`
*   `-1000 <= nums[i] <= 1000`

**Note:** This question is the same as 724: [https://leetcode.com/problems/find-pivot-index/](https://leetcode.com/problems/find-pivot-index/)

### Solution
1. Find sum of all elements
2. Loop through the list of elements and:
    - compare the sum of elements to the left of current element with (total sum - current element - left sum)
    - if equal -> return index
    - otherwise, increment left sum += element  

</details>  



