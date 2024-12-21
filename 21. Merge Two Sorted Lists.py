# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        comlist = []
        while list1:
            comlist.append(list1.val)
            list1 = list1.next
        while list2:
            comlist.append(list2.val)
            list2 = list2.next

        sortlist = sorted(comlist)  
        mergelist = []
        for val in sortlist:
            mergelist.append(ListNode(val))  
        for l in range(len(mergelist) - 1):
            mergelist[l].next = mergelist[l + 1]

        
        value = mergelist[0] if mergelist else None
        
        return mergelist[0] if mergelist else None



if __name__ == "__main__":
    
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    sol = Solution()
   
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    
    result = sol.mergeTwoLists(list1, list2)

    output = []
    while result:
        output.append(result.val)
        result = result.next
    print("Merged Linked List:", output)
