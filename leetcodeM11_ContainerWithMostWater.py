class Solution:

    def maxArea(self, height: List[int]) -> int:

        l = len(height)
        d_height = enumerate(height)

        for i, d in d_height:
            print(i, d)

            #종료조건 : l * height를 했을 때 지금 max에 들어가있는 값보다 무조건 작을 때
            #그전까지는 두개씩 찝어서 계산 : index 있고 두개 높이 있으니까 가능

        return

    #min(s), max(s) : 시간 복잡도 :  O(n)

    # le = len(height)
    # count = 0
    # # 나보다 w 가 작은데 h도 작은거는 계산할 필요 X
    # # 이전거보다 h가 큰 것 만 find
    # for i in range(le):
    #     for w in range(le-1,i,-1):

    #return 0
    # count = 0
    # re_arr = []
    # le = len(height)
    # for i in range(le):
    #     for w in range(1,le):
    #         if i+w >= le:
    #             break
    #         re_arr.append(w * min(height[i],height[i+w]))
    #         count += 1
    # print("c2",count)
    # return max(re_arr)

    # 7 3 3 8

    #https://hongcana.tistory.com/41

class Solution:

def maxArea(self, height: List[int]) -> int:

    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        area = (r - l) * min(height[r], height[l])
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


    # 7 3 3 8
    #https://www.youtube.com/watch?v=Kb20p6zy_14 (쉽게 설명)
    #https://hongcana.tistory.com/41
