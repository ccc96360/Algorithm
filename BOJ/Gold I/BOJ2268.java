//BOJ2268 수들의 합 20210720
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n, m, PIV = 1 << 20;
    static long[] tree = new long[PIV*2];
    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = nextInt(stk); m = nextInt(stk);
        while(m-- > 0){
            stk = new StringTokenizer(br.readLine());
            int cmd = nextInt(stk), a = nextInt(stk), b = nextInt(stk);
            if(cmd == 0){
                bw.write(query(min(a,b), max(a,b)) + "\n");
            }else{
                update(a, b);
            }
        }
        bw.flush();
        bw.close();
    }

    static void update(int idx, int v){
        idx += PIV;
        tree[idx] = v;
        while((idx/2) > 0){
            idx /= 2;
            tree[idx] = tree[idx*2] + tree[idx*2 + 1];
        }
    }

    static long query(int l, int r){
        long ret = 0L;
        l += PIV; r += PIV;
        while(l <= r){
            if(l % 2 == 1) ret += tree[l++];
            if(r % 2 == 0) ret += tree[r--];
            l /= 2;
            r /= 2;
        }
        return ret;
    }

    static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}