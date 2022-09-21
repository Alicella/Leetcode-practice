class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    # Thinking process:
        # mapping is implemented by a dictionary
        # the same char in s can only map to another char in t,
        # consisting a key-value pair in the mapping dic
        # the mapping relationship is unique

# using two dictionaries
        mapping_s_t = {}
        mapping_t_s = {}
        
        for i in range(len(s)):
            key_s = s[i]
            key_t = t[i]
            
            if key_s not in mapping_s_t and key_t not in mapping_t_s:
                    mapping_s_t[key_s] = key_t
                    mapping_t_s[key_t] = key_s
            elif mapping_s_t.get(key_s) != key_t or mapping_t_s.get(key_t) != key_s:
                return False

        
# 86ms answer using a dictionary and a list:        
#         mapping = {}
#         for i in range(len(s)):
#             char_k = s[i]
#             char_v = t[i]
            
#             if char_k not in mapping:
# # the key hasn't occured but values already exist, indicating wrong pairs
#                 if char_v in mapping.values():   # time consuming
#                     return False
                
#                 mapping[char_k] = char_v
              
#             elif mapping[char_k] != char_v:
#                 return False
        
        return True
            
                
        