//BOJ1965 상자넣기 20210618
import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        List<Integer> arr = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        int[] arr2 = new int[n];
        Arrays.fill(arr2, 1);
        for(int i = 1; i < n; i++){
            int v = arr.get(i);
            for(int j = i - 1; j >= 0; j--){
                if (arr.get(j) < v && arr2[i] < arr2[j] + 1){
                    arr2[i] = arr2[j] + 1;
                }
            }
        }
        System.out.println(Arrays.stream(arr2).max().getAsInt());
    }
}