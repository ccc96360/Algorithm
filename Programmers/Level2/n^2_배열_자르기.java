//n^2 배열 자르기 월간 코드 챌린지 시즌 3 20211017
import static java.lang.Math.*;
class Solution {
    public int[] solution(int n, long left, long right) {
        long m = right - left + 1;
        int[] answer = new int[(int)m];
        long num = left;
        for(int i = 0; i < m; i++){
            long r = num / n, c = num % n;
            answer[i] = (int) max(r, c) + 1;
            num++;
        }
        return answer;
    }
}