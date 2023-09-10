import java.util.*;
  
public class Main {
  public int[] solution(int n, int[] arr) {

    for (int i=1; i<n; i++) {
        int tmp = arr[i], j;
        for (j=i-1; j>=0; j--) { // i 전의 값 기준으로 거꾸로 간다. 
            if (arr[j] > tmp) { 
                arr[j+1] = arr[j];// 큰것들을 계속 뒤로뒤로뒤로 보냄. 
            } else {
                break;
            }
        }
        arr[j+1] = tmp;
    }
  	return arr;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
   
    int n = in.nextInt();
    int[] arr = new int[n];
    
    for (int i=0; i<n; i++) {
      arr[i] = in.nextInt();
    }
    

    for (int i : T.solution(n, arr)) {
      System.out.println(i + " ");
    }
    
    return ;
  }
}