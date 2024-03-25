class Solution {
public:
    bool isPalindrome(int x) {
      // 첫 번째 내 솔루션 ( str으로 바꾸어 인덱싱으로 비교하기 )
        // bool result = true;
        // string s = to_string(x);
        // int len = s.length();
        // int loop = len / 2;
        // for (int i=0; i<loop; i++){
        //     if (s[i] !=  s[len-1-i])
        //         result = false;
        // }
        
        // return result;

    // 전문 솔루션
    // 1.  반복문으로 digit을 뒤에서부터 떼어내어 반대로 만들기 
        // if (x < 0){
        //     return false;
        // }

        // int reverse = 0;
        // int tmp = x;
        // int digit;

        // while(tmp > 0){
        //     digit = tmp % 10;
        //     reverse = reverse * 10 + digit;
        //     tmp /= 10;
        // }

        // return ( x == reverse );

    // 2. 반절만 그렇게 하기
    // bool isPalindrome(int x) {
    //     if (x < 0 || (x != 0 && x % 10 == 0)) {
    //         return false;
    //     }

    //     int reversed = 0;
    //     while (x > reversed) {
    //         reversed = reversed * 10 + x % 10;
    //         x /= 10;
    //     }
    //     return (x == reversed) || (x == reversed / 10);
    // }
};

        
    }
};
