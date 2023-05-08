import java.util.*;
  
public class Main {
    public String Solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char x : s.toCharArray()) {
            if (x == ')') {
                if (stack.empty()) {
                    return "NO";
                } else {
                    stack.pop();
                }
            } else {
                stack.push(x);
            }
        }
        if (!stack.empty()) return "NO";
        return "YES";
    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        String s = in.next();
        System.out.println(T.Solution(s));
        return ;
    }
}