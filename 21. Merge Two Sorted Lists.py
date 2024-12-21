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
        # Dummy node to simplify merging
        dummy = ListNode()
        current = dummy

        # Merge the two linked lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes from either list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return merged list starting at dummy.next
        return dummy.next

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
    print(result)