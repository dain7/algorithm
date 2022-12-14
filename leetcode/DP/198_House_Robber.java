class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        int prev1 = 0; // 전까지의 최대값
        int prev2 = 0; // 전전까지의 최대값
        for (int num : nums) {
            int tmp = prev1; // 바로 직전의 값을 임시 저장한다.
            prev1 = Math.max(prev2 + num, prev1); // 현재+전전 최대값 vs 직전값 => 더 큰게 직전의 최대값
            prev2 = tmp; // 바로 직전의 값은 전전의 최대값으로 설정
    }
        return prev1;
    }
}