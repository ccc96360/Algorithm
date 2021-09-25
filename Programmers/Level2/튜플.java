//튜플 2019 카카오 개발자 겨울 인턴십 20210924
import java.util.*;
import java.util.stream.*;

class Solution {

    public int[] solution(String s) {
        List<List<Integer>> set = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        StringBuilder num = new StringBuilder();
        for (char c : s.toCharArray()) {
            if('0' <= c && c <= '9'){
                num.append(c);
            }else {
                if (!num.toString().equals("")) {
                    tmp.add(Integer.parseInt(num.toString()));
                    num = new StringBuilder();
                }
                if (c == '}') {
                    if (tmp.isEmpty()) continue;
                    set.add(tmp);
                    tmp = new ArrayList<>();
                }
            }
        }
        List<List<Integer>> sorted = set.stream()
                .sorted(Comparator.comparingInt(List::size))
                .collect(Collectors.toList());

        int n = sorted.size();
        int[] answer = new int[n];

        Set<Integer> elements = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            List<Integer> li = sorted.get(i);
            for (Integer v : li) {
                if(!elements.contains(v)){
                    answer[i] = v;
                    elements.add(v);
                    break;
                }
            }
        }

        return answer;
    }
}