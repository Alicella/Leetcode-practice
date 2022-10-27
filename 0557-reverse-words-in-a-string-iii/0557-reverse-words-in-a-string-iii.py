class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = r = 0
        s += ' '
        s_reversed = ''
        
        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                s_reversed += s[l: r+1][::-1]
                r += 1
                l = r
                
        return s_reversed[1:]
        
        
        
        
        # return " ".join([word[::-1] for word in s.split()])
        
        # split the string by whitespace, into a list
        sentence_li = s.split(" ")
        new_li = []
        for word in sentence_li:
            word_li = list(word)
            
            # reverse each word
            l, r = 0, len(word_li) - 1
            while l <= r:
                word_li[l], word_li[r] = word_li[r], word_li[l]
                l += 1
                r -= 1
            new_word = ''.join(word_li)
            
            # put each reversed word into the new list
            new_li.append(new_word)
        
        return ' '.join(new_li)
        
       