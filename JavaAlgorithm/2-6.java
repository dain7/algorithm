import java.util.*;

/**
* 내 풀이
 */
public class Main {
  // 소수인지 체크하는 함수
  public boolean isDecimal(Integer number) {
    boolean answer = true;
    if (number == 1) return false;
    for(int i=2; i<number; i++) {
      if (number%i == 0) {
        answer = false;
        break;
      }
    }
    return answer;
  }
  
  // 소수 찾기 함수
  public ArrayList<Integer> Solution(int n, int[] numbers) {
    ArrayList<Integer> answer = new ArrayList<>();
    for (int i=0; i<n; i++) {
      int number = numbers[i];
      StringBuilder sb = new StringBuilder(Integer.toString(number));
      String reverseString = sb.reverse().toString();
      Integer integer = Integer.parseInt(reverseString);
      if(isDecimal(integer)) {
        answer.add(integer);
      };
    }
    return answer;
  }

  // 메인 함수
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    int[] numbers = new int[n];
    
    for (int i=0; i<n; i++) {
      numbers[i] = in.nextInt();
    }
    
    for (Integer integer : T.Solution(n, numbers)) {
      System.out.print(integer + " ");
    };
    return ;
  }
}



/**
* 선생님 풀이
 */
 