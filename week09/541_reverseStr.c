void swapstr(char * s, int left, int right){
    int i = left, j = right-1;
    while (i < j){
        s[i] ^= s[j];
        s[j] ^= s[i];
        s[i++] ^= s[j--];
    }

}

char * reverseStr(char * s, int k){
    int len = strlen(s);
    for (int i = 0; i < len; i += 2*k){
        if ((i+k) <= len) 
            swapstr(s, i, i+k);
        else
            swapstr(s, i, len);
    }
    
    return s;
}
