class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        String = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','X':'x','Y':'y','Z':'z'}
        print(len(String))
if __name__ == "__main__":
    sol = Solution()
    s = "Hello"
    result = sol.toLowerCase(s)
    print(result)        