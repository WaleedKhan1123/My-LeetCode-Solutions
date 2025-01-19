# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry =0 

        while l1:
            l1 = l1.next
             


if __name__ == "__main__":

    sol = Solution()
    
    l1 = [2,4,3]
    
    l2 = [5,6,4]
    
    def createLinkedList(list):
        dummy = ListNode()
        current = dummy
        for l in list:

            current.next = ListNode(l)
            current =  current.next
        return dummy.next
            
    l1 = createLinkedList(l1)
    l2 = createLinkedList(l2)
    result = sol.addTwoNumbers(l1,l2)

