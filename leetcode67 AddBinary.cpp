#include <string>
#include <bitset>
class Solution {
public:
    string addBinary(string a, string b) {
        
        
        float deci_a=0 , deci_b=0;
        //int a1 = stoi(a);
        //int b1 = stoi(b);
        int len_a = a.length();
        int len_b = b.length(); 

        for(int j =0 ; j<len_a ; j++){
		    deci_a += (a[len_a-j-1] - '0') * pow(2,j);
	    }
        for(int j =0 ; j<len_b ; j++){
		    deci_b += (b[len_b-j-1]-'0') * pow(2,j) ;
	    }

        //  for(int j =0 ; b1>0 ; j++){
		//     deci_b += (b1%10) * pow(2,j) ;
		//     b1/=10;
	    // }
        cout << deci_a << "\n";
        cout << deci_b << "\n";
        long long sum = deci_a + deci_b;
        if(sum == 0){
            return "0";
        }
        //string result = bitset<16>(sum).to_string();
        //cout << sum << "\n";
        long long res1 = 0;
        for(long long i =1; sum>=1; i*=10){
		    res1 = (sum%2)*i + res1;
		    sum /=2;
	    }
        //cout << res1 << "\n";
        // bool frist = true;
        // string Final = "";

        // for(int i=0; i<result.length(); i++){
        //     if( result[i] == '1' && frist ){
        //         frist = false;
        //         Final += result[i];
        //     }
        //     else if( !frist ){
        //         Final += result[i];
        //     }
        // }
        return to_string(res1);
        
    }
};////////////////////////////////////////////// 해결 아직 못함 


class Solution {
 public:
  string addBinary(string a, string b) {
    string ans;
    int carry = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;

    while (i >= 0 || j >= 0 || carry) {
      if (i >= 0)
        carry += a[i--] - '0';
      if (j >= 0)
        carry += b[j--] - '0';
      ans += carry % 2 + '0';
      carry /= 2;
    }

    reverse(begin(ans), end(ans));
    return ans;
  }
};

