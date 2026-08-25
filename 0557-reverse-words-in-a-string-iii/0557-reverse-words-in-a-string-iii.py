class Solution:
    def reverseWords(self, s: str) -> str:
        s= " ".join([word[::-1] for word in s.split()])
        return s
        
            
            
