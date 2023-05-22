import java.util.*;
  
public class Main {
    public String Solution(String seq, String subjects) {
        Queue<Character> q1 = new LinkedList<>();
  
        for (char c : seq.toCharArray()) {
            q1.add(c);
        }

        for (char c : subjects.toCharArray()) {
            if (q1.contains(c)) {
                if (q1.poll() != c) return "NO";
            }
        }

        if (!q1.isEmpty()) return "NO";
        return "YES";
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        String input1 = in.next();
        String input2 = in.next();
        System.out.println(T.Solution(input1, input2));
        return ;
    }
}