class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            t=0
            while n>0:
                l=n%10
                t=t+l**2
                n=n//10
            n=t
        return True
        