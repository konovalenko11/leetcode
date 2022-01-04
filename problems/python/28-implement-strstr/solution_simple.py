import dis

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    return haystack.find(needle) if needle else 0

f = Solution()

haystack = 'a'*100000 + "b"
needle = 'a'*10000 + "b"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = 'a'*100 + "b"
needle = 'a'*10 + "b"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = "hello"
needle = "ll"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = "hello"
needle = "lo"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = "hello"
needle = "l"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = "mississippi"
needle = "issip"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = "aaaaa"
needle = "bba"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

haystack = "aaaaa"
needle = ""
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

# dis.dis(f.addBinary)