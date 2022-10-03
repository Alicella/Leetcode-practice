class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = {}
        
        for word in words:
            d[word] = 1 + d.get(word, 0)
            
        res = sorted(d, key = lambda word: (-d[word], word))
        
        return res[:k]