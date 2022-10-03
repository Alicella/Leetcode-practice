class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return self.stack(s, []) == self.stack(t, [])
        
    
    def stack(self, s, stack):
        for char in s:
            if char != "#":
                stack.append(char)
            else:
                if not stack: continue
                stack.pop()
        return stack