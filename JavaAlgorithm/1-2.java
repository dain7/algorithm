import java.util.Scanner;

/** 
 * 나의 풀이
 */
public class Main {
  public String solution(String word) {
    StringBuilder builder = new StringBuilder();
    
    for (char c : word.toCharArray()) {
    // 대소문자 변환한거랑 같으면 == 대소문자면
      if (c == Character.toUpperCase(c)) {
        // 소문자 변환해서 리턴
        builder.append(Character.toLowerCase(c));
      } else {
        builder.append(Character.toUpperCase(c));
      }
    }
    
    return builder.toString();
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.next();
    System.out.println(T.solution(word));
    return ;
  }
}


/*
 * 선생님 풀이
 */
  
public class Main {
  public String solution(String word) {
    String answer = "";
    for (char c : word.toCharArray()) {
    // Character에 is~~Case 사용
      if (Character.isUpperCase(c)) answer+=Character.toLowerCase(c);
      else answer+=Character.toUpperCase(c);
    }
    return answer;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String word = in.next();
    System.out.println(T.solution(word));
    return ;
  }
}