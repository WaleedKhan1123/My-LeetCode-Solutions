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
        print(f"l1 is {l1} l2 is {l2}")    


if __name__ == "__main__":

    sol = Solution()
    
    l1 = [2,4,3]
    
    l2 = [5,6,4]
    
    def createLinkedList(list):
        ind = 0
        dummy = ListNode()
        current = dummy
        while current!=None:
          
            current.val = list[ind]
            current = current.next
            ind+=1
        return dummy.next
            
    dummy = createLinkedList(l1)
    print(dummy)
    result = sol.addTwoNumbers(l1,l2)

