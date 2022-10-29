class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        dict1 = {}
        dict2 = {}
        for char in s1:
            dict1[char] = dict1.get(char, 0) + 1
        
        for l in range(len(s2) - len(s1) + 1):
            r = l + len(s1) - 1
            for char in s2[l:r+1]:
                if char not in dict1:
                    dict2 = {}
                    break
                else:
                    dict2[char] = dict2.get(char, 0) + 1
                    
            if dict2 == dict1:
                print(dict1)
                print(dict2)
                return True
            else:
                dict2 = {}
        
        # return False