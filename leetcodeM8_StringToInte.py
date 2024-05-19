class Solution:
  def myAtoi(self, s: str) -> int:
      MIN_INT = -2147483648
      MAX_INT = 2147483647
      s = s.strip()
      sign = 1
      result = ""
      re = 0
      metZero = False
      leadingSign = False
      print(s)
      for i in range(len(s)):
          if s[i] == "0":
              metZero = True
          if metZero and not s[i].isdigit():
              break
          if not leadingSign and s[i].isdigit():
              leadingSign = True

          if (s[i] == "-" or s[i] == "+") and i+1 < len(s) and s[i+1].isdigit() and not leadingSign:
              leadingSign = True
              if s[i] == "-":
                  sign = -1  
          elif not s[i].isdigit():
              break
          else:
              result += s[i]

      if result != "":
          re = int(result)
          re = re * sign
          if re > MAX_INT:
              return MAX_INT
          if re < MIN_INT:
              return MIN_INT 
      return re
