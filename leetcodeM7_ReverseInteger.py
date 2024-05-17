#include <climits>

class Solution {
public:
    int reverse(int x) {
        int y = 1;
        int result = 0;

        try{
            while(x != 0){
            if (  result > INT_MAX/10 || result < INT_MIN/10 )
            {
                throw overflow_error("Message");
            }
            result *= 10;
            result += x % 10;
            x = x / 10;
            }
        }
        catch(overflow_error& e){
            return 0;
        }

        cout << result ;
        return result;

    }
};