//BOJ2217 로프 20210615
import java.io.*;
import java.util.*;

import static java.lang.Math.max;

public class BOJ2217 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        int maxWeight = 0;
        for(int i = 0; i < n; i++){
            maxWeight = max(arr[i] * (n-i), maxWeight);
        }
        System.out.println(maxWeight);
    }
}