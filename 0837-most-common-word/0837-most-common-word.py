class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = ['!', '?', ',', ';', '.', "'"]
        for p in punctuations:
            paragraph = paragraph.replace(p, " ")
        words = paragraph.split()
        d = {}
        for i in words:
            s = i.lower()
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        fre = "" 
        max1 = 0
        for k, v in d.items():
            if v > max1 and k not in banned:
                fre = k
                max1 = v
        return fre
