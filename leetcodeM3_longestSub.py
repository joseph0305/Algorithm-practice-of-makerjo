class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = {0: ""}
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


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = {0: ""}
        chunk = ''
        le = len(s)
        i = 0

        while i < le:
            if s[i] not in chunk:
                chunk += s[i]
            else:
                dic[len(chunk)] = chunk
                j = i - 1
                while s[i] != s[j] and j != 0:
                    j -= 1
                i = j + 1
                chunk = s[i]
            print(i)

            i += 1
        dic[len(chunk)] = chunk

        return max(dic)


# 동작하고 exeeded time 통과 , 최종통과 but 시간 아직 오래걸림
