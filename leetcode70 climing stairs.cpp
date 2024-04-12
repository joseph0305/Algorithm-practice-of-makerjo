class Solution {
public:
    int climbStairs(int n) {
        // 1 : 1way  
        // 2 : 1 , 2 : 2way
        // 3 : 111 , 21 , 12 : 3way
        // 4 // 1111 , 22 , 211 , 121 , 112 // 5 way
        // 5 1111, : 8
        // like 피보나치
        if (n == 1 || n == 2){
            return n;
        }
        int frist = 1;
        int second = 2;

        int i = 2;
        int container = 0;
        while( i != n){
            container = second;
            second = frist + second;
            frist = container;
            i++;
        }
        return second;
    }
};

// better solution 재귀 함수
class Solution {
public:
    int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return climbStairs(n-1) + climbStairs(n-2);
    }
};

// 재귀 함수 + memoization
class Solution {
public:
    int climbStairs(int n, unordered_map<int, int>& memo) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (memo.find(n) == memo.end()) {
            memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo);
        }
        return memo[n];
    }

    int climbStairs(int n) {
        unordered_map<int, int> memo;
        return climbStairs(n, memo);
    }
};
