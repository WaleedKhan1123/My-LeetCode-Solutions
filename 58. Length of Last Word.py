import re

# Your input string
s = "  Hello   world!  This is an example.  "

# Use regex to find words and spaces, preserving their order
elements = re.findall(r'\S+|\s+', s)

# Filter only words from elements to find the first and last words
words = [word for word in elements if word.strip()]
print(words)
if words:
    first_word = words[0]
    last_word = words[-1]

print("Split elements (words and spaces):", elements)
print("First word:", first_word)
print("Last word:", last_word)


# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
        
        
# if __name__ == "__main__":
#     sol = Solution()
#     s="Hello World"
#     result = sol.lengthOfLastWord(s)
#     print(result)