//BOJ1735 분수 합 20210630

import java.io.*;
import java.util.StringTokenizer;

public class BOJ1735 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        Bunsu a = new Bunsu(Integer.parseInt(stk.nextToken()), Integer.parseInt(stk.nextToken()));

        stk = new StringTokenizer(br.readLine());
        Bunsu b = new Bunsu(Integer.parseInt(stk.nextToken()), Integer.parseInt(stk.nextToken()));

        System.out.println(Bunsu.add(a,b));
    }

    static class Bunsu{
        private int ja;
        private int mo;

        public Bunsu(int ja, int mo) {
            int min = (mo > ja) ? ja : mo;
            int gcd = 1;
            for(int i = 2; i <= min; i++){
                if(mo % i == 0 && ja % i == 0)
                    gcd = i;
            }
            this.ja = ja / gcd;
            this.mo = mo / gcd;
        }

        static Bunsu add(Bunsu a, Bunsu b){
            Bunsu ret;
            int jaA = a.getJa(), jaB = b.getJa();
            int moA = a.getMo(), moB = b.getMo();
            int ja = jaA * moB + jaB * moA;
            int mo = moA * moB;
            ret = new Bunsu(ja, mo);
            return ret;
        }


        public int getJa() {
            return ja;
        }

        public int getMo() {
            return mo;
        }

        @Override
        public String toString() {
            return ja + " " + mo;
        }
    }
}