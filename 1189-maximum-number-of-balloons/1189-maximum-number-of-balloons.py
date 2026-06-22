class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count={} # dictionary to store the frequencyh of an elements in it 

        for ch in text:
            count[ch]=count.get(ch,0)+1

        b=count.get('b',0)
        a=count.get('a',0)
        l=count.get('l',0)//2     # // give without deciamal like 3
        o=count.get('o',0)//2  # / gives with decimal  like 3.5
        n=count.get('n',0)

        return min(b,a,l,o,n)   # if b=5,a=6,l=8,o=2,n=1   then ballon it forms one so we taking minimum from that only 
