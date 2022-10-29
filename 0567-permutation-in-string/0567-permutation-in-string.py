class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #https://www.youtube.com/watch?v=UbyhOgBN834&ab_channel=NeetCode
        if len(s2) < len(s1): return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            # ord function get the ASCII value of the character
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            l += 1
        
        return matches == 26
        
        
        
        
        
        
        
        
        
        
        #O(len(s1) * len(s2))
#         if len(s2) < len(s1):
#             return False
        
#         dict1 = {}
#         dict2 = {}
#         for char in s1:
#             dict1[char] = dict1.get(char, 0) + 1
        
#         for l in range(len(s2) - len(s1) + 1):
#             r = l + len(s1) - 1
#             for char in s2[l:r+1]:
#                 if char not in dict1:
#                     dict2 = {}
#                     break
#                 else:
#                     dict2[char] = dict2.get(char, 0) + 1
                    
#             if dict2 == dict1:
#                 return True
#             else:
#                 dict2 = {}
        
#         return False