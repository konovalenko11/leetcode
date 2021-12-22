# Problem Descriptions

<!-----------------------------------------------------------------------------
-- 54. Spiral Matrix
------------------------------------------------------------------------------>
<details>
<summary><b>54. Spiral Matrix</b>
<a href="python/54-spiral-matrix/main.py">[python]</a>
</summary>
<br />

</details>

<!-----------------------------------------------------------------------------
-- 66. Plus One
------------------------------------------------------------------------------>
<details>
<summary><b>66. Plus One</b>
<a href="python/66-plus-one/main.py">[python]</a>
</summary>
<br />
<div><p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>'s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> digits = [0]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>'s.</li>
</ul>

### Solution
1. Loop throught the digits in reverse order
2. If `digits[idx] == 9` then `digits[idx] = 0`
3. Else `digits[idx] += 1` and `return digits`
4. If you went throug sll elements, it means that the the most significant 
   element was 9, lso we need to add "1" at the beginning of an array:
   `[1] + digits`

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
<p>Given an array of integers <code>nums</code>, calculate the <strong>pivot index</strong> of this array.</p>

<p>The <strong>pivot index</strong> is the index where the sum of all the numbers <strong>strictly</strong> to the left of the index is equal to the sum of all the numbers <strong>strictly</strong> to the index's right.</p>

<p>If the index is on the left edge of the array, then the left sum is <code>0</code> because there are no elements to the left. This also applies to the right edge of the array.</p>

<p>Return <em>the <strong>leftmost pivot index</strong></em>. If no such index exists, return -1.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,7,3,6,5,6]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no index that satisfies the conditions in the problem statement.</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [2,1,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as&nbsp;1991:&nbsp;<a href="https://leetcode.com/problems/find-the-middle-index-in-array/" target="_blank">https://leetcode.com/problems/find-the-middle-index-in-array/</a></p>

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
<div><p>You are given an integer array <code>nums</code> where the largest integer is <strong>unique</strong>.</p>

<p>Determine whether the largest element in the array is <strong>at least twice</strong> as much as every other number in the array. If it is, return <em>the <strong>index</strong> of the largest element, or return </em><code>-1</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,6,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 4 is less than twice the value of 3, so we return -1.</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 1 is trivially at least twice the value as any other number because there are no other numbers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li>The largest element in <code>nums</code> is unique.</li>
</ul>
</div>

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
<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, find the <strong>leftmost</strong> <code>middleIndex</code> (i.e., the smallest amongst all the possible ones).</p>

<p>A <code>middleIndex</code> is an index where <code>nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]</code>.</p>

<p>If <code>middleIndex == 0</code>, the left side sum is considered to be <code>0</code>. Similarly, if <code>middleIndex == nums.length - 1</code>, the right side sum is considered to be <code>0</code>.</p>

<p>Return <em>the <strong>leftmost</strong> </em><code>middleIndex</code><em> that satisfies the condition, or </em><code>-1</code><em> if there is no such index</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,-1,<u>8</u>,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,-1,<u>4</u>]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [2,5]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no valid middleIndex.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> nums = [<u>1</u>]
<strong>Output:</strong> 0
<strong>Explantion:</strong>
The sum of the numbers before index 0 is: 0
The sum of the numbers after index 0 is: 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as&nbsp;724:&nbsp;<a href="https://leetcode.com/problems/find-pivot-index/" target="_blank">https://leetcode.com/problems/find-pivot-index/</a></p>

### Solution
1. Find sum of all elements
2. Loop through the list of elements and:
    - compare the sum of elements to the left of current element with (total sum - current element - left sum)
    - if equal -> return index
    - otherwise, increment left sum += element  

</details>  



