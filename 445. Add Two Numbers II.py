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

        Number_String1 = ''
        Number_String2 = ''
        
        while l1:
            Number_String1 += str(l1.val) 
            l1 = l1.next 
        
        while l2:
            Number_String2+=str(l2.val)
            l2 = l2.next
 
        num = int(Number_String1)+int(Number_String2)
        num = str(num)
        numlist = []
        
        for n in num:
            numlist.append(int(n))
    
        dummy = ListNode()
        current = dummy

        for l in numlist:
            current.next = ListNode(l)
            current =  current.next
        return dummy.next

if __name__ == "__main__":

    sol = Solution()
    
    l1 = [7,2,4,3]
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

    while result:
        print(result.val)
        result = result.next

    