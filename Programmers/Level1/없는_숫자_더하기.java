//없는 수자 더하기 월간 코드 챌린지 시즌3 20211003
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        boolean[] exist = new boolean[10];
        for(int v: numbers) exist[v] = true;
        for(int i = 0; i <= 9; i++) if(!exist[i]) answer += i;
        return answer;
    }
}