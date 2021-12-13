# Problem Descriptions

<details>
<summary><b>1991. Find the Middle Index in Array</b>
<a href="problems/python/1991-find-the-middle-index-in-array/main.py">[python]</a>
</summary>

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]`.

If `middleIndex == 0`, the left side sum is considered to be **0**. Similarly, if `middleIndex == nums.length - 1`, the right side sum is considered to be **0**0.

Return the leftmost `middleIndex` that satisfies the condition, or **-1** if there is no such index.

</details>  



