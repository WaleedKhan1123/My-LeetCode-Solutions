class Solution(object):
    def mergeList(self, l1,l2):
        """
        :type s: str
        :rtype: int
        """
        newList = []
        print(f"l1 is {l1} and l2 {l2}")
        newList.append(i for i in l1 if l1[i]!= 0)
        print(newList)

        return newList


if __name__ == "__main__":
    sol = Solution()
    l1=[1,2,2,4,0,0]
    l2 = [1,3,7]
    result = sol.mergeList(l1,l2)
    print(result)
