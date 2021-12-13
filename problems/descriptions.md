# Problem Descriptions

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

</details>  



