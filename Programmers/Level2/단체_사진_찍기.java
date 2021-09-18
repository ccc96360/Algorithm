//단체 사진 찍기 2017 카카오 코드 본선 20210918
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

class Solution {

    String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};
    int cnt = 0;
    public int solution(int n, String[] data) {
        int answer = 0;

        Map<String, List<String[]>> conditions = new HashMap<>();
        Map<String, Integer> pos = new HashMap<>();

        for (String friend : friends) {
            pos.put(friend, -1);
            conditions.put(friend, new ArrayList<>());
        }

        for(String dat : data) {
            String[] tmp = dat.split("");
            String a = tmp[0], b = tmp[2], cond = tmp[3], num = tmp[4];

            conditions.get(a).add(new String[]{b, num, cond});
            conditions.get(b).add(new String[]{a, num, cond});
        }

        int[] loc = new int[8];

        cnt = 0;
        solve(conditions, 0, pos, loc);

        answer = cnt;
        return answer;
    }

    public void solve(Map<String, List<String[]>> conditions, int depth, Map<String, Integer> pos, int[] loc){
        if(depth == 8){
            cnt++;
        }else{
            for(int i = 0; i < 8; i++){
                String friend = friends[i];
                if(pos.get(friend) != -1) continue;
                if(canSeat(conditions.get(friend), depth, pos)) {
                    pos.put(friend, depth);
                    loc[depth] = i;
                    solve(conditions, depth + 1, pos, loc);
                    loc[depth] = 0;
                    pos.put(friend, -1);

                }
            }
        }
    }

    public boolean canSeat(List<String[]> condition, int loc, Map<String, Integer> pos){
        for (String[] v : condition) {
            String other = v[0], cond = v[2];
            int num = Integer.parseInt(v[1]);

            int otherLoc = pos.get(other);

            if(otherLoc == -1) continue;

            int diff = abs(loc - otherLoc) - 1;
            if(cond.equals("<") && diff >= num){
                return false;
            }
            if(cond.equals(">") && diff <= num){
                return false;
            }
            if(cond.equals("=") && diff != num){
                return false;
            }
        }
        return true;
    }
}