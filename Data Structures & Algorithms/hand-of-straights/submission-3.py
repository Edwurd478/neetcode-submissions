"""
sort the array
[1, 2, 2, 3, 3, 4, 4, 5]

hash map:
{1: 1, 2: 2, 3: 2, 4: 2, 5: 1}
try each starting digit 1 -> 1000, go as high as you can consecutively while subtracting one from each digit in the hash map
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        digits = {}
        for num in hand:
            digits[num] = digits.get(num, 0) + 1
        
        for digit in range(0, 1001):
            while digit in digits:
                if not digits:
                    return True
                for i in range(digit, digit+groupSize):
                    if i not in digits:
                        if i == digit:
                            break
                        else:
                            return False
                    digits[i] -= 1
                    if digits[i] == 0:
                        del digits[i]
        
        return True