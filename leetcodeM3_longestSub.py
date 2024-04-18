class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:

      dic = {0:""}
      chunk = ''

      for i in range(len(s)):
          stri = s[i:]
          chunk = ''
          for w in stri:
              if w not in chunk:
                  chunk += w
              else:
                  dic[len(chunk)] = chunk
                  chunk = w

          dic[len(chunk)] = chunk



      return max(dic)

# 동작은 하지만 exeeded time