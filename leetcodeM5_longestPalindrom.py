class Solution:
  def longestPalindrome(self, s: str) -> str:
      re_list = []
      w = ""
      le = len(s)
      if le <= 1:
          return s
      for i in range(le):
          w = s[i]
          for j in range(i+1,le):
              w += s[j]
              if w == w[::-1]:
                re_list.append(w)


      if len(re_list) == 0:
          return s[0]
      else:
          return max(re_list, key=len) 

