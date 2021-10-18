//교점에 별 만들기 위클리 챌린지 10주차 20211018
import java.util.*;

import static java.lang.Math.*;
class Solution {
    
    final int MAX_INF = Integer.MAX_VALUE, MIN_INF = Integer.MIN_VALUE;
    int n;
    
    public String[] solution(int[][] linesInput) {
        n = linesInput.length;
        Line[] lines = new Line[n];
        for(int i = 0; i < n; i++){
            lines[i] = new Line(linesInput[i]);
        }
        
        int mxX = MIN_INF, mnX = MAX_INF, mxY = MIN_INF, mnY = MAX_INF;
        List<int[]> points = new ArrayList<>();
        for(int i = 0; i < n - 1; i++){
            Line a = lines[i];
            for(int j = i + 1; j < n; j++){
                Line b = lines[j];
                int[] point = a.getIntersectPoint(b);
                if(point.length == 1) continue;
                int x = point[0], y = point[1];
                points.add(point);
                mxX = max(x, mxX);
                mnX = min(x, mnX);
                mxY = max(y, mxY);
                mnY = min(y, mnY);
            }
        }
        
        int mr = mxY - mnY + 1, mc = mxX - mnX + 1;
        char[][] ans = new char[mr][mc];
        for(int i = 0; i < mr; i++){
            Arrays.fill(ans[i], '.');
        }
        
        for(int[] p : points){
            int r = mxY - p[1], c = p[0] - mnX;
            ans[r][c] = '*';
        }
        
        String[] answer = new String[mr];
        for(int i = 0; i < mr; i++){
            answer[i] = new String(ans[i]);
        }
        return answer;
    }
    
    // ax + by + c = 0;
    class Line{
        long a;
        long b;
        long c;
        
        Line(){}
        Line(int[] line){
            this.a = line[0];
            this.b = line[1];
            this.c = line[2];
        }
        
        int[] getIntersectPoint(Line other){
            int[] notInteger = new int[]{-1};
            long oa = other.getA(), ob = other.getB(), oc = other.getC();
            long tmp = a * ob - b * oa;
            if(tmp == 0) return notInteger;
            long tmpX = b * oc - c * ob, tmpY = c * oa - a * oc;
            if(tmpX % tmp != 0 || tmpY % tmp != 0) return notInteger;
            long x = tmpX / tmp, y = tmpY / tmp;
            return new int[]{(int) x, (int) y};
        }
        
        long getA(){ return a; }
        long getB(){ return b; }
        long getC(){ return c; }
        
        @Override
        public String toString(){
            return a + "x + " + b + "y + " + c + " = 0";
        }
    }
}