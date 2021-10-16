//상호 평가 위클리 챌린지 2주차 20211016
import static java.lang.Math.*;
class Solution {
    
    final int EXCEPT = -1;
    public String solution(int[][] scores) {
        String answer = "";
        int n = scores.length;
        
        for(int c = 0; c < n; c++){
            int selfEval = scores[c][c];
            int mx = -1, mn = 101;
            boolean dup = false;
            for(int r = 0; r < n; r++){
                if(r == c) continue;
                int score = scores[r][c];
                if(score == selfEval) dup = true;
                mx = max(mx, score);
                mn = min(mn, score);
            }
            if(dup) continue;
            if(mx < selfEval || mn > selfEval) scores[c][c] = EXCEPT;
        }
        
        for(int c = 0; c < n; c++){
            int cnt = 0, sum = 0;
            for(int r = 0; r < n; r++){
                int score = scores[r][c];
                if(score == EXCEPT) continue;
                cnt++;
                sum += score;
            }
            answer += getGrade(sum / cnt);
        }
        return answer;
    }
    String getGrade(int score){
        if(score >= 90) return "A";
        else if(score >= 80) return "B";
        else if(score >= 70) return "C";
        else if(score >= 50) return "D";
        else return "F";
    }
}