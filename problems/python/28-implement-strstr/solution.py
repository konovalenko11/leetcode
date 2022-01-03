import dis

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:

    # Returning "0" on empty needle.
    if not needle:
      return 0

    h_len = len(haystack)
    n_len = len(needle)

    for h_idx in range(h_len):
      for n_idx in range(n_len):
        h_idx_shifted = h_idx + n_idx

        # If not enough chars left in haystack to get the match, returning -1.
        if h_idx_shifted >= h_len:
          return -1

        # If chars does not match, then there is no sense to proceed.
        if haystack[h_idx_shifted] != needle[n_idx]:
          break

        if n_idx == n_len - 1:
          return h_idx

    return -1

f = Solution()

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