bool isPalindrome(int x) {
    int i = 0;
    int digit = 0;
    double reverse = 0;
    double original = 0;

    original = x;   // store original number
    
    while (x > 0)
    {
        // break down the number and build it in reverse to compare
        digit = x % 10;
        x = x / 10;
        // printf("x: %d", x);

        // build digit in reverse
        reverse = reverse * 10 + digit;
        // printf("reverse: %d", reverse);
    }

    // compare original to reverse
    if (original == reverse)
    {
        printf("original: %d ", original);
        printf("reverse: %d", reverse);
        return true;
    }

    return false;
}
