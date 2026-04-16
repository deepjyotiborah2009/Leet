class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in s.split(' ')[::-1]:
            if i!='':
              return len(i)
              break
        