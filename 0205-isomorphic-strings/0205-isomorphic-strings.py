class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for sc, tc in zip(s, t):
            if (s_map.get(sc, tc) != tc) or (t_map.get(tc, sc) != sc):
                return False
            s_map[sc] = tc
            t_map[tc] = sc

        return True