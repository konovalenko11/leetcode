from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    i = 0
    # j = len(s) - 1

    # while (i < j):
    for i in range(len(s) // 2):
      s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

      # i += 1
      # j -= 1

f = Solution()

s = ["h","e","l","l","o"]
print(f'Input: {s}')
f.reverseString(s)
print(f'Answer: {s}')

s = list("1234")
print(f'Input: {s}')
f.reverseString(s)
print(f'Answer: {s}')