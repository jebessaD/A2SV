class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict=Counter(s)
        t_dict=Counter(t)

        for i in t_dict:
            if i not in s or t_dict[i]>s_dict[i]:
                return i

