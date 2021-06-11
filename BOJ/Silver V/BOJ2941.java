//BOJ2941 크로아티아 알파벳 20210611
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;


public class BOJ2941 {
	private static HashSet<String> croatiaAlphabet = new HashSet<String>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String str = br.readLine();
		initAlpha();
				
		int cnt = 0;
		String tmp = "";
		for(char s: str.toCharArray()) {
			tmp += s;
			if(tmp.length() == 2) {
				if(croatiaAlphabet.contains(tmp)) {
					tmp = "";
					cnt++;
				}
				else if(!tmp.startsWith("dz")) {
					tmp = tmp.substring(1);
					cnt++;
				}
			}
			else if(tmp.length() == 3) {
				if(tmp.equals("dz=")) {
					tmp = "";
					cnt++;
				}
				else {
					tmp = tmp.substring(2);
					cnt += 2;
				}
			}
		}
		if(tmp != "") cnt+=tmp.length();
		System.out.println(cnt);
	}
	
	public static void initAlpha() {
		croatiaAlphabet.add("c=");
		croatiaAlphabet.add("c-");
		croatiaAlphabet.add("dz=");
		croatiaAlphabet.add("d-");
		croatiaAlphabet.add("lj");
		croatiaAlphabet.add("nj");
		croatiaAlphabet.add("s=");
		croatiaAlphabet.add("z=");
	}

}
