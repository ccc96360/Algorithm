//2개 이하로 다른 비트 월간 코드 챌린지 시즌 2 20211001
class Solution {
    public long[] solution(long[] numbers) {
        int n = numbers.length;
        long[] answer = new long[n];
        for(int i = 0; i < n; i++){
            answer[i] = f(numbers[i]);
        }
        return answer;
    }
    
    private long f(long x){
        String str = "0" + Long.toBinaryString(x);
        int n = str.length(), exp = 1;
        if(str.charAt(n - 1) == '0') return x + 1;
        for(int i = n - 2; i > 0; i--){
            if(str.charAt(i) == '0'){
                return x + (1L << exp) - (1L << (exp - 1));
            }
            exp++;
        }
        return x + (1L << exp) - (1L << (exp - 1));
    }

}