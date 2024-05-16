class Solution:
  def convert(self, s: str, numRows: int) -> str:
      if numRows == 1:
          return s
      # row 에 따라 배열 개수 만들기
      arrs = []
      for _ in range(numRows):
          arrs.append([])


      reverse = True
      i = 0
      for j in range(len(s)):
          if j % (numRows-1) == 0:
              reverse = not reverse
          arrs[i].append(s[j])
          if reverse:
              i -= 1
          else:
              i += 1

      result = ""
      for a in arrs:
          result +=  ''.join(a)

      return result
