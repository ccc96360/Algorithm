//조이스특 코딩테스트 연습 / 탐욕법 20210927
import static java.lang.Math.*;

class Solution {

    int n;

    public int solution(String name) {
        n = name.length();
        boolean[] isChanged = new boolean[name.length()];
        char[] spelling = name.toCharArray();
        for(int i = 0; i < n; i++){
            if(spelling[i] == 'A') isChanged[i] = true;
        }

        int idx = findStartIndex(spelling);ㄴ
        int answer = min(idx, n - idx);

        while(idx != -1){
            char v = spelling[idx];
            isChanged[idx] = true;
            answer += min(v - 'A', 'Z' - v + 1);

            int[] next = nextIdxAndDist(idx, isChanged);
            idx = next[0];
            answer += next[1];
        }
        return answer;
    }

    private int[] nextIdxAndDist(int idx, boolean[] isChanged){
        int right = 0, left = 0, rIdx = idx, lIdx = idx;
        do{
            rIdx = (rIdx + 1) % n;
            right++;
            if(rIdx == idx) {
                rIdx = -1;
                break;
            }
        }while(isChanged[rIdx]);

        do{
            lIdx = (lIdx == 0)? (n - 1) : (lIdx - 1);
            left++;
            if(lIdx == idx){
                lIdx = -1;
                break;
            }
        }while (isChanged[lIdx]);

        if(rIdx == -1 && lIdx == -1) return new int[]{-1, 0};
        int[] ret = (right >= left)? new int[]{lIdx, left} : new int[]{rIdx, right};
        return ret;
    }

    private int findStartIndex(char[] spelling) {
        int idxP = 0, idxM = 0;
        while(true){
            if(spelling[idxP] != 'A') return idxP;
            if(spelling[idxM] != 'A') return idxM;
            idxP = (idxP + 1) % n;
            idxM = (idxM == 0) ? (n - 1) : (idxM - 1);
        }
    }
}