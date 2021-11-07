//JadenCase 문자열 만들기 연습문제 20211107
class Solution {
    
    int diff = 'A' - 'a';
    
    public String solution(String s) {
        int n = s.length();
        char[] arr = s.toCharArray();
        
        boolean isFirst = true;
        for(int i = 0; i < n; i++){
            if(isFirst){
                if(isLowCase(arr[i])){
                    arr[i] += diff;
                }
                isFirst = false;
            }else{
                if(isUpperCase(arr[i])) arr[i] -= diff;
            }
            if(arr[i] == ' ') isFirst = true;
        }
        
        return new String(arr);
    }
    
    boolean isUpperCase(char c){
        return 'A' <= c && c <= 'Z';
    }
    
    boolean isLowCase(char c){
        return 'a' <= c && c <= 'z';
    }
}