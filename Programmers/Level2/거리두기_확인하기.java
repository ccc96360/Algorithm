//거리두기 확인하기 2021 카카오 채용연계형 인턴십 20210923
import java.util.*;
import java.util.stream.*;

import static java.lang.Math.*;

class Solution {

    private final String PERSON = "P", PARTITION = "X", TABLE = "O";

    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        for (int i = 0; i < 5; i++) {
            answer[i] = solve(places[i]);
        }
        return answer;
    }

    public int solve(String[] place){
        String[][] board = new String[5][];
        for(int i = 0; i < 5; i++){
            board[i] = place[i].split("");
        }

        List<int[]> people = findPeople(board);

        for (int[] person1 : people) {
            for (int[] person2 : people) {
                int dist = manhattanDist(person1, person2);
                if(dist == 0) continue;
                if(dist == 1) return 0;
                if(dist == 2 && !hasAPartition(board, person1, person2)) return 0;
            }
        }

        return 1;
    }

    public boolean hasAPartition(String[][] board, int[] p1, int[] p2){
        int r1 = p1[0], c1 = p1[1], r2 = p2[0], c2 = p2[1];
        if(r1 == r2){
            return board[r1][(c1 + c2) / 2].equals(PARTITION);
        } else if(c1 == c2){
            return board[(r1 + r2) / 2][c1].equals(PARTITION);
        }else{
            return board[r1][c2].equals(PARTITION) && board[r2][c1].equals(PARTITION);
        }
    }

    public List<int[]> findPeople(String[][] board){
        List<int[]> ret = new ArrayList<>();
        for(int r = 0; r < 5; r++){
            for(int c = 0; c < 5; c++){
                if(board[r][c].equals(PERSON)){
                    ret.add(new int[]{r,c});
                }
            }
        }
        return ret;
    }

    public int manhattanDist(int[] p1, int[] p2){
        int r1 = p1[0], c1 = p1[1], r2 = p2[0], c2 = p2[1];
        return abs(r1 - r2) + abs(c1 - c2);
    }
}