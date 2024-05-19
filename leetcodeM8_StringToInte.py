class Solution:
  def myAtoi(self, s: str) -> int:
      MIN_INT = -2147483648
      MAX_INT = 2147483647
      s = s.strip()
      sign = 1
      result = ""
      re = 0
      
      leadingSign = False
      print(s)
      for i in range(len(s)):
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


# 문제가 영어여서 잘못 파악함
# 0일때 케이스를 특수하게 나눠서 처리했는데 , 그럴 필요가 없었음

## 다른분이 한 솔루션
class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()
        if s == "":
            return 0

        sign = 1
        i = 0
        if s[i] == "-":
            sign = -1
            i += 1

        elif s[i] == "+":
            sign = 1
            i += 1

        res = 0

        while i < len(s):
            if not s[i].isdigit():
                break

            res =  res*10+int(s[i]) 
            i += 1

        res = res * sign

        if res > 2**31 -1:
            return 2**31 -1
        elif res < -2**31:
            return  -2**31

        else:
            return res   


## 알고보니 +뒤에 숫자 있는지 체크여부도 불필요한거였음
# leading +,- 나온 후로 not digit이면 바로 멈춰버리는 케이스에 다 포함되는 거였음
# 내가 고민했던거 "+" , "3+"

class Solution:
  def myAtoi(self, s: str) -> int:
      MIN_INT = -2147483648
      MAX_INT = 2147483647
      s = s.lstrip()
      sign = 1
      result = ""
      re = 0
      leadingSign = False
      for i in range(len(s)):
          if not leadingSign and s[i].isdigit():
              leadingSign = True

          if (s[i] == "-" or s[i] == "+")  and not leadingSign:
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