
// 내 첫번째 솔루션
// 간단하지만 시간복잡도가 O(n) 임
class Solution {
public:
    int mySqrt(int x) {
         for(long long i=1; i<=x; i++){
             if(i*i == x)
                 return i;
             if(i * i > x){
                 return i - 1;
             }
         }
         return 0;
    }
};

// 내 두번째 솔루션
// binary 알고리즘 응용하여 코딩
// 예상 시간 복잡도 O(log n)

class Solution {
public:
    int mySqrt(int x) {
        if(x==0){
            return 0;
        }
        int start = 1;
        int end = x;
        long long mid = x / 2;
        while( end  > start + 1){
            if(mid*mid == x){
                return mid;
            }
            else if(mid*mid > x){
                end = mid;
            }
            else{
                start = mid;
            }
            mid = (start+end) / 2;
        }
        //cout << start, end;
        return start;

    }
};
