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
        # print(f"List is => {mergelist[0].val}")
        c = 0
        value = mergelist[0]
        while value is not None:
            # print(c)
            print(f"{value.val} =>",end="")
            value = value.next
            
            c+=1
        print(c)
            
if __name__ == "__main__":

    sol = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    result = sol.mergeTwoLists(list1,list2)
    print(result)