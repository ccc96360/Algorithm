//행렬의 곱셈 연습문제 20211105
class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int r1 = arr1.length, c1 = arr1[0].length, r2 = arr2.length, c2 = arr2[0].length;
        int[][] answer = new int[r1][c2];
        for(int r = 0; r < r1; r++){
            for(int c = 0; c < c2; c++){
                for(int i = 0; i < c1; i++){
                    answer[r][c] += arr1[r][i] * arr2[i][c];
                }
            }
        }
        return answer;
    }
}