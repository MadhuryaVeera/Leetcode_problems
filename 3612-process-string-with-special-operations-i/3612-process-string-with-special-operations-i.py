class Solution:
    def processStr(self, s: str) -> str:
        res =[] # list method 2
        for ch in s:
            if ch.isalpha():
                res.append(ch)
            elif ch=="*":
                if res:
                    res.pop()
            elif ch=="#":
                res.extend(res)
            else:
                res.reverse()
        return "".join(res)
        