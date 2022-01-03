class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        # Converting string bit number into int number.
        a_int = int(a, 2)
        b_int = int(b, 2)
        
        # Result starts from "0b" prefix, so we want to not print it. 
        return f'{a_int + b_int:b}'

f = Solution()

a = '11'
b = '1'
print(f'Input: a = "{a}", b = "{b}"')
print(f'Answer: {f.addBinary(a, b)}')

a = '1010'
b = '1011'
print(f'Input: a = "{a}", b = "{b}"')
print(f'Answer: {f.addBinary(a, b)}')