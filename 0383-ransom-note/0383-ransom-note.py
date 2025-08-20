class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n=len(ransomNote)
        count=0
        l=list(magazine)
        for i in ransomNote:
            if i in l:
                count+=1
                l.remove(i)
        return count==n