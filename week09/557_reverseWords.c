char * reverseWords(char * s){
    int length = strlen(s);
    int i = 0;
    while (i < length){
        int start = i;
        while (i < length && s[i] != ' '){
            i++;
        }
        int left = start, right = i-1;
        while (left <= right){
            int temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
        while (i < length && s[i] == ' '){
            i++;
        }
    }
    return s;
}
