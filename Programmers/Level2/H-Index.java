//H-Index 코딩테스트 연습 / 정렬 20210930
import java.util.*;

class Solution {

    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int n = citations.length;
        for(int h = 0; h <= 10000; h++){
            int lb = lowerBound(citations, h);
            int hUp = (citations[lb] >= h) ? (n - lb) : (n - lb - 1);
            if(hUp >= h) answer = h;
        }
        return answer;
    }
    private int lowerBound(int[] arr, int v){
        int l = 0, r = arr.length - 1;
        while(l < r){
            int mid = (l + r) / 2;
            if(arr[mid] >= v){
                r =  mid;
            }else{
                l = mid + 1;
            }
        }
        return r;
    }
}