import java.util.*;
  
public class Main {
  public String Solution(String s1, String s2) {
    String answer = "YES";
    HashMap<Character, Integer> map = new HashMap<>();
    
    for (char c : s1.toCharArray()) {
      map.put(c, map.getOrDefault(c, 0)+1);
    }
    
    for (char c : s2.toCharArray()) {
      if(!map.containsKey(c)) {
        answer = "NO";
        break;
      } 
      if (map.get(c) > 0) {
        map.put(c, map.get(c)-1);
      } else {
        answer = "NO";
        break;
      }
    }
    
    return answer;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String s1 = in.next();
    String s2 = in.next();
    System.out.println(T.Solution(s1, s2));
    return ;
  }
}