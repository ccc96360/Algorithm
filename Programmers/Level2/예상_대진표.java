//예상 대진표 2017 팁스타운 20210928
class Solution {

    public int solution(int n, int a, int b) {
        int answer = 1;
        if(a > b){
            int tmp = b;
            b = a; a = tmp;
        }
        while (!isMeet(a, b)) {
            a = (a + 1) / 2;
            b = (b + 1) / 2;
            answer++;
        }
        return answer;
    }
    private boolean isMeet(int a, int b){
        if(b - a == 1){
            return (a % 2 == 1) && (b % 2 == 0);
        }
        return false;
    }
}