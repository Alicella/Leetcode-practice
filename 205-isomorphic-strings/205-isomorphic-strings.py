class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # mapping is implemented by a dictionary
        # the same char in s can only map to another char in t,
        # consisting a key-value pair in the mapping dic
        # the mapping relationship is unique
        # what corner cases to check?
        
        mapping = {}
        for i in range(len(s)):
            char_k = s[i]
            char_v = t[i]
            
            if char_k not in mapping:
                if char_v in mapping.values():
                    return False
                mapping[char_k] = char_v
              
            elif mapping[char_k] != char_v:
                return False
        
        return True
            
                
        