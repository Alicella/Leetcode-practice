class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0
        tbd = {}
        
        # turn string to list, for later mumtation
        s = list(secret)
        g = list(guess)

        # iterate through secret and guess, find all bulls and
        # store non-bulls letters to a dictionary tbd
        for i in range(len(s)):
            if s[i] == g[i]:
                bulls += 1
                g[i] = '#'
            else:
                tbd[s[i]] = 1 + tbd.get(s[i], 0)
        
        # iterate through guess, find all cows
        for i in range(len(g)):
            if g[i] in tbd:
                cows += 1
                tbd[g[i]] -= 1
                if tbd[g[i]] == 0:
                    tbd.pop(g[i])
         
        return str(bulls) + 'A' + str(cows) + 'B'