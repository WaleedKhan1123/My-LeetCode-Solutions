import re
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        elements = re.findall(r'\S+|\s+', s)
        words = [words for words in elements if words.strip()]
        subtring_Length = len(words[-1])
        return subtring_Length
    
    
if __name__ == "__main__":
    sol = Solution()
    s="Hello World"
    result = sol.lengthOfLastWord(s)
    print(result)