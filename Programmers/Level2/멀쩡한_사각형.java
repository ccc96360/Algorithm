//멀쩡한 사각형 Summer/Winter Coding(~2019) 20211015
class Solution {
    
    public long solution(int w, int h) {
        long n = (long)w * (long)h;
        return n - solve(w, h);
    }
    
    long solve(long w, long h){
        long gcd = gcd(w, h);
        if(gcd == 1){
            return w + h - 1;
        }else{
            return solve(w / gcd, h / gcd) * gcd;   
        }
        
    }
    
    long gcd(long a, long b){
      long tmp;
      while(b != 0){
        tmp = a % b;
        a = b;
        b = tmp;
      }
      return a;
    }
}