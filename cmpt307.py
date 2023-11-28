import pdb
import typing


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