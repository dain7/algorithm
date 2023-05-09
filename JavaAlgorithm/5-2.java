import java.util.*;
  
public class Main {
    public String Solution(String s) {
        String answer = "";
        Stack<Character> stack = new Stack();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push('(');
            } else if (c == ')') {
                stack.pop();
            } else {
                if (stack.empty()) {
                    answer += Character.toString(c);
                }
            }
        }
        return answer;
    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        String s = in.next();
        System.out.println(T.Solution(s));
        return ;
    }
}