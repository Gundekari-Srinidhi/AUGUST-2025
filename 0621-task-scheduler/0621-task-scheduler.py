class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        max_freq = 0
        for val in d.values():
            if val > max_freq:
                max_freq = val
        max_count = 0
        for val in d.values():
            if val == max_freq:
                max_count += 1
        return max(len(tasks), (max_freq-1 ) * (n +1) + max_count)

        