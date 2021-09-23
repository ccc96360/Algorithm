//[1차] 뉴스 클러스터링 2018 KAKAO BLIND RECRUITMENT 20210923
import java.util.*;
import java.util.stream.*;

import static java.lang.Math.*;

class Solution {

    private final int KEY = 65536;

    public int solution(String str1, String str2) {
        int answer = 0;

        Map<String, Integer> map1 = makeMap(str1.toLowerCase());
        Map<String, Integer> map2 = makeMap(str2.toLowerCase());

        Map<String, Integer> union = new TreeMap<>();
        int ja = 0;
        for (String s1 : map1.keySet()) {
            int v1 = map1.get(s1);
            if(map2.containsKey(s1)){
                int v2 = map2.get(s1);
                ja += min(v1, v2);
                union.put(s1, max(v1, v2));
            }else{
                union.put(s1, v1);
            }
        }

        for(String s2: map2.keySet()){
            if(!map1.containsKey(s2)){
                union.put(s2, map2.get(s2));
            }
        }

        int mo = 0;
        for(String s : union.keySet()){
            mo += union.get(s);
        }
        if(ja == 0 && mo == 0) return KEY;

        double res = (double) ja /  (double) mo;
        answer = (int)(res * KEY);
        return answer;
    }

    private Map<String, Integer> makeMap(String str1) {
        Map<String, Integer> ret = new TreeMap<>();
        for(int i = 0; i < str1.length() - 1; i++){
            char s1 = str1.charAt(i), s2 = str1.charAt(i + 1);
            if(!isAlpha(s1) || !isAlpha(s2)) continue;
            String word = String.valueOf(s1) + String.valueOf(s2);
            ret.put(word, ret.getOrDefault(word, 0) + 1);
        }
        return ret;
    }

    private boolean isAlpha(char s){
        return 'a' <= s && s <= 'z';
    }
}