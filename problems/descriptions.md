# Problem Descriptions


<!-----------------------------------------------------------------------------
-- 14. Longest Common Prefix
------------------------------------------------------------------------------>
<details>
<summary><b>14. Longest Common Prefix</b>
   <a href="python/28-implement-strstr/solution.py">[python]</a>
</summary>
<br />

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



