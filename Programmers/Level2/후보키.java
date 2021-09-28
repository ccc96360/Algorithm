//후보키 2019 카카오 BLIND RECRUITMENT 20210928
import java.util.*;

class Solution {

    int r, c, answer;
    String[][] table;
    List<Set<Integer>> keys;

    public int solution(String[][] relation) {
        r = relation.length;
        c = relation[0].length;
        answer = 0;
        table = relation;
        keys = new ArrayList<>();
        for(int maxCol = 1; maxCol <= c; maxCol++){
            solve(maxCol, 0, new boolean[c], 0);
        }

        return answer;
    }

    private void solve(int maxCol, int depth, boolean[] selectedCol, int startIdx){
        if(depth == maxCol){
            StringBuilder tmp = new StringBuilder();
            for(int i = 0; i < c; i ++){
                if(selectedCol[i]) tmp.append(i);
            }

            if(!isUnique(selectedCol)) return;
            if(!isMinimality(selectedCol)) return;
            answer++;
        }else{
            for(int i = startIdx; i < c; i++){
                selectedCol[i] = true;
                solve(maxCol, depth + 1, selectedCol, i + 1);
                selectedCol[i] = false;
            }
        }
    }

    private boolean isUnique(boolean[] selectedCol) {
        Set<String> rows = new HashSet<>();
        for(int i = 0; i < r; i++){
            StringBuilder row = new StringBuilder();
            for(int j = 0; j < c; j++){
                if(!selectedCol[j]) continue;
                row.append(" ").append(table[i][j]);
            }

            String str = row.toString();
            if(rows.contains(str)){
                return false;
            }else{
                rows.add(str);
            }
        }
        return true;
    }

    private boolean isMinimality(boolean[] selectedCol) {
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < c; i ++){
            if(selectedCol[i]) set.add(i);
        }

        for (Set<Integer> key : keys) {
            if(set.containsAll(key)) return false;
        }
        keys.add(set);
        return true;
    }
}