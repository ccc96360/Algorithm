//BOJ11656 접미사 배열 20210629
import java.io.*;
import java.util.Arrays;

public class BOJ11656 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String str = br.readLine();
        int n = str.length();
        String[] arr = new String[n];

        for(int i = 0; i < n; i++){
            arr[i] = str.substring(i);
        }
        Arrays.sort(arr);

        for(String v : arr){
            bw.write(v + "\n");
        }
        bw.flush();
        bw.close();
    }
}