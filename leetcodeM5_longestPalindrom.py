class Solution:

    def longestPalindrome(self, s: str) -> str:
        re_list = []
        w = ""
        le = len(s)
        if le <= 1:
            return s
        for i in range(le):
            w = s[i]
            for j in range(i + 1, le):
                w += s[j]
                if w == w[::-1]:
                    re_list.append(w)

        if len(re_list) == 0:
            return s[0]
        else:
            return max(re_list, key=len)


# 부분집합 구하는 방법 (블로그)
#https://velog.io/@tks7205/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0


# Manacher 알고리즘 >> 이문제 푸는 가장 빠른 알고리즘
# 알고리즘 설명 유튜브 
# https://www.youtube.com/watch?v=l-XCWjps-UQ



class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s
        def ADDch(s):
            re = "$"
            for st in s:
                re += st
                re += "$"
            return re

        result = s[0]
        s = ADDch(s)
        p = [0] * len(s)

        rightBound = 0
        center = 0
        Max_len = 1

        for i in range(len(s)):
            # i < right면 dp를 사용할수 있는 상태인 거임 , 왼쪽에 이미 계산할걸 쓸 수 있는 상태가 된거임
            # 이미 계산된거 반영
            if i < rightBound:
                p[i] = min(p[2*center-i],rightBound-i)
            # i 주변으로 pal인지 체크
             # pal 맞으면 계속 확장 , 배열에 계속 반영
             # range를 넘어가면 stop , pal이 아니면 stop
             # dp 문제임 , 계산이 중복되면 반영해서 계산
            while i-p[i]-1 >= 0 and i+p[i]+1 < len(s) and s[i-p[i]-1] == s[i+p[i]+1]:
                p[i] += 1  

            # R 반영 , C 반영 
            # 지금 계산한 rightBound가 기존의 right보다 크다면
            # rightBound 업데이트 , center 도 업데이트 
            if i+p[i] > rightBound:
                rightBound = i+p[i]
                center = i
            if p[i] > Max_len:
                Max_len = p[i]
                result = s[i-p[i]:i+p[i]+1].replace("$","")

        return result





# N B N N B R 
#[0 0 0 0 0 0 0 0 0 0 0 0 0 ]
# $ N $ B $ N $ N $ B $ R $
# i
# c
# R