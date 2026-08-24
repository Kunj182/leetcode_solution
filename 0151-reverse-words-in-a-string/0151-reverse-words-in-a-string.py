class Solution:
    def reverseWords(self, s: str) -> str:
        strip = s.strip()
        arr = strip.split()
        i = 0
        j = len(arr)-1
        while i<j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1
        return " ".join(arr)