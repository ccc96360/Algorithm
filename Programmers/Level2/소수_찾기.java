//소수 찾기 코딩테스트 연습/완전탐색 20210926
import java.util.*;

class Solution {

    boolean[] isPrime = new boolean[10000000];
    Set<Integer> cases = new TreeSet<>();
    int  n;

    public int solution(String numbers) {
        int answer = 0;
        n = numbers.length();
        String[] arr = numbers.split("");

        makePrimes();
        for(int maxDepth = 1; maxDepth <= n; maxDepth++){
            solve(arr, 0, new String[maxDepth], new boolean[n], maxDepth);
        }
        for (Integer x : cases) {
            if (isPrime[x]) answer++;
        }

        return answer;
    }

    private void makePrimes() {
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for(int i = 2; i < 1000; i++){
            if(!isPrime[i]) continue;
            for(int j = i + i; j < 10000000; j += i){
                isPrime[j] = false;
            }
        }
    }

    private void solve(String[] arr, int depth, String[] curNum, boolean[] selected, int maxDepth) {
        if(depth == maxDepth){
            String num = String.join("", curNum);
            cases.add(Integer.parseInt(num));
        }else{
            for(int i = 0; i < n; i++){
                if(selected[i]) continue;
                selected[i] = true;
                curNum[depth] = arr[i];
                solve(arr, depth + 1, curNum, selected, maxDepth);
                selected[i] = false;
            }
        }
    }
}