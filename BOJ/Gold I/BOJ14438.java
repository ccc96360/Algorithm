//BOJ14438 수열과 쿼리17 20210802

import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n, m, PIV = 1 << 17;
    static int[] arr = new int[PIV * 2];
    public static void main(String[] args) throws IOException {
        Arrays.fill(arr, Integer.MAX_VALUE);
        n = Integer.parseInt(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());
        for(int i = 1 ; i <= n; i++){
            update(i, nextInt(stk));
        }

        m = Integer.parseInt(br.readLine());
        while(m-- > 0){
            stk = new StringTokenizer(br.readLine());
            int op = nextInt(stk);
            if(op == 1){
                update(nextInt(stk), nextInt(stk));
            }else{
                bw.write(query(nextInt(stk), nextInt(stk)) + "\n");
            }
        }

        bw.flush();
        bw.close();
    }

    static void update(int idx, int v){
        idx += PIV;
        arr[idx] = v;
        while(idx / 2 > 0){
            idx /= 2;
            arr[idx] = min(arr[idx*2], arr[idx*2+1]);
        }
    }

    static int query(int left, int right){
        left += PIV; right += PIV;
        int ret = min(arr[left], arr[right]);
        while(left <= right){
            if(left % 2 == 1) ret = min(ret, arr[left++]);
            if(right % 2 == 0) ret = min(ret, arr[right--]);
            left /= 2;
            right /= 2;
        }
        return ret;
    }

    static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}