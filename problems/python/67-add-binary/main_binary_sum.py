class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        # Converting string bit number into int number.
        a_int = int(a, 2)
        b_int = int(b, 2)
        
        # Performing binary addition until carry number (b_int) is 0.
        # https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
        while b_int:
          carry = a_int & b_int
          result = a_int ^ b_int
          
          a_int = result
          b_int = carry << 1
        
        # Result starts from "0b" prefix, so we want to not print it. 
        return bin(a_int)[2:]

f = Solution()

a = '11'
b = '1'
print(f'Input: a = "{a}", b = "{b}"')
print(f'Answer: {f.addBinary(a, b)}')

a = '1010'
b = '1011'
print(f'Input: a = "{a}", b = "{b}"')
print(f'Answer: {f.addBinary(a, b)}')