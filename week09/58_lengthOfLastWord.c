int lengthOfLastWord(char * s){
    int len = strlen(s), i = -1;
    while(len > 0 && s[len - 1] == ' ') len--;
    if (len < 0) return 0;
    for (i = len - 1; i >= 0; i--)
    {
        if (s[i] == ' ') break;
    }
    return len - i - 1;
}

