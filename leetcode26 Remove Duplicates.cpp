#include <array>
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    
        int len = nums.size();
        set<int> S;
        
        for(int i=0; i<len; i++){
            S.insert(nums[i]);
        }
        int i = 0;
        for(set<int>::iterator iter = S.begin(); iter != S.end(); iter++){
            nums[i] = *iter;
            i++;
        }

        return S.size();

    }
};
