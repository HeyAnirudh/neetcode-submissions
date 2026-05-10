class Solution:
    def merge(self, inte: List[List[int]]) -> List[List[int]]:
        inte.sort(key=lambda x :x[0])
        res=[inte[0]]

        for start , end in inte[1:]:
            lastend=res[-1][1]

            if start <= lastend:
                res[-1][1]=max(lastend,end)
            else:
                res.append([start,end])

        return res

        