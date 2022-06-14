class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_list = []
        for char in s:
            if char not in cur_list:
                cur_list.append(char)
                cur_len = len(cur_list)
                if cur_len > max_len:
                    max_len = cur_len
            else:
                i = cur_list.index(char)
                cur_list = cur_list[i+1:] + [char]
        return max_len
        