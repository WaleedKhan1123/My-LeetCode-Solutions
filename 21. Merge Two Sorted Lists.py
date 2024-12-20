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
        mergelist = []
        for l in range(len(sortlist)-1):
            mergelist.append(ListNode(sortlist[l]))
        for l in range(len(mergelist)-1):
            mergelist[l].next = mergelist[l+1]
        print("List is =>")
        for l in range(len(mergelist)):
            print(f"{mergelist[l].val} =>")
            
            
if __name__ == "__main__":
    sol = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    result = sol.mergeTwoLists(list1,list2)
    print(result)