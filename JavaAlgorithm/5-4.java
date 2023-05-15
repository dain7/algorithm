import java.util.*;
  
public class Main {
    public int Solution(String input) {
        Stack<Integer> s = new Stack<>();
        Integer a, b;
        for (char c : input.toCharArray()) {
            if (c=='+') {
                a = s.pop();
                b = s.pop();
                s.push(b+a);
            } else if (c=='-') {
                a = s.pop();
                b = s.pop();
                s.push(b-a);
            } else if (c=='*') {
                a = s.pop();
                b = s.pop();
                s.push(b*a);
            } else if (c=='/') {
                a = s.pop();
                b = s.pop();
                s.push(b/a);
            } else {
                s.push(Character.getNumericValue(c));
            }
        }
        return s.pop();
    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        String input = in.next();
        System.out.println(T.Solution(input));
        return ;
    }
}