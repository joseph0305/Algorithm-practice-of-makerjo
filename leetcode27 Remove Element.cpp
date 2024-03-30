#include <vector>
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int k = 0;
        int j = 0;
        for(int i=0; i<len; i++){
            if( nums[i] != val){
                nums[j] = nums[i];
                
            }
            else{
                j -= 1;
                k += 1;
            }
            
            j++;
        }
        return len-k;
    }
};


// 좀 더 깔끔한 솔루션 
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int index = 0;
        for(int i = 0; i< nums.size(); i++){
            if(nums[i] != val){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
};

// 배운점 : if else 경우의 수 따질때 one case : j가 - 여야하는 상황 normal case : +가 유지 되어야하는 상황  이라면 반대로 생각해보자 (뒤집어 보자)
// 그렇다면 other side: j가 + 되는 상황 normal case : none -> 더 쉽게 코드를 줄일 수 있다
// case를 안쪽으로 생각 말고 뒤집어 생각해 보자
// 증, 감의 순서를 뒤집어 보자

// 내가 개선한 솔루션
#include <vector>
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int k = 0;
        int j = 0;
        for(int i=0; i<len; i++){
            if( nums[i] != val){
                nums[j] = nums[i];
                j++;
                //k += 1; k == j 이므로 return  j 해도 됨
            }
            
        }
        return j;
    }
};
