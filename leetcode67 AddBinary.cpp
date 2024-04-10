class Solution {
public:
    string addBinary(string a, string b) {
        
        string result;
        int i = a.length() - 1;
        int j = b.length() - 1;
        int rest = 0;
        int plate = 0;

        while( i>=0 || j>=0 || rest ){
            plate = 0;
            if( i >= 0){
                plate += a[i] - '0';
                i--;
            }
            if( j>=0 ){
                plate += b[j] - '0';
                j--;
            }
            plate += rest;
            result += plate % 2 + '0';
            rest = plate /=  2;
        }

        reverse(begin(result),end(result));
        return result;
    }
};


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

