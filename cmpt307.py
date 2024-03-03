import pdb
import typing
import math
from pprint import pformat


class Solution:

    def lifeBoat(self, arr: typing.List[int], maxWeight: int) -> int:
        arr.sort()
        boat = 0
        i = 0
        for j in reversed(range(len(arr))):
            if arr[i] + arr[j] <= maxWeight and i < j:
                i += 1
            boat += 1
            if (i >= j):
                break
        return boat
    
    def printdp(self, dp: typing.List[int]) -> None:
        for i,value in enumerate(dp):
            print(i, value)

    def subsetSum(self, S: typing.List[int], t: int) -> tuple:
        """
        Let S be a set of n dist. pos. int., and let t be a pos. int. Devise an algo. that determines, with O(nt) operations in the worst case
        if there exists a subset of S whose element total t

        @params
            S: list of distinct, positive integers
            total: a positive int
        @return
            True if its existed a subset of S that its sum is equalled to t
        """  
        S.sort()
        S_len = len(S)
        dp = [[False for _ in range(t+1)] for _ in range(S_len+1)]
        for i in range(S_len+1):
            dp[i][0] = True
        for i in range(1, S_len+1):         # i is first ith coin you can use to make j
            for j in range(1, t+1):         # j is sum value
                if S[i-1] <= j:             # check out of range for dp[i-1][j-S[i-1]]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-S[i-1]]
                else:
                    dp[i][j] = dp[i-1][j] 
        return dp[S_len][t]        

    def find_minumum_bribe(self, lower: int, upper: int, init: int, min_bribe: int) -> int:
        total_cost = 0
        lower_limit = lower
        upper_limit = upper
        mid = 84
        # pdb.set_trace()
        while lower_limit < upper_limit:
            total_cost += mid
            if mid >= min_bribe:
                upper_limit = mid - 1
            else:
                lower_limit = mid + 1
            mid = math.ceil((lower_limit + upper_limit) / 2)
        total_cost += mid
        return total_cost
