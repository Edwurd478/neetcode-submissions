class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins_left = n
        step_size = 1
        while coins_left >= step_size:
            coins_left -= step_size
            step_size += 1
        return step_size-1