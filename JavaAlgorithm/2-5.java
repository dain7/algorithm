import java.util.Scanner;
  
public class Main {
  public Integer Solution(int n) {
    int answer = 0;
    int[] ch = new int[n+1]; // int는 default값이 0이다.
    for (int i=2; i<=n; i++) {
      if(ch[i]==0) {
        answer++;
        for (int j=i; j<=n; j=j+i) {
          ch[j]=1;
        }
      }
    }
    return answer;
  }
  public static void main(String[] args){
    Main T = new Main();
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    System.out.println(T.Solution(n));
    return ;
  }
}