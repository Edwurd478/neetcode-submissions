class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while fast == 0 or fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        slow2 = 0
        while slow != slow2:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow
        
        
        """
        fast = head
        slow = head
        ans = -1
        while fast.val != slow.val:
            fast = fast.next.next
            slow = slow.next
            if not slow:
                slow = head
            if not fast or not fast.next:
                fast = head
            
            if fast.val == slow.val:
                ans = fast.val
        
        return ans
        """