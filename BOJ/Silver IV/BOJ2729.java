//BOJ2729 이진수 덧셈 20210723
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());
        while(tc-- > 0) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            String a = stk.nextToken();
            String b = stk.nextToken();
            if (a.length() < b.length()) {
                String tmp = a;
                a = b;
                b = tmp;
            }
            String[] ans = binAdd(a.split(""), b.split("")).split("");
            String out = "";
            boolean flag = false;
            for(String s: ans){
                if(s.equals("1")) flag = true;
                if(!flag) continue;
                out += s;
            }
            bw.write(((out.length() == 0)? "0" : out) + "\n");
        }
        bw.flush();
        bw.close();
    }

    static String binAdd(String[] a, String[] b){
        int idx1 = a.length - 1, idx2 = b.length - 1;
        String ret = "";
        int carry = 0;
        while(idx2 >= 0){
            int ta = Integer.parseInt(a[idx1]), tb = Integer.parseInt(b[idx2]);
            int sum = ta + tb + carry;
            ret = ((sum % 2 == 0)? "0" : "1" )+ ret;
            carry = sum / 2;
            idx1--; idx2--;
        }
        while(idx1>=0){
            int ta = Integer.parseInt(a[idx1]);
            int sum = ta + carry;
            ret = ((sum % 2 == 0)? "0" : "1" )+ ret;
            carry = sum / 2;
            idx1--;
        }
        if(carry == 1) ret = "1" + ret;
        return ret;
    }

}