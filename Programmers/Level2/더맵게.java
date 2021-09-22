//더맵게 연습_Heap 20210922
import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int v :scoville){
            pq.add(v);
        }

        while(pq.peek() < K){
            if(pq.size() < 2) return -1;
            int a = pq.poll();
            int b = pq.poll();
            if(a == 0 && b == 0) return -1;
            pq.add(a + b * 2);
            answer++;
        }

        return answer;
    }

}