import dis

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:

    # Returning "0" on empty needle.
    if not needle:
      return 0

    h_len = len(haystack)
    n_len = len(needle)
    h_idx = 0

    while h_idx < h_len:
      print(f'[{h_idx}]: {haystack[h_idx]}')

      # If haven't found match till that time, there is no sense to proceed.
      if h_idx + n_len > h_len:
        return -1 

      # Indicates if loop was interrupted. If not, it means that we found a 
      # match.
      search_broken = False

      for n_idx in range(n_len):
        h_idx_shifted = h_idx + n_idx

        if haystack[h_idx_shifted] != needle[n_idx]:
          search_broken = True
          break

      if not search_broken:
        return h_idx

      h_idx += 1

    return -1

f = Solution()

# haystack = 'a'*100000 + "b"
# needle = 'a'*10000 + "b"
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

haystack = 'a'*10 + "b"
needle = 'a'*2 + "b"
print(f'Input: haystack = "{haystack}", needle = "{needle}"')
print(f'Answer: {f.strStr(haystack, needle)}')

# haystack = "hello"
# needle = "ll"
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

# haystack = "hello"
# needle = "lo"
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

# haystack = "hello"
# needle = "l"
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

# haystack = "mississippi"
# needle = "issip"
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

# haystack = "aaaaa"
# needle = "bba"
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

# haystack = "aaaaa"
# needle = ""
# print(f'Input: haystack = "{haystack}", needle = "{needle}"')
# print(f'Answer: {f.strStr(haystack, needle)}')

# dis.dis(f.addBinary)