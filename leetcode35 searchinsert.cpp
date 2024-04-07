#include <array>
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        for(int i=0; i<len; i++){
            if(nums[i] >= target){
                return i;
            }
        }
        return len;
    }
};

// 다른 사람 솔루션 binary 알고리즘 , O(log n) 시간 복잡도
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low=0;
        int high=nums.size();
        int mid;
        if(target>nums[high-1]){
            return high;
        }
        while(low<=high){
              mid=(low+high)/2;
            if(nums[mid]==target){  
                return mid;
            }
          
            if(target<nums[mid]){     
            high=mid-1;    
            }else{
            low=mid+1;        
            }
          
        }
         return  low;   
    }
};
