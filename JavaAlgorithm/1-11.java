// 나의 풀이
import java.util.Scanner;
  
public class Main {
  public String Solution(String word) {
    String now = "";
    int count = 0;
    String answer = "";
    int index = 0;
    for (char w : word.toCharArray()) {
      String w2 = Character.toString(w);
      if (index == word.length()-1) {
        if (now.equals(w2)) {
          count += 1;
          answer += now;
           if (count != 1) {
           answer += Integer.toString(count);
        	}
          break;
      	} else {
          answer += now;
           if (count != 1) {
           answer += Integer.toString(count);
        }
          answer += w2;;
          break;
      	}
      }
    
      if (now.equals("")) {
        now = w2;
        count += 1;
      } else if (now.equals(w2)) {
        count += 1;
      } else {
        answer += now;
        if (count != 1) {
           answer += Integer.toString(count);
        }
        now = w2;
        count = 1;
      }
      index += 1;
    }
    return answer;
  }

  
// 선생님 풀이
import java.util.Scanner;
  
public class Main {
  public String Solution(String str) {
    String answer = "";
    str = str + " ";
    int cnt = 1;
    for (int i=0; i<str.length()-1; i++) {
      if (str.charAt(i) == str.charAt(i+1)) cnt++;
      else {
        answer += str.charAt(i);
        if (cnt>1) answer += String.valueOf(cnt);
        cnt = 1;
      }
    }
    return answer;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    String str = in.next();
    System.out.println(T.Solution(str));
    return ;
  }
}