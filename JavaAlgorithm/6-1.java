
class Main {
    public int[] solution(int n, int[] arr) {
        for (int i=0; i<n-1; i++){
            int idx = i;
            for (int j=i+1; j<n; j++) {
                if (arr[j] < arr[idx]) idx=j;
            }
            int tmp = arr[i];
            arr[i] = arr[idx]; // idx에는 제일 작은 값 -> i에 해당 값 저장
            arr[idx] = tmp;

        }

        return arr;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++) arr[i] = kb.nextInt();
        for (int x : T.solution(n, arr)) System.out.println(x+ " ");
    }
}