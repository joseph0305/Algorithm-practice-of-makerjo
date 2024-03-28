#include <queue>

class Solution {
public:
    bool isValid(string s) {

        int len = s.length();
        queue<char> Q;

        for(int i=0; i<len; i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{' ){
                Q.push(s[i]);
            }
            else {
                if(Q.size() == 0){
                    return false;
                }
                else if(
                        (s[i] == ')' && Q.front() != '(') ||
                        (s[i] == ']' && Q.front() != '[') ||
                        (s[i] == '}' && Q.front() != '{') 
                        ){   return false;}
                else{
                    Q.pop();
                }
                
            }
        }
        if(Q.size() != 0){
            return false;
        }
      return true;
    }
};

// queue 를 사용하면 기존 "()" , "{}[]" , "{[]}" 같은 예제들도 true 일뿐만 아니라 )( 이렇게 반대로 나오지 않는 한 "([)]" 같은 경우도 true로 나옴
// 즉 열리고 닫히는 order 만 충족이 된다면 true가 됨

// 그러나 열렸으면 무조건 닫히는 괄호가 순서되로 와야한다라는 규칙과 함께, 수학에서 처럼 괄호안에 괄호가 있어야한다는 규칙이 들어간다면 "([)]" 같은 경우 false 가 된다. "(){}" 나 "{[]}" 같은 경우만 참이 됨.
// 그럴때는 stack을 쓴다
// 위와 똑같은 논리에서 stack을 쓰면 된다.


// 아래는 stack 썼을 때
#include <queue>
#include <stack>

class Solution {
public:
    bool isValid(string s) {

        int len = s.length();
        stack<char> Q;

        for(int i=0; i<len; i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{' ){
                Q.push(s[i]);
            }
            else {
                if(Q.size() == 0){
                    return false;
                }
                else if(
                        (s[i] == ')' && Q.top() != '(') ||
                        (s[i] == ']' && Q.top() != '[') ||
                        (s[i] == '}' && Q.top() != '{') 
                        ){   return false;}
                else{
                    Q.pop();
                }
                
            }
        }
        if(Q.size() != 0){
            return false;
        }
      return true;
    }
};


