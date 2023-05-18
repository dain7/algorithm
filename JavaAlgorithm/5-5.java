import java.util.*;
  
public class Main {
    public int Solution(String s) {
        Stack<Character> stack = new Stack<>();
        int answer = 0;
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            } else {
                stack.pop();
                if (s.charAt(i-1) == '(') {
                    answer += stack.size();
                } else {
                    answer += 1;
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