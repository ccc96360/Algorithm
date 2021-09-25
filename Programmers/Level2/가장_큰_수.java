//가장 큰 수 코딩테스트 연습/정렬 20210925
import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        return Arrays.stream(numbers)
                .mapToObj(String::valueOf)
                .sorted((o2, o1) -> (o1 + o2).compareTo(o2 + o1))
                .collect(Collectors.joining())
                .replaceFirst("^0+(?!$)", "");
    }
}