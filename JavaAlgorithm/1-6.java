import java.util.Scanner;

// 나의 풀이
public class Main {
  public String Solution(String word) {
    String answer = "";
    for (char character : word.toCharArray()) {
      String w = Character.toString(character);
      if (!answer.contains(w)) {
        answer += w;
      }
    }
    return answer;
  }

  public String Solution(String word) {
    String answer = "";
    for (int i=0; i<word.length(); i++) {
      // 현재 인덱스와 해당 글자의 맨처음 인덱스와 같으면!
      if (word.indexOf(word.charAt(i)) == i) {
        answer += word.charAt(i);
      }
    }
    return answer;
  }


  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.next();
    System.out.println(T.Solution(word));
    return ;
  }
}