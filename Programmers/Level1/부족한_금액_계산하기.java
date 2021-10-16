//부족한 금액 계산하기 위클리 챌린지 1주차 20211016
class Solution {
    public long solution(int price, int money, int count) {
        long n = (long) count;
        long ans = (((n * (n + 1L)) / 2L) * price) - money;
        return (ans < 0L)? 0L : ans;
    }
}