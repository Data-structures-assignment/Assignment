class Solution {
    public int reverse(int x) {
         int reversed = 0;
        
        while (x != 0) {
            int digit = x % 10;
            
            // Check for overflow before adding new digit
            if (reversed > 214748364 || (reversed == 214748364 && digit > 7)) return 0;
            if (reversed < -214748364 || (reversed == -214748364 && digit < -8)) return 0;
            
            reversed = reversed * 10 + digit;
            x /= 10;
        }
        
        return reversed;
        
    }
}
