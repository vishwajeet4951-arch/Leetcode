class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich=0
        for customer in accounts:
            t=0
            for money in customer:
                t=t+money
            if t>rich:
                rich=t
        return rich
        