# Definition for singly-linked list.
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
if __name__ == "__main__":
   if __name__ == "__main__":
    
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    sol = Solution()
   
    head = [1,2,3,4,5]

    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    result = sol.reverseList(head)
    output = linked_list_to_list(result)
    print("Merged Linked List:", output)