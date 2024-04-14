#include <algorithm>

class Solution {
public:
  void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int end = m + n;

    for (int i = m; i < end; i++) {
      nums1[i] = nums2[i - m];
    }

    sort(nums1.begin(), nums1.end());
  }
};