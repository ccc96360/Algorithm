//BOJ01972 다음 순열 20210623
import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static int n;
    public static int[] curPermutation;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());
        curPermutation = new int[n];
        for(int i = 0; i < n; i++) {
            curPermutation[i] = Integer.parseInt(stk.nextToken());
        }
        int[] nextPermutation = nextPermutation(curPermutation);

        if(nextPermutation == null){
            System.out.println(-1);
        }
        else{
            for(int v: nextPermutation){
                bw.write(v + " ");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    public static int[] nextPermutation(int[] curP) {
        int size = curP.length;
        int[] ret = new int[size];
        int idx = -1;
        ret[0] =curP[0];
        for(int i = 0; i < n-1; i++){
            ret[i+1] = curP[i+1];
            if(curP[i] < curP[i+1]) idx = i;
        }
        if(idx == -1){
            return null;
        }

        for(int i = size - 1; i > idx; i--){
            if(ret[i] > ret[idx]){
                int tmp = ret[i];
                ret[i] = ret[idx];
                ret[idx] = tmp;
                break;
            }
        }

        int[] tmp = Arrays.copyOfRange(ret, idx + 1, size);
        int m = size - idx - 1;
        for(int i = 0; i < m; i++){
            ret[i+idx+1] = tmp[m - i - 1];
        }
        return ret;
    }
}