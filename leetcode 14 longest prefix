class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # string 안에 있는 str들을 하나씩 꺼네 가지고 있는 prefix를 자기 인데스 0부터 끝까지 조사한다.
        # if len(strs) == 1:
        #     return strs[0]
        # dic = {}
        # count = 0
        # for st in strs:
            
        #     for i in range(1,len(st)+1):
               
        #         for com in strs:
        #             if com[0:i] == st[0:i]:
        #                 count += 1
        #         if count > 1:
        #             dic[st[0:i]] = count
        #         count = 0
        # if len(dic) == 0:
        #     return ""
        # sorted_dict = sorted(dic.items(), key = lambda item: item[1], reverse = True)
        # if sorted_dict
        # return sorted_dict[0][0]

        # common 이 흔한이 아닌 공통의.... 로 해석됨...


        v = strs
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans
