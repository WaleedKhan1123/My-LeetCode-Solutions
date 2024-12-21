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
        # Step 1: Extract values from list1 and list2 into a Python list
        comlist = []
        while list1:
            comlist.append(list1.val)
            list1 = list1.next
        while list2:
            comlist.append(list2.val)
            list2 = list2.next

        # Step 2: Sort the combined list
        sortlist = sorted(comlist)
        print(f"Sorted List: {sortlist}")  # Debug print

        # Step 3: Create a linked list from the sorted values
        mergelist = []
        for val in sortlist:
            mergelist.append(ListNode(val))  # Create nodes

        # Step 4: Link the nodes
        for l in range(len(mergelist) - 1):
            mergelist[l].next = mergelist[l + 1]

        # Debug: Print the merged linked list
        value = mergelist[0] if mergelist else None
        while value:
            print(f"{value.val} => ", end="")
            value = value.next
        print("None")  # End of the list

        # Return the head of the merged list
        return mergelist[0] if mergelist else None


# Example to Test
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    sol = Solution()
    # Input linked lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    # Call the function
    result = sol.mergeTwoLists(list1, list2)

    # Print the result as a Python list for verification
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print("Merged Linked List:", output)
