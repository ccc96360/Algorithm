//BOJ11286 절대값 힙 20210703
import java.io.*;
import java.util.*;

import static java.lang.Math.abs;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<MyNum> pq = new PriorityQueue<>();
        for(int i = 0; i < n; i++){
            int tmp = Integer.parseInt(br.readLine());
            if(tmp == 0){
                MyNum out = pq.poll();
                if(out == null){
                    bw.write(0 + "\n");
                }
                else{
                    bw.write(out.getRealNum() + "\n");
                }
            }
            else{
                pq.add(new MyNum(tmp));
            }
        }
        bw.flush();
        bw.close();
    }

    static class MyNum implements Comparable<MyNum>{
        private int abs;
        private int realNum;

        @Override
        public int compareTo(MyNum o) {
            if(this.abs == o.getAbs()){
                return this.realNum - o.getRealNum();
            }
            return this.abs - o.getAbs();
        }

        public MyNum(int realNum) {
            this.abs = abs(realNum);
            this.realNum = realNum;
        }

        public int getAbs() {
            return abs;
        }

        public int getRealNum() {
            return realNum;
        }

        public void setAbs(int abs) {
            this.abs = abs;
        }

        @Override
        public String toString() {
            return "MyNum{" +
                    "abs=" + abs +
                    ", realNum=" + realNum +
                    '}';
        }
    }
}