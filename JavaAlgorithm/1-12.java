import java.util.Scanner;


/*
* 나의 풀이
*/ 
public class Main {
  public String Solution(int cnt, String password) {
    String answer = "";
    
    for (int i=0; i<cnt; i++) {
      int start = i*7; // 7개씩 기준이므로 *7
      int end = start+7;
      String word = password.substring(start, end);
      
      String temp = "";
      for (int j=0; j<word.length(); j++) {
        if (word.charAt(j)=='#') temp+="1";
        else if (word.charAt(j)=='*') temp+="0";
      }
      int decimal = Integer.parseInt(temp, 2); // 2진수를 10진수로 변환
      answer += String.valueOf((char)decimal); // ascii code 찾기
    }
    return answer;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int cnt = in.nextInt();
    String password = in.next();
    System.out.println(T.Solution(cnt, password));
    return ;
  }
}

/*
* 선생님 풀이
*/

public class Main {
  public String Solution(int cnt, String password) {
    String answer = "";
    
    for (int i=0; i<cnt; i++) {
      String temp = password.substring(0, 7).replace('#', '1').replace('*', '0');
      int decimal = Integer.parseInt(temp, 2); // 2진수를 10진수로 변환
      answer += (char)decimal; // ascii code 찾기
      password = password.substring(7);
    }
    return answer;
  }
  
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int cnt = in.nextInt();
    String password = in.next();
    System.out.println(T.Solution(cnt, password));
    return ;
  }
}