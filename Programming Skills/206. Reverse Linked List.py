class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        prev = None
        current = head
        
        while current:
            next_node = current.next  
            current.next = prev  
            prev = current  
            current = next_node  
        return prev

if __name__ == "__main__":
    
   def createList(values):
       dummy = ListNode()
       current = dummy
       for val in values:
           current.next = ListNode(val)
           current = current.next
       return dummy.next
   List = [1,2,3]

   head = createList(List)
   sol = Solution()

   result = sol.reverseList(head)

#    print(value.next.next.val)

