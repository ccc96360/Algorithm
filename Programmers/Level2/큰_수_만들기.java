//큰 수 만들기 코딩테스트 연습 / 탐욕법 20210930
class Solution {

    public String solution(String number, int k) {
        int n = number.length();
        StringBuilder sb = new StringBuilder();
        char[] arr = number.toCharArray();
        for (int i = 0; i < n; i++) {
            char v = arr[i];
            boolean top = true;
            for(int j = i + 1; j <= i + k && j < n; j++){
                if(arr[j] > v){
                    k--;
                    top = false;
                    break;
                }
            }
            if(n - i == k) break;
            if(top) sb.append(v);
        }
        return sb.toString();
    }
}