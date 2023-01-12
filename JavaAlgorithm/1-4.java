import java.util.Scanner;
  
public class Main {
  public String Solution(String word) {
    String answer = "";
    for (int i=word.length()-1; i>=0; i--) {
      answer += word.charAt(i);
    }
    return answer;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int number = in.nextInt();
    for (int i=0; i<number; i++) {
      String word = in.next();
      System.out.println(T.Solution(word));
    }
    return ;
  }
}