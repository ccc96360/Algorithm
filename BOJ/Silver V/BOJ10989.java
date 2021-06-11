//BOJ10989 수 정렬하기 3 20210611
import java.io.*;
import java.util.Arrays;

public class BOJ10989 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i ++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        for(Integer v : arr){
            bw.write(v + "\n");
        }
        bw.flush();
        bw.close();
    }
}