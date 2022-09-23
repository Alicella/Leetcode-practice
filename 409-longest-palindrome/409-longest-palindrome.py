class Solution:
    def longestPalindrome(self, s: str) -> int:
        # thinking:
        # palindrome needs 0/1 unique letter and 
        # 2n identicle letter pairs
        # the length = 2n or 2n + 1
        # solve using hash table/dictionary
        
#         counts = {}
#         for char in s:
#             if char in counts:
#                 counts[char] += 1
#             else:
#                 counts[char] = 1
        
#         length = 0
#         odd_count_exist = False
        
#         for count in counts.values():
#             if count % 2 == 0:
#                 length += count
#             else:
#                 length += count - 1
#                 odd_count_exist = True
        
#         if odd_count_exist:
#             length += 1
            
#         return length


        # use set()
        pairs = 0
        unpaired_chars = set()
        
        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        return pairs * 2 + 1 if unpaired_chars else pairs * 2