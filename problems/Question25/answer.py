class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse pointer
            prev = current            # Move prev to current
            current = next_node       # Move to next node
        
        return prev  # New head