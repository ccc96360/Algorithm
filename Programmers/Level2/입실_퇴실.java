//입실 퇴실 위클리 챌린지 7주차 20211006
import java.util.*;

class Solution {
    public int[] solution(int[] enter, int[] leave) {
        int n = enter.length;
        int[] answer = new int[n];
        Set<Integer> room = new TreeSet<>();
        int leaveIdx = 0;
        for(int i = 0; i < n; i++){
            int person = enter[i];
            
            answer[person - 1] = room.size();
            for(int v : room){
                answer[v - 1] += 1;
            }
            room.add(person);
            
            int outPerson = leave[leaveIdx];
            while(room.contains(outPerson)){
                room.remove(outPerson);
                if(leaveIdx == n - 1) break;
                outPerson = leave[++leaveIdx];
            }
        }
        
        return answer;
    }
}