//피보나치 수 연습문제 20211105
class Solution {
    
    int[] fibo = new int[100001];
    final int MOD = 1234567;
    
    public int solution(int n) {
        return fibo(n);
    }
    
    public int fibo(int n){
        if(n == 0) return 0;
        if(n == 1) return 1;
        if(fibo[n] != 0) return fibo[n];
        fibo[n] = (fibo(n - 1) + fibo(n - 2)) % MOD; 
        return fibo[n];
    }
}