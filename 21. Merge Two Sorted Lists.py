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
        i=0
        nodes = {}
        comlist = list1+list2
        sortlist = sorted(comlist)
        print(sortlist)
        for l in sortlist:
            i=i+1
            
        
        print(nodes[f"node{1}"].next)
if __name__ == "__main__":
    sol = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    result = sol.mergeTwoLists(list1,list2)
    print(result)