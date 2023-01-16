import java.util.Scanner;
  
public class Main {
  public String Solution(String word){
    word = word.toLowerCase();
    StringBuilder sb = new StringBuilder(word);
    String rev = sb.reverse().toString();
    // equalsIgnoreCase() 사용시 대소문자 구분 필요없음
    if (word.equals(rev)) {
      return "YES";
    } else {
      return "NO";
    }
  } 
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.next();
    System.out.println(T.Solution(word));
    return ;
  }
}