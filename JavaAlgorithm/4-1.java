import java.util.*;
  
public class Main {
    public char Solution(int n, String str) {
        char answer = "";
        Integer max_value = 0;
        HashMap<Character,Integer> hash = new HashMap<>();
        
        for (char s : str.toCharArray()) {
            hash.put(s, hash.getOrDefault(s, 0) + 1);
        }

        for (char key : hash.keySet()) {
            if (hash.get(key) >  max_value) {
                answer = key;
                max_value = hash.get(key);
            }
        }
        
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner in=new Scanner(System.in);
        int n = in.nextInt();
        String str = in.next();
        System.out.println(T.Solution(n, str));
        return ;
    }
}