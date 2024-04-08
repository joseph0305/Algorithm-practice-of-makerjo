#include <string>


class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = s.length();
      
        int i = len;
        int count = 0;
        bool Notfirst_space = true;
        while(i != 0){
            i = i - 1;
            if(i == len-1 && s[i] == ' '  ){
                Notfirst_space = false;
            }
            if(s[i] != ' ' ){
                count++;
                Notfirst_space = true;
            }
            else if( s[i] == ' ' && Notfirst_space ){
                return count;
            }
        }
        return count;
        


    }
};

// rtrim 을 쓰려했지만 오류 때문에 못씀 (왜인지는 명확X)
// rtrim 구현 코드
  // static inline void rtrim(string &s) {
        //     s.erase(find_if(s.rbegin(), s.rend(),
        //     not1(std::ptr_funstd::isspace))).base(), s.end());
        // }
        // 파이썬에서 strip 함수를 구현 
        // Boost 라이브러리에 있지만 직접 구현 은 위처럼 //#include <boost/algorithm/string.hpp>
        // find_if(string이나 배열의 앞 포인터, 뒤포인터 , bool을 return 하는 단항함수 )
        // not1은 단항함수의 return 된 bool 값을 반대 값으로 만들어준다
        // ptr_funstd 은 함수 포인터 어댑터로 not1()안에는 단항함수 객체가 들어와야하는데 ,
        // 일반 함수가 들어가게 되므로 호환을 위해 써주게 된다. 호환위해 써주는게 어댑터
        //boost::trim_right(s);
