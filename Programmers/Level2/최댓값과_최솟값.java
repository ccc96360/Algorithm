//최댓값과 최솟값 연습문제 20211105
import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int[] arr = Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(arr);
        sb.append(arr[0]).append(" ").append(arr[arr.length-1]);
        return sb.toString();
    }
}