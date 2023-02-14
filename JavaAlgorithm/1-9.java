import java.util.Scanner;
  
public class Main {
  public Integer Solution(String word) {
    String answer = "";
    for (char w : word.toCharArray()) {
      if (!Character.isAlphabetic(w)) {
        answer += Character.toString(w);
      }
    }
    return Integer.parseInt(answer);
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.next();
    System.out.println(T.Solution(word));
    return ;
  }
}