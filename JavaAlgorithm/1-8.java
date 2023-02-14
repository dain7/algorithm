import java.util.Scanner;
  
public class Main {
  public String Solution(String word) {
    word = word.replaceAll("[^ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z0-9]", "");
    word = word.replaceAll(" ", "");
    
    String answer = "YES";
    String newWord = new StringBuilder(word).reverse().toString();
    if (!word.equalsIgnoreCase(newWord)) {
      answer = "NO";
    }
    return answer;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.nextLine();
    System.out.println(T.Solution(word));
    return ;
  }
}