//124 나라의 숫자 연습문제 20210920
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

class Solution {

    public String solution(int n) {
        int[] subSum = new int[19];
        subSum[0] = 0; subSum[1] = 3;
        for(int i = 2; i <= 18; i++){
            subSum[i] = (subSum[i-1] - subSum[i-2]) * 3 + subSum[i-1];
        }

        int digit = 1;
        for(int i = 1; i <= 18 ; i++){
            if(subSum[i] >= n){
                digit = i;
                break;
            }
        }
        n = n - subSum[digit - 1];
        String[] ans = new String[digit];
        for(int i = digit - 1; i >= 0; i--){
            int v = (int) pow(3, i);
            if(n % v != 0){
                ans[i] = (n/v == 0) ? "1" : ((n/v == 1) ? "2" : "4");
            }else{
                ans[i] = (n/v == 1) ? "1" : ((n/v == 2) ? "2" : "4");
                for(int j = i - 1; j >= 0; j--){
                    ans[j] = "4";
                }
                break;
            }
            n %= v;

        }

        return reverseAndJoin(ans);
    }

    public String reverseAndJoin(String[] s){
        List<String> tmp = Arrays.stream(s).collect(Collectors.toList());
        Collections.reverse(tmp);
        return tmp.stream().collect(Collectors.joining());
    }
}