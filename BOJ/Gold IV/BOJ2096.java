//BOJ2096 내려가기 20210706
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][3];
        for(int i = 0; i < n; i++){
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        int[] prevMax = {arr[0][0], arr[0][1], arr[0][2]};
        int[] prevMin = {arr[0][0], arr[0][1], arr[0][2]};

        for(int i = 1; i < n; i++){
            int[] nextMax = new int[3];
            int[] nextMin = new int[3];

            nextMax[0] = max(prevMax[0], prevMax[1]) + arr[i][0];
            nextMax[1] = max(max(prevMax[0], prevMax[1]), prevMax[2]) + arr[i][1];
            nextMax[2] = max(prevMax[1], prevMax[2]) + arr[i][2];

            nextMin[0] = min(prevMin[0], prevMin[1]) + arr[i][0];
            nextMin[1] = min(min(prevMin[0], prevMin[1]), prevMin[2]) + arr[i][1];
            nextMin[2] = min(prevMin[1], prevMin[2]) + arr[i][2];

            prevMax = nextMax;
            prevMin = nextMin;
        }

        System.out.println(Arrays.stream(prevMax).max().getAsInt() + " " + Arrays.stream(prevMin).min().getAsInt());
    }
}